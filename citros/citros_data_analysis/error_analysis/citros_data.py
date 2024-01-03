import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.patches import Ellipse
from scipy.optimize import minimize
from scipy.interpolate import interp1d
from itertools import cycle
from numpy.typing import ArrayLike
from typing import Union, Optional
import matplotlib.figure
from .citros_stat import CitrosStat
import warnings

class CitrosData:
    """
    Create CitrosData object, that allows to bin and interpolate data.

    CitrosData object has two main attributes: 'data' - the vector of depending variables, 
    and all other additional columns - 'addData'. Both 'data' and 'addData' attributes contains pandas.DataFrame.

    Parameters
    ----------
    db : DataFrame or tuple of two DataFrames or None, optional
        If `db` is a DataFrame, column `data_label` is supposed to be a data sample and set to a 'data' attribute of a CitrosData object.
        The additional information about data may be extracted from columns labeled as:
            'type_name' - specify type of the data, set to the 'type' attribute,
            'units' - data units, set to the 'units' attribute.
            'parameter_label' - column with dict, specifying the parameters, if it is presented, the first row is set as parameters.
        All other columns are assigned to 'addData' attribute.
    type_name : str, optional
        Specifies type of the data.
    units : str, optional
        Specifies units of the data.
    data_label : str or list of str, default 'data'
        Specifies label of the data in DataFrame
    parameters : dict
        Parameters. Mostly used in regression analysis.
    parameter_label : str or list of str
        Specify label of a column in a pandas DataFrame, where the parameters are written as a dict.
        Used only if `db` is a pandas DataFrame and `parameters` is not specified.
    sid_label : str, default 'sid'
        label of the sim run id column (usually 'sim_run_id' or 'sid').
    omit_nan_rows : bool, default None
        If True, any rows containing one or more NaN values will be excluded from the analysis, see `Notes`.
    inf_vals : None or float, default 1e308
        If specified, all values from `data_label` column that exceed the provided value in absolute terms 
        will be treated as NaN values. If this functionality is not required, set inf_vals = None.

    Notes
    -----
    If `omit_nan_rows` set True in case of multidimensional vectors, the mean and covariance matrices will be calculated 
    only for rows that do not contain NaN values in all columns of the vector.
    Otherwise, if `omit_nan_rows` is set to False, columns are treated individually.
    The mean values are computed over non-NaN values within each column, and the elements of the covariance 
    matrices are calculated pairwise, for rows without NaN values.
    For example, for 3-dimensional vector:

    ```code
    +----+-----+-----+
    | x  | y   | z   |
    +====+=====+=====+
    | 1  | 3   | NaN |
    +----+-----+-----+
    | 2  | NaN | 5   |
    +----+-----+-----+
    | 3  | 5   | 6   |
    +----+-----+-----+
    | 4  | 7   | 7   |
    +----+-----+-----+
    ```

    if `omit_nan_rows` set True, the first and the second rows will be omitted from all calculations, while 
    in case `omit_nan_rows` set False, NaN values will be omitted only when the column is used in calculations. 
    For example, for mean calculations difference is the follows:

    ```code
	omit_nan_rows = True   omit_nan_rows = False
    +-----+---+-----+      +-----+---+---+
    |  x  | y | z   |      |  x  | y | z |
    +=====+===+=====+      +=====+===+===+
    | 3.5 | 6 | 6.5 |      | 2.5 | 5 | 6 |
    +-----+---+-----+      +-----+---+---+
    ```
    """

    def __init__(self, db = None, type_name = '', units = '', data_label = 'data', 
                 parameters = None, parameter_label ='', sid_label = 'sid', omit_nan_rows = None, inf_vals = 1e308):

        if parameters is None:
            parameters = {}
        
        if db is None:
            # self.type = type_name
            self.units = units
            self.data = pd.DataFrame()
            self.data_dim = 0
            self.addData = pd.DataFrame()
            self.filter = pd.DataFrame()
            self.parameters = parameters
            self.sid_label = sid_label
            self.inf_vals = inf_vals
            if omit_nan_rows is None:
                self.omit_nan_rows = True
            else:
                self.omit_nan_rows = omit_nan_rows
            if isinstance(data_label, str):
                self.data_label = [data_label]
            elif isinstance(data_label, list):
                self.data_label = data_label.copy()
        
        if isinstance(db, tuple):
            data, addData = db

            if (data is not None) and (addData is not None):
                if len(data) != len(addData):
                    raise ValueError('len(data) must match len(addData)')
                if data.index.to_list() != addData.index.to_list():
                    raise IndexError('indexes of data and addData must be the same')

            self.type = type_name
            self.units = units
            if omit_nan_rows is None:
                self.omit_nan_rows = True
            else:
                self.omit_nan_rows = omit_nan_rows

            self.inf_vals = inf_vals

            if data is None:
                self.data = pd.DataFrame()
                self.data_dim = 0
                self.filter = pd.DataFrame()
            else:
                self._set_data(data)
            if addData is None:
                self.addData = pd.DataFrame()
            else:
                self.addData = addData.fillna(np.nan)
            
            self.parameters = parameters.copy()
            self.sid_label = sid_label
            
        if isinstance(db, CitrosData):
            if type_name == '':
                try:
                    self.type = db.type
                except:
                    self.type = type_name
            else:
                self.type = type_name

            if units == '':
                try:
                    self.units = db.units
                except:
                    self.units = units
            else:
                self.units = units
            
            try:
                self.parameters = db.parameters.copy()
            except:
                self.parameters = parameters.copy()

            try:
                self.sid_label = db.sid_label
            except:
                self.sid_label = sid_label
            
            if omit_nan_rows is None:
                self.omit_nan_rows = db.omit_nan_rows
            else:
                self.omit_nan_rows = omit_nan_rows

            if inf_vals is None:
                self.inf_vals = db.inf_vals
            else:
                self.inf_vals = inf_vals

            self._set_data(db.data)
            self.addData = db.addData.fillna(np.nan).copy()

        if isinstance(db, pd.DataFrame):
            drop_column = []

            self.type = type_name

            self.units = units

            self.parameters = {}
            if len(parameters) == 0:
                if isinstance(parameter_label, str) and parameter_label != '':
                    try:
                        self.set_parameter(parameter_label, db[parameter_label].iloc[0])
                    except:
                        self.parameters = {}
                elif isinstance(parameter_label, list):
                    try:
                        for item in parameter_label:
                            self.set_parameter(item, db[item].iloc[0])
                    except:
                        self.parameters = {}
                else:
                    self.parameters = {}
            else:
                self.parameters = parameters.copy()

            self.sid_label = sid_label
            if isinstance(data_label, str):
                data_label = [data_label]
            elif isinstance(data_label, list):
                data_label = data_label.copy()
            else:
                print('error: data_label must be str or list of str')
            if omit_nan_rows is None:
                self.omit_nan_rows = True
            else:
                self.omit_nan_rows = omit_nan_rows
            self.inf_vals = inf_vals
            for item in data_label:
                if item not in db.columns:
                    print(f"error: The column '{item}' does not exist")
                    return
            self._set_data(db[data_label])
            drop_column += data_label
            self.addData = db.drop(columns=drop_column).fillna(np.nan)

        self._set_index_level_names()

    def _set_data(self, dataset):
        """
        Set 'data' attribute of the CitrosData object

        Parameters
        ----------
        dataset : Series or DataFrame
            May contains dicts or lists in rows or their combination (dict of lists, list of dicts, etc)
        """
        k = []
        self._resolve_data(dataset, k)
        self.data = pd.concat(k, axis = 1).fillna(np.nan)
        self.data_dim = self.data.shape[1]
        self.data_label = list(self.data.columns)
        # self.filter = self.data.notna().all(axis = 1)

        if self.inf_vals is not None and self.inf_vals not in ['none', 'None']:
            self.filter = self.data.notna() & ((abs(self.data) - self.inf_vals) < 0)
        else:
            self.filter = self.data.notna()

        if self.omit_nan_rows:
            self.filter= pd.DataFrame(columns = self.data.columns, index = self.data.index, data = {col: self.filter.all(axis = 1) for col in self.data.columns})
        
    def _resolve_data(self, dataset, k):
        """
        Recursively turns all dictionaries and lists to columns.

        Parameters
        ----------
        dataset : pandas.Series or pandas.DataFrame
            Input data
        k : list
            Output list of pandas.Series
        """
        if isinstance(dataset, pd.Series):
            if isinstance(dataset.iloc[0], (list, np.ndarray)):
                dataset_item = dataset.apply(lambda x: x[n] for n in range(len(dataset.iloc[0])))
                dataset_item.columns = [dataset.name+'['+str(n)+']' for n in range(len(dataset.iloc[0]))]
                self._resolve_data(dataset_item, k)
            elif isinstance(dataset.iloc[0], dict):
                dataset_item = dataset.apply(lambda x: x[k] for k in dataset.iloc[0].keys())
                keys =  list(dataset.iloc[0].keys())
                dataset_item.columns = [dataset.name + '.' + k for k in keys]
                self._resolve_data(dataset_item, k)
            else:
                k.append(dataset)
        elif isinstance(dataset, pd.DataFrame):
            for name in dataset.columns:
                self._resolve_data(dataset[name], k)

    def _set_index_level_names(self):
        if isinstance(self.data.index, pd.core.indexes.multi.MultiIndex):
            self.xid_label = self.data.index.names[0]
            self.x_label = self.xid_label.split('_id')[0]
        else:
            self.xid_label = None
            self.x_label = None
    
    # Correspondence Between Simulations
    
    def bin_data(self, n_bins: int = 10, param_label: str = 'rid', min_lim: Optional[float] = None, max_lim: Optional[float] = None, 
                 show_fig: bool = False):
        """
        Bin values of column `param_label` in `n_bins` intervals, group data according to the binning and 
        calculate mean data values of each group.

        In order to establish a correspondence between the values of the data from different simulations, 
        an independent variable `param_label` is selected and used to assign indexes. `param_label` values are divided into 
        `n_bins` ranges, assigning index to each interval, and then for each simulation the averages of the data values 
        is calculated in each bin.
        'addData' and 'data' attributes of the new CitrosData object have two levels of indexes, 
        with id values from binning as the first level and 'sid' as the second one.

        Parameters
        ----------
        n_bins : int, default 10
            Number of bins.
        param_label : str, default 'rid'
            Label of column on the basis of which the indices will be calculated.
        min_lim : float
            The minimum value of the range for binning, `min_lim` < `max_lim`.
            If None then the minimum value of the entire range is selected.
        max_lim : float
            The maximum value of the range for binning, `min_lim` < `max_lim`.
            If None then the maximum value of the entire range is selected.
        show_fig : bool, default False
            If the histogram that represents the distribution of the values in `param_label` should be shown.
        
        Returns
        -------
        out : CitrosData
            New CitrosData object with two levels of indexes in 'addData' and 'data' attributes.

        Examples
        --------
        Query some data from the topic 'A'

        >>> df = citros.topic('A').data(['data.x.x_1', 'data.time'])
        >>> print(df)

        Construct CitrosData object with one data-column 'data.x.x_1':

        >>> dataset = analysis.CitrosData(df, data_label=['data.x.x_1'], units = 'm')

        Divide 'data.time' values in 50 bins and assign indexes to these intervals. For each simulation group 
        'data.x.x_1' values according to the binning and calculate mean of the each group:

        >>> db = dataset.bin_data(n_bins = 50, param_label = 'data.time')

        The result is a CitrosData object with two levels of indexes:

        >>> print(db.data)
                            data.x.x_1
        data.time_id  sid            
        0             1     0.00000
                      2     -0.04460
                      3     -0.07900
        1             1     0.01600
        ...

        >>> print(db.addData)
                            data.time
        data.time_id  sid           
        0             1     8.458
                      2     8.458
                      3     8.458
        1             1     24.774
        ...
        """

        new_indexes, bins_dict, bins, flag_x = self._get_index(n_bins, param_label, min_lim = min_lim, max_lim = max_lim, show_fig = show_fig)
        new_db = self._group_data(new_indexes, bins_dict, flag_x)
        return new_db
    
    def _get_index(self, n_bins, param_label, min_lim = None, max_lim = None, show_fig = False):
        """
        Bin values of column `param_label` in `n_bins` intervals and find indexes for the values according to these intervals.
        
        The range for binning is specified with the `min_lim` and `max_lim` parameters.

        Parameters
        ----------
        n_bins : int
            Number of bins.
        param_label : str
            Label of the column on the basis of which the indices will be calculated.
        min_lim : float
            The minimum value of the range for binning, `min_lim` < `max_lim`.
            If None then the minimum value of the entire range is selected.
        max_lim : float
            The maximum value of the range for binning, `min_lim` < `max_lim`.
            If None then the maximum value of the entire range is selected.
        show_fig : bool, default False
            If the histogram that represents the distribution of the values in `param_label` should be shown.

        Returns
        -------
        new_indexes : pandas.Series
            Index of the bin for each value in `param_label`. 
            The indexes of this Series itself are corresponding to levels of the indexes of the `df`.
            The label of the column is `param_label`_id.
        bins_dict : dict
            Indexes of the bins and corresponding to them values of the bins centers.
        bins : numpy.ndarray
            Edges of the bins.
        """
        if self.inf_vals is not None and self.inf_vals not in ['None', 'none']:
            flag_x = self.addData[param_label].notna() & ((self.addData[param_label].abs() - self.inf_vals) < 0)
        else:
            flag_x = self.addData[param_label].notna()
        db = self.addData[flag_x].copy()
        try :
            h_list = list(set(db[param_label]))
        except KeyError:
            print('There is no column labeled "'+param_label+'"')
            return (None,)*3
        if min_lim is None:
            min_lim = min(h_list)
        if max_lim is None:
            max_lim = max(h_list)
        bins = np.linspace(min_lim, max_lim, n_bins+1)
        bin_centers = bins[:-1]+np.diff(bins)/2
        h_id = [i for i in range(n_bins)]
        bins_dict = dict(zip(h_id, bin_centers))
        new_indexes = pd.cut(db[param_label], bins, labels = h_id, include_lowest = True)
        new_indexes.name = param_label+'_id'
        if show_fig:
            if n_bins > 100:
                edge_color = None
            else:
                edge_color = "k"
            fig, ax = plt.subplots(ncols = 1, nrows = 1, figsize = (6,6))
            counts = new_indexes.value_counts().sort_index().to_list()
            ax.bar(bins[:-1],counts,width=np.diff(bins),align = 'edge', edgecolor = edge_color)
            ax2 = ax.twiny()
            ax2.set_xlim(ax.get_xlim())
            n = 4
            h_id = [i for i in range(n_bins)]
            if len(h_id) <= 2*n:
                new_ticks_indexes = h_id
            else:
                new_ticks_indexes = [(len(h_id)-1)//n*i for i in range(0, n+1)]
                if (len(h_id)-1) not in new_ticks_indexes:
                    new_ticks_indexes = new_ticks_indexes[:-1] + [len(h_id)-1,]
            ax2.set_xticks(bin_centers[new_ticks_indexes], labels = np.array(h_id)[new_ticks_indexes])
            ax2.set_xlabel(param_label+'_id')
            fig.supxlabel(param_label)
            fig.supylabel('counts')
            fig.tight_layout()
            fig.show()

        return (new_indexes, bins_dict, bins, flag_x)
    
    def _group_data(self, new_indexes, bins_dict, flag_x):
        """
        Group data according to id values in `new_indexes` and calculate mean values of the each group.

        'addData' and 'data' attributes of the new CitrosData object have two levels of indexes, 
        with id values from `new_indexes` as the first level and 'sid' as the second one.

        Parameters
        ----------
        new_indexes : pandas.Series
            New indexes, obtained by _get_index(...) function. The indexes of this Series itself must match
            the indexes of the `dataset`.
        bins_dict : dict
            The dict with indexes and corresponding to them values.
            The column with corresponding values are added to addData attribute of the returning CitrosData object.
            For example, if the `new_indexes` label is 'time_id', then the label of the added column is 'time'.

        Returns
        -------
        out : CitrosData
            New CitrosData object with two levels of indexes in 'addData' and 'data' attributes.      
        """
        new_id = new_indexes.name
        new_label = new_id.split('_id')[0]
        bin_mean = new_indexes.apply(lambda x: bins_dict.get(x)).to_list()
        data_copy = self.data[flag_x].copy()
        data_copy[new_id] = new_indexes.to_list()
        data_copy[self.sid_label] = self.addData[flag_x][self.sid_label]
        flag = pd.concat([self.filter[flag_x], pd.DataFrame({new_id: [True for i in range(len(data_copy))], 
                                                             self.sid_label: [True for i in range(len(data_copy))]}, index = data_copy.index)], axis = 1)
        new_data = data_copy[flag].groupby([new_id, self.sid_label]).mean()

        addData_copy = self.addData[flag_x].copy()
        addData_copy[new_id] = new_indexes.to_list()
        addData_copy[new_label] = bin_mean
        new_addData = pd.DataFrame(addData_copy.groupby([new_id, self.sid_label])[new_label].first())
        new_db = CitrosData((new_data,new_addData), type_name = self.type, units = self.units, data_label = self.data_label,
                        parameters = self.parameters, sid_label = self.sid_label, omit_nan_rows=self.omit_nan_rows, 
                        inf_vals = self.inf_vals)
        return new_db

    def scale_data(self, n_points: int = 10, param_label: str = 'rid', show_fig: bool = False, intr_kind: str = 'linear'):
        """
        Scale parameter `param_label` for each of the 'sid' and interpolate data on the new scale.

        In order to establish a correspondence between the values of the data from different simulations, 
        an independent variable `param_label` is selected and used to assign indexes. 
        First the `param_label` interval is shifted and scaled in the way that the minimum value equals 0 and the maximum is 1.
        Then the data is interpolated to a new scale, that consists of `n_points` evenly spaced points and spans from 0 to 1.
        For each 'sid' this procedure is performed separately.
        'addData' and 'data' attributes of the new CitrosData object have two levels of indexes, 
        with id values from scaling as the first level and 'sid' as the second one.

        Parameters
        ----------
        n_points : int, default 10
            Number of points in a new scale, which will be used for interpolation.
        param_label : str, default 'rid'
            Label of the parameter to scale
        show_fig : bool, default False
            If the figures with the results of interpolation should be shown.
            If the 'sid' exceed 5, only first 5 will be shown.
            If data consists of several vectors, for each of them the separate figure will be plotted.
        intr_kind : str, default 'linear'
            Type of the interpolation, see scipy.interpolate.interp1d.

        Returns
        -------
        out : CitrosData
            CitrosData object with multi-level indexing: the first level stores ids of the points of the new scale, the second one - 'sid'.
            Values of the new scale are stored in 'addData' attribute.

        Examples
        --------
        Query some data from the topic 'A'

        >>> df = citros.topic('A').data(['data.x.x_1', 'data.time'])
        >>> print(df)

        Construct CitrosData object with one data-column 'data.x.x_1':

        >>> dataset = analysis.CitrosData(df, data_label=['data.x.x_1'], units = 'm')

        Scale 'data.time' to [0, 1] interval, define a new range of 50 points uniformly distributed from 0 to 1, 
        and interpolate data points over this new interval:

        >>> db = dataset.scale_data(n_points = 50, param_label = 'data.time')

        The result is a CitrosData object with two levels of indexes:

        >>> print(db.data)
                            data.x.x_1
        data.time_id  sid            
        0             1      0.000000
                      2     -0.057000
                      3     -0.080000
        1             1      0.025494
        ...

        >>> print(db.addData)
                            data.time
        data.time_id  sid           
        0             1     0.000000
                      2     0.000000
                      3     0.000000
        1             1     0.020408
        ...
        """
        if self.inf_vals is not None and self.inf_vals not in ['None', 'none']:
            flag_x = self.addData[param_label].notna() & ((self.addData[param_label].abs() - self.inf_vals) < 0)
        else:
            flag_x = self.addData[param_label].notna()
        list_sim_run = list(set(self.addData[flag_x][self.sid_label]))
        param_scaled = self.addData[flag_x].groupby(self.sid_label)[param_label].transform(lambda x: (x-x.min())/(x.max()-x.min()))
        new_scale = np.linspace(0, 1, n_points)
        data_col = []
        for col in self.data.columns:
            data_copy = self.data[flag_x][col]
            filtr = self.filter[flag_x][col]
            list_sim_run = list(set(self.addData[flag_x][filtr][self.sid_label]))
            f_col = []
            for s in list_sim_run:
                filtr_s = self.addData[flag_x][filtr][self.sid_label] == s
                f_col.append(interp1d(param_scaled[filtr][filtr_s], data_copy[filtr][filtr_s], kind = intr_kind, fill_value=np.nan, bounds_error = False))
            data_col.append(pd.concat([pd.DataFrame(f_col[i](new_scale)) for i in range(len(list_sim_run))], axis =0))
        data = pd.concat([pd.DataFrame(data_col[i]) for i in range(len(self.data.columns))], axis = 1)
        data.index.name = param_label + '_id'
        addData = pd.DataFrame({self.sid_label : [item for sublist in [[i]*n_points for i in list_sim_run] for item in sublist],\
            param_label: new_scale.tolist()*len(list_sim_run)}, index = data.index)
        data.set_index([data.index, addData[self.sid_label]], inplace=True)
        data.columns = self.data.columns.copy()
        addData.set_index([addData.index, self.sid_label], inplace=True)
        new_db = CitrosData((data.sort_index(),addData.sort_index()), type_name = self.type, units = self.units, data_label = self.data_label,\
                        parameters = self.parameters, sid_label = self.sid_label, omit_nan_rows=self.omit_nan_rows, inf_vals = self.inf_vals)
        if show_fig:
            for i in range(self.data_dim):
                color_list = cycle(['tab:red','tab:orange','tab:olive','tab:green','tab:cyan','tab:blue', 'tab:purple',\
                    'tab:pink', 'tap: gray'])
                N = min(len(list_sim_run), 5)
                fig, ax = plt.subplots(nrows = N, ncols = 1, figsize=(6, 6))
                if not isinstance(ax, np.ndarray):
                    ax = np.array([ax])
                for j in range(N):
                    filtr = (self.addData[flag_x][self.sid_label] == list_sim_run[j])
                    ax[j].plot(param_scaled[filtr],self.data[self.filter][flag_x][filtr].iloc[:,i], '.', color = next(color_list))
                    ax[j].plot(new_db.addData[new_db.data.iloc[:,i].notna()][param_label].xs(list_sim_run[j], level = self.sid_label),\
                        new_db.data[new_db.data.iloc[:,i].notna()].iloc[:,i].xs(list_sim_run[j], level = self.sid_label), 'k-')
                    ax[j].set_title(self.sid_label + ' = '+str(list_sim_run[j]))
                    ax[j].grid(True)
                    ax[j].set_xlim([-0.05, 1.05])

                fig.supxlabel(new_db.x_label)
                fig.supylabel(new_db.data.columns[i]+', [' + self.units+']')
                fig.suptitle(new_db.type)
                fig.tight_layout()
                fig.show()
        return new_db

    # Statistics
    
    def get_statistics(self, return_format: str = 'pandas'):
        """
        Return table with statistics for CitrosData object.

        Parameters
        ----------
        return_format : {'pandas', 'citrosStat'}, default 'pandas'
            Returning format. 

        Returns
        -------
        Statistics : pandas.DataFrame or citros_data_analysis.error_analysis.citros_stat.CitrosStat
            Collected statistics.
            If `return_format` is 'pandas', then returns pandas.DataFrame with the following columns:
            - (1) the independent variable column, its label matches `x_label` attribute; 
            - (2) column with mean values;
            - (3) column with the covariance matrixes; 
            - (4) column with the square roots of the diagonal elements of the covariance matrix: ( sqrt(s1), sqrt(s2), sqrt(s3) ), 
            where s1,s2,s3 - diagonal of the covariance matrix. 
            
            If `return_format` is 'citrosStat', then returns CitrosStat object with 'x', 'mean', 'covar_matrix' and 'sigma' attributes,
            that corresponds to (1)-(4) items, but in the form of pandas.DataFrames.
        
        See Also
        --------
        CitrosData.bin_data, CitrosData.scale_data, CitrosData.show_statistics

        Examples
        --------
        Import 'data_access' and 'error_analysis' modules and create CitrosDB object to query data:
        
        >>> from citros_data_analysis import data_access as da
        >>> from citros_data_analysis import error_analysis as analysis
        >>> citros = da.CitrosDB()

        Let's consider a data of the topic 'A', json-data part of which has the following structure:

        ```python
        data
        {'x': {'x_1': -0.08, 'x_2': -0.002, 'x_3': 17.7}, 'time': 0.3}
        {'x': {'x_1': 0.0, 'x_2': 0.08, 'x_3': 154.47}, 'time': 10.0}
        ...
        ```

        Let's query data and pass it to CitrosData object to perform analysis.
        It is possible to query all columns separately:

        >>> df = citros.topic('A').data(['data.x.x_1', 'data.x.x_2', 'data.x.x_3', 'data.time'])
        >>> print(df)
           sid   rid   time       topic   type   data.x.x_1   data.x.x_2   data.x.x_3   data.time
        0  1     0     312751159  A       a      0.000        0.080        154.47       10.0
        1  1     1     407264008  A       a      0.008        0.080        130.97       17.9
        2  1     2     951279608  A       a      0.016        0.078        117.66       20.3
        ...

        and define data labels for the CitrosData object as follows:

        >>> dataset = analysis.CitrosData(df,
        ...                               data_label = ['data.x.x_1', 'data.x.x_2', 'data.x.x_3'],
        ...                               units = 'm')

        or query 'data.x' as a one column:

        >>> df = citros.topic('A').data(['data.x', 'data.time'])
        >>> print(df)
           sid   rid   time       topic   type   data.x                                       data.time
        0  1     0     312751159  A       a      {'x_1': 0.0, 'x_2': 0.08, 'x_3': 154.47}     10.0
        1  1     1     407264008  A       a      {'x_1': 0.008, 'x_2': 0.08, 'x_3': 130.97}   17.9
        2  1     2     951279608  A       a      {'x_1': 0.016, 'x_2': 0.078, 'x_3': 117.66}  20.3
        ...

        and correspondingly set data_label:

        >>> dataset = analysis.CitrosData(df,
        ...                               data_label = 'data.x',
        ...                               units = 'm')

        To analyze data of multiple simulations it is necessary to establish a correspondence between the values of the data 
        from these different simulations. One approach is to select an independent variable, define a scale that is common 
        to all simulations and assign indexes on this scale. Then, the values of variables from different simulations
        will be connected by this independent variable.

        There are two ways to perform index assignment: divide the independent variable into N ranges, 
        assign an index to each interval, and calculate the averages of the data values for each simulation in each range, 
        or scale the independent variable to the interval [0,1], define a new range of N points uniformly distributed from 0 to 1, 
        and interpolate data points over this new interval. The first approach corresponds to the bin_data() method, while the second 
        is implemented by the scale_data() method:

        >>> db = dataset.bin_data(n_bins = 50, param_label = 'data.time')
        >>> #or
        >>> db = dataset.scale_data(n_points = 50, param_label = 'data.time')

        Let's assume that the last variant was chosen. And now get the statistics:

        >>> stat = db.get_statistics(return_format = 'citrosStat')

        It returns CitrosStat object, that stores independent variable values, mean data values, covariance matrix and 
        standard deviation (square root of the covariance matrix diagonal elements) for each index.

        The mean data value, independent variable values and standard deviation are the pandas.DataFrames:

        >>> print(stat.mean)
                       data.x.x_1   data.x.x_2  data.x.x_3
        data.time_id                                    
        0              -0.045667    0.044667    93.706667
        1              -0.026038    0.059598    73.345027
        ...

        >>> print(stat.x)
                       data.time
        data.time_id           
        0              0.000000
        1              0.020408
        ...

        >>> print(stat.sigma)
                        data.x.x_1  data.x.x_2  data.x.x_3
        data.time_id                                    
        0               0.041187    0.042158    69.647524
        1               0.050354    0.026935    84.049381
        2               0.049388    0.010733    40.279784

        and the covariance matrix is a pandas.Series. Each its row contains N x N dimensional numpy.ndarray, where N
        is a data dimension:

        >>> print(stat.covar_matrix.loc[0])
        [[1.69633333e-03 1.54366667e-03 2.60583167e+00]
        [1.54366667e-03 1.77733333e-03 2.93335333e+00]
        [2.60583167e+00 2.93335333e+00 4.85077763e+03]]
        """
        if self.xid_label is None:
            print('error: data must have two levels of indices: the first level corresponds to the independent variable\
                  \n(such as time or height) and the second one is sid.\
                  \nTry bin_data() or scale_data() methods to prepare the data.')
            return None
        statistics = pd.DataFrame()

        mu = self.data[self.filter].groupby(level = self.xid_label).mean().apply(lambda x: np.array(x), axis = 1)
        with warnings.catch_warnings():
            #avoid warnings when calculate covariance for the one value
            warnings.simplefilter("ignore", category=RuntimeWarning)
            covar_matrix = self.data[self.filter].groupby(level = self.xid_label).cov().groupby(level = self.xid_label).apply(lambda x: np.array(x))
        sigma = self.data[self.filter].groupby(level = self.xid_label).std().apply(lambda x: np.array(x), axis = 1)
        x_value = self.addData[self.x_label].groupby(level = self.xid_label).first()
        
        statistics['mean'] = mu
        statistics['covar_matrix'] = covar_matrix
        statistics['sigma'] = sigma

        statistics.insert(loc = 0, column = self.x_label, value = x_value)

        if return_format == 'citrosStat':
            return CitrosStat(statistics, self.data.columns, self.x_label)
        elif return_format == 'pandas':
            return statistics
        else:
            print('error: there is no return_format {return_format}, try "citrosStat" or "pandas"')
        
    def _plot_1Dstatistics(self, statistics, filter_st, ax = None, n_std = 3, num_data = 0, ylabel = None, std_color = 'r', 
                           std_area = False, std_lines = True, line_style_custom = '-'):
        """
        Plot data vs. `x_label` on a single ax for a one-dimensional data.

        Plots data vs. `x_label` for different 'sid', for mean value and shows `n_std`-sigma interval.

        Parameters
        ----------
        statistics : pandas.DataFrame
            DataFrame with columns [`x_label`,'mean','sigma'], see function get_statistic(...).
        filter_st : pandas.Series
            Filter on non-nan values of the statistics.
        ax : matplotlib.axes.Axes
            Matplotlib ax to plot on.
        n_std : int, default 3
            Error interval to display in standard deviations.
        num_data : int
            Order of the column if data consists of several columns.
        ylabel : str
            If None, then label of the column.
        std_color : str, default 'r'
            Color for displaying standard deviations, red by default.
        std_area : bool, default False
            Fill area within `n_std`-standard deviation lines with color.
        std_lines : bool, default True
            If False, remove standard deviation boundary lines.
        line_style_std : str
            Type of the line to plot std boundary.

        Returns
        -------
        out : matplotlib.axes.Axes
        """
        sim_run_id = list(set(self.addData[self.filter.iloc[:, num_data]].index.get_level_values(self.sid_label)))
        N_run = len(sim_run_id)
        color_list =  [tuple(np.random.uniform(0,1, size=3)) for _ in range(N_run)]
        for run_id, c in zip(sim_run_id, color_list):
            ax.plot(self.addData[self.x_label][self.filter.iloc[:, num_data]].xs(run_id, level = self.sid_label), \
                self.data.iloc[:,num_data][self.filter.iloc[:, num_data]].xs(run_id, level = self.sid_label),'-', color = c, linewidth = 1)
            if ylabel is None:
                ylabel = self.data.columns[num_data]
                ylabel += ", ["+self.units+"]" if self.units != '' else ''
            ax.set_ylabel(ylabel)

        ax.plot(statistics[statistics['mean'].notna()][self.x_label], statistics[statistics['mean'].notna()]['mean'], 'k-', linewidth = 2, label = 'mean')
        if n_std is not None:
            if std_lines:
                ax.plot(statistics[self.x_label][filter_st], statistics['mean'][filter_st] + n_std*statistics['sigma'][filter_st],
                        line_style_custom, color = std_color, label = r'$\pm$'+str(n_std)+ r'$\sigma$',markersize = 0.7)
                ax.plot(statistics[self.x_label][filter_st], statistics['mean'][filter_st] - n_std*statistics['sigma'][filter_st], 
                        line_style_custom, color = std_color, markersize = 0.7)
                label = None
            else:
                label = r'$\pm$'+str(n_std)+ r'$\sigma$'
            if std_area:
                ax.fill_between(statistics[self.x_label][filter_st].values, (statistics['mean'][filter_st] - n_std*statistics['sigma'][filter_st]).values,
                                (statistics['mean'][filter_st] + n_std*statistics['sigma'][filter_st]).values, color = std_color, label = label,
                                alpha = 0.12)

        ax.grid(True)
        return ax

    def _plot_statistics(self, statistics, fig = None, fig_title = None, show_fig = True, return_fig = False, n_std = 3, 
                         std_color = 'r', connect_nan_std = True, std_area = False, std_lines = True):
        """
        Plot data vs. `x_label` figure for a N multidimensional data on N axis.

        Parameters
        ----------
        Statistics : pandas.DataFrame
            DataFrame with columns [`x_label`,'mean','sigma'], see function get_statistic(...).
        fig : matplotlib.figure.Figure, optional
            figure to plot on. If None, then the new one is created.
        fig_title : str
            Title of the figure.
        show_fig : bool, default True
            If the figure should be shown, True by default.
        return_fig : bool, default False
            If True, return fig and list of ax.
        n_std : int, default 3
            Error interval to display in standard deviations.
        std_color : str, default 'r'
            Color for displaying standard deviations, red by default.
        connect_nan_std : bool, default True
            If True, all non-NaN values in standard deviation boundary line are connected, resulting in a continuous line. 
            Otherwise, breaks are introduced in the standard deviation line whenever NaN values are encountered.
        std_area : bool, default False
            Fill area within `n_std`-standard deviation lines with color.
        std_lines : bool, default True
            If False, remove standard deviation boundary lines.

        Returns
        -------
        fig : matplotlib.figure.Figure
            if `return_fig` set to True
        ax : list of matplotlib.axes.Axes
            if `return_fig` set to True
        """
        if (not show_fig) and (not return_fig):
            return
 
        if isinstance(statistics, CitrosStat):
            statistics = statistics.to_pandas()

        # if not isinstance(statistics['mean'].iloc[0], np.ndarray):
        #     N = 1
        # else:
        N = len(statistics['mean'].iloc[0])
        if fig is None:
            fig, ax = plt.subplots(nrows = N, ncols = 1,figsize=(6, 6))
            if N == 1:
                ax = np.array([ax])
        else:
            ax = []
            for i in range(1,N+1):
                ax.append(fig.add_subplot(N,1,i))
            ax = np.array(ax)

        # else:
        for n in range(N):
            res_mean = statistics['mean'].apply(lambda x: x[n])
            res_sigm = statistics['sigma'].apply(lambda x: x[n])
            if connect_nan_std:
                filter_st = res_sigm.notna()
                line_style_custom = '-'
            else:
                filter_st = pd.Series([True]*len(res_sigm), index = res_sigm.index)
                if res_sigm.notna().all():
                    line_style_custom = '-'
                else:
                    line_style_custom = '.-'
            self._plot_1Dstatistics(pd.concat([statistics[self.x_label],res_mean,res_sigm], axis =1),\
                filter_st, ax = ax[n], n_std = n_std, num_data = n, std_color = std_color, 
                std_area = std_area, std_lines = std_lines, line_style_custom = line_style_custom)
        handles, labels = ax[-1].get_legend_handles_labels()

        fig.supxlabel(self.x_label)
        if fig_title is None:
            fig.suptitle('Statistics')
        else:
            fig.suptitle(fig_title)
        fig.legend(handles, labels, bbox_to_anchor=(1.0, 0.94),loc ='upper left')
        fig.tight_layout()

        if show_fig:
            fig.show()
        if return_fig:
            return fig, ax
    
    def show_statistics(self, fig: Optional[matplotlib.figure.Figure] = None, show_fig: bool = True, return_fig: bool = False, 
                        n_std: int = 3, fig_title: str = 'Statistics', std_color: str = 'r', connect_nan_std: bool = True, 
                        std_area: bool = False, std_lines: bool = True):
        """
        Collect statistics for CitrosData object and plot it.

        Parameters
        ----------
        fig : matplotlib.figure.Figure
            figure to plot on. If None, the new one will be created.
        show_fig : bool
            If the figure should be shown, True by default.
        return_fig : bool
            If the figure parameters fig, ax should be returned; 
            fig is matplotlib.figure.Figure and ax is matplotlib.axes.Axes
        n_std : int, default 3
            Error interval to display in standard deviations.
        fig_title : str, default 'Statistics'
            Title of the figure.
        std_color : str, default 'r'
            Color for displaying standard deviations, red by default.
        connect_nan_std : bool, default True
            If True, all non-NaN values in standard deviation boundary line are connected, resulting in a continuous line. 
            Otherwise, breaks are introduced in the standard deviation line whenever NaN values are encountered.
        std_area : bool, default False
            Fill area within `n_std`-standard deviation lines with color.
        std_lines : bool, default True
            If False, remove standard deviation boundary lines.

        Returns
        -------
        fig : matplotlib.figure.Figure
            if `return_fig` set to True
        ax : numpy.ndarray of matplotlib.axes.Axes
            if `return_fig` set to True

        See Also
        --------
        CitrosData.get_statistics(), CitrosData.bin_data(), CitrosData.scale_data()

        Examples
        --------
        Import 'data_access' and 'error_analysis' modules and create CitrosDB object to query data:
        
        >>> from citros_data_analysis import data_access as da
        >>> from citros_data_analysis import error_analysis as analysis
        >>> citros = da.CitrosDB()
        
        Download json-data column 'data.x', that contains data.x.x_1, data.x.x_2 and data.x.x_3 and column 'data.time':

        >>> df = citros.topic('A').data(['data.x', 'data.time'])

        Construct CitrosData object with 3 data-columns from 'data.x':

        >>> dataset = analysis.CitrosData(df, data_label=['data.x'], units = 'm')

        Use method scale_data() or bin_data() to get correspondence between different simulation:

        >>> db_sc = dataset.scale_data(n_points = 150, 
                                       param_label = 'data.time', 
                                       show_fig = False)
        
        Show statistics plot:

        >>> db_sc.show_statistics()
        """
        if self.xid_label is None:
            print('error: data must have two levels of indices: the first level corresponds to the independent variable\
                  \n(such as time or height) and the second one is sid.\
                  \nTry bin_data() or scale_data() methods to prepare the data.')
            return None
        statistics = self.get_statistics(return_format = 'pandas')
        return self._plot_statistics(statistics, fig = fig, fig_title = fig_title, show_fig = show_fig, return_fig = return_fig, 
                                     n_std = n_std, std_color = std_color, connect_nan_std = connect_nan_std, std_area = std_area, 
                                     std_lines = std_lines)

    # Correlation
    
    def show_correlation(self, db2: Optional[pd.DataFrame] = None, x_col: int = 0, y_col: int = 0, 
                         slice_id: Optional[int] = None, slice_val: Optional[float] = None, n_std: int = 3,
                         bounding_error: bool = False, fig: Optional[matplotlib.figure.Figure] = None, return_fig: bool = False, 
                         display_id: bool = True, return_ellipse_param: bool = False, **kwargs):
        """
        Show data correlation for the given `slice_id`. 

        Prepare data from one or more CitrosData objects and plot confidence ellipses for the specified id = `slice_id`.
        If the data stored in CitrosData object `db` is multidimensional, then `x_colNumber` and `y_colNumber` must be provided.
        If the data from another CitrosData objects is used, the latter must be provided in `db2`. Then the data from `db` 
        is supposed to be plotted along x-axis and the data from `db2` is supposed to be plotted along y-axis.

        Parameters
        ----------
        db2 : CitrosData
            Additional CitrosData object.

        x_col : int >=0 or str, optional
            - If `int` - index of column to plot along x axis, >=0.
            - If `str` - label of the column to plot along y axis
            - If data is multidimensional, must be specified, otherwise data is supposed to be 1-dimensional.

        y_col : int >=0  or str, optional
            - If `int` - index of column to plot along y axis, >=0.
            - If `str` - label of the column to plot along y axis
            - If data is multidimensional, must be specified, otherwise data is supposed to be 1-dimensional.

        slice_id : int
            id of the slice.
        slice_val : float
            Value, for which the nearest slice_id is search.
            Used only if slice_id is None.
        n_std : list or int, default 3
            Radius or list of radii of the confidence ellipses in sigmas, 3 by default.
        bounding_error : bool, default False
            If the bounding error should be depicted.
        fig : matplotlib.figure.Figure, optional
            figure to plot on. If None, then the new one is created.
        return_fig : bool, default False.
            If the fig, ax should be returned.
        display_id : bool, default True
            Whether to print the pair of `slice_id` `slice_val` or not.
        return_ellipse_param : bool, default False
            If True, returns ellipse parameters.

        Other Parameters
        ----------------
        kwargs : dict, optional
            see matplotlib.patches.Ellipse.

        Returns
        -------
        fig : matplotlib.figure.Figure
            if `return_fig` set to True
        ax : matplotlib.axes.Axes
            if `return_fig` set to True
        ellipse_param : dict or list of dict
            Ellipse parameters if `return_ellipse_param` set True.
            Parameters of the ellipse:
            - x : float - x coordinate of the center.
            - y : float - y coordinate of the center.
            - width : float - total ellipse width (diameter along the longer axis).
            - height : float - total ellipse height (diameter along the shorter axis).
            - alpha : float - angle of rotation, in degrees anti-clockwise from the minor axis.

            If bounding_error set True:
            - bounding_error : float - radius of the error circle.

        Examples
        --------
        Import 'data_access' and 'error_analysis' modules and create CitrosDB object to query data:
        
        >>> from citros_data_analysis import data_access as da
        >>> from citros_data_analysis import error_analysis as analysis
        >>> citros = da.CitrosDB()

        For topic 'B' query json-data column 'data.x.x_1', 'data.x.x_2' and 'data.time':

        >>> df = citros.topic('B').data(['data.x.x_1', 'data.x.x_2', 'data.time'])

        Construct CitrosData object with 2 data-columns 'data.x.x_1', 'data.x.x_2':
        
        >>> dataset = analysis.CitrosData(df, data_label=['data.x.x_1', 'data.x.x_2'], units = 'm')

        Use method scale_data() or bin_data() to get correspondence between different simulation
        and assign indexes to 'data.time' axis:

        >>> db_sc = dataset.scale_data(n_points = 20, 
        ...                            param_label = 'data.time', 
        ...                            show_fig = False)

        Plot correlation plot for the index = 5:

        >>> db_sc.show_correlation(x_col = 'data.x.x_2',
        ...                        y_col = 'data.x.x_1',
        ...                        slice_id = 5,
        ...                        n_std = [1,2,3],
        ...                        bounding_error= False)
        slice_id = 5,
        slice_val = 0.2632
        """
        if self.xid_label is None:
            print('error: data must have two levels of indices: the first level corresponds to the independent variable\
                  \n(such as time or height) and the second one is sid.\
                  \nTry bin_data() or scale_data() methods to prepare the data.')
            return None
        if isinstance(x_col, str):
            if x_col not in self.data.columns:
                print(f"Column '{x_col}' does not exist")
                return None
        elif isinstance(x_col, int):
            if x_col > (len(self.data.columns)-1):
                print(f"'x_col' must be <= {len(self.data.columns)-1}")
                return None
        else:
            print(f"'x_col' must be str or int")
            return None
        
        if db2 is None:
            if isinstance(y_col, str):
                if y_col not in self.data.columns:
                    print(f"Column '{y_col} does not exist'")
                    return None
            elif isinstance(x_col, int):
                if y_col > (len(self.data.columns)-1):
                    print(f"'y_col' must be <= {len(self.data.columns)-1}")
                    return None
            else:
                print(f"'y_col' must be str or int")
                return None
        
        else:
            if isinstance(y_col, str):
                if y_col not in db2.data.columns:
                    print(f"Column '{y_col} does not exist'")
                    return None
            elif isinstance(x_col, int):
                if y_col > (len(db2.data.columns)-1):
                    print(f"'y_col' must be <= {len(db2.data.columns)-1}")
                    return None
            else:
                print(f"'y_col' must be str or int")
                return None

        if slice_id is None:
            if slice_val is not None:
                if db2 is None:
                    slice_id = self._get_id_by_val(slice_val, (x_col, y_col))
                else:
                    slice_id = self._get_id_by_val(slice_val, (x_col,))
            else:
                print('either `slice_id` or `slice_val` must be specified')
                return
        if db2 is None:
            try:
                x_units = self.units
                y_units = self.units
            except:
                x_units = ''
                y_units = ''
            
            try :
                if isinstance(x_col, str):
                    x = self.data[x_col].xs(slice_id, level = self.xid_label)
                    x_filter = self.filter.loc[:, x_col].xs(slice_id, level = self.xid_label)
                elif isinstance(x_col, int):
                    x = self.data.iloc[:,x_col].xs(slice_id, level = self.xid_label)
                    x_filter = self.filter.iloc[:, x_col].xs(slice_id, level = self.xid_label)
                if isinstance(y_col, str):
                    y = self.data[y_col].xs(slice_id, level = self.xid_label)
                    y_filter = self.filter.loc[:, y_col].xs(slice_id, level = self.xid_label)
                elif isinstance(y_col, int):
                    y = self.data.iloc[:,y_col].xs(slice_id, level = self.xid_label)
                    y_filter = self.filter.iloc[:, y_col].xs(slice_id, level = self.xid_label)
            except KeyError:
                print('slice_id must be <= n_bins/points')
                return
            except IndexError:
                print('data in `db` has only {0} column{1}'.format(self.data.shape[1], np.where(self.data.shape[1] == 1,'','s')))
                return

        else:
            try:
                x_units = self.units
            except:
                x_units = ''

            try:
                if isinstance(x_col, str):
                    x = self.data[x_col].xs(slice_id, level = self.xid_label)
                    x_filter = self.filter.loc[:, x_col].xs(slice_id, level = self.xid_label)
                elif isinstance(x_col, int):
                    x = self.data.iloc[:,x_col].xs(slice_id, level = self.xid_label)
                    x_filter = self.filter.iloc[:, x_col].xs(slice_id, level = self.xid_label)
            except KeyError:
                print('slice_id must be <= n_bins/points')
                return
            except IndexError:
                print('data in `db` has only {0} column{1}'.format(self.data.shape[1], np.where(self.data.shape[1] == 1,'','s')))
                return
            try:
                y_units = db2.units
            except:
                y_units = ''

            try:
                if slice_val is not None:
                    slice_id_2 = db2._get_id_by_val(slice_val, (y_col,))
                else:
                    slice_id_2 = slice_id
                if isinstance(y_col, str):
                    y = db2.data[y_col].xs(slice_id_2, level = self.xid_label)
                    y_filter = db2.filter.loc[:, y_col].xs(slice_id_2, level = self.xid_label)
                elif isinstance(y_col, int):
                    y = db2.data[db2.filter.iloc[:, y_col]].iloc[:,y_col].xs(slice_id_2, level = self.xid_label)
                    y_filter = db2.filter.iloc[:, y_col].xs(slice_id_2, level = self.xid_label)
            except KeyError:
                print('slice_id must be <= n_bins/points')
                return
            except IndexError:
                print('data in `db2` has only {0} column{1}'.format(db2.data.shape[1], np.where(db2.data.shape[1] == 1,'','s')))
                return

        result = pd.concat([x,y], axis = 1)
        result_filter = pd.concat([x_filter,y_filter], axis = 1)
        units_name = [np.where(units != '', ', [' + units + ']', '') for units in [x_units, y_units]]
        column_names = []
        if isinstance(x_col, str):
            column_names += [x_col + units_name[0].tolist()]
        elif isinstance(x_col, int):
            column_names += [np.where(self.data.shape[1] != 1, 'col_' + str(x_col), '').tolist() + units_name[0].tolist()]
        if isinstance(y_col, str):
            column_names += [y_col + units_name[1].tolist()]
        if isinstance(y_col, int):
            column_names += [np.where((db2 if db2 is not None else self).data.shape[1] != 1, 'col_' + str(y_col), '').tolist() + units_name[1].tolist()]
        flag = result_filter.all(axis = 1)
        if True in flag.value_counts().index:
            plot_points = True
            if flag.value_counts()[True] > 1:
                # it is possible to plot std ellipses
                plot_ellipse = True
            else:
                plot_ellipse = False
                bounding_error = False
        else:
            plot_points = False
            plot_ellipse = False

        slice_val = self._get_val_by_id(slice_id)
        if db2 is None:
            if display_id:
                print('slice_id = {0},\nslice_val = {1}'.format(slice_id, slice_val))
            title_slice_id = str(slice_id)
        else:
            slice_val_2 = db2._get_val_by_id(slice_id_2)
            if display_id:
                print('slice_id = {0},\nslice_val = {1},\nslice_id_2 = {2},\nslice_val_2 = {3}'.format(slice_id, slice_val, slice_id_2, slice_val_2))
            if slice_id == slice_id_2:
                title_slice_id = str(slice_id)
            else:
                title_slice_id = str([slice_id, slice_id_2])
        return self._plot_correlation(result.iloc[:,0][flag],result.iloc[:,1][flag], axis_labels = column_names,\
            title = 'correlation, ' + self.xid_label + ' = '+ title_slice_id, n_std = n_std, bounding_error = bounding_error,\
            return_fig = return_fig, fig = fig, plot_points = plot_points, plot_ellipse = plot_ellipse,\
            return_ellipse_param = return_ellipse_param, **kwargs)

    def _get_id_by_val(self, val, cols):
        """
        Return the nearest slice_id for the given `val` where corresponding value of the column `col` is not nan.
        """
        flag = True
        for col in cols:
            if isinstance(col, str):
                flag = self.filter.loc[:, col] & flag
            elif isinstance(col, int):
                flag = self.filter.iloc[:, col] & flag
        return (self.addData[flag][self.x_label] - val).abs().idxmin()[0]
    
    def _get_val_by_id(self, slice_id):
        """
        Return value for the given `slice_id`.
        """
        return self.addData.xs(slice_id, level = self.xid_label)[self.x_label].iloc[0]
    
    def _plot_correlation(self, x: ArrayLike, y: ArrayLike, n_std: Union[int, list] = 3, axis_labels: Optional[str] = None, 
                          title: str = 'correlation', bounding_error: bool = True, return_fig: bool = False, 
                          fig: Optional[matplotlib.figure.Figure] = None, plot_points: bool = True, plot_ellipse: bool = True, 
                          return_ellipse_param: bool = False, **kwargs):
        """
        Plot and show figure with one or several confidence ellipses (`x`,`y`).

        Parameters
        ----------
        x : array-like
            Shape (n, ).
        y : array-like
            Shape (n, ).
        n_std : list or int, default 3
            Radius or list of radii of confidence ellipse in sigmas, 3 by default.
        axis_labels : list of str
            List of x and y axis labels.
        title : str
            Title of the figure.
        bounding_error : bool, default True
            If the bounding error should be depicted.
        return_fig : bool
            If the fig and ax should be returned.
        fig : matplotlib.figure.Figure, optional
            figure to plot on. If None, then the new one is created.
        plot_points : bool, default True
            If True then plot points on the image.
        plot_ellipse : bool, default True
            If True then plot ellipse on the image.
        return_ellipse_param : bool, default False
            If True, returns ellipse parameters.

        kwargs : dict, optional
            see matplotlib.patches.Ellipse.

        Returns
        -------
        fig : matplotlib.figure.Figure
            if `return_fig` set to True
        ax : matplotlib.axes.Axes
            if `return_fig` set to True
        ellipse_param : dict or list of dict
            Ellipse parameters if `return_ellipse_param` set True.
            Parameters of the ellipse:
            - x : float
                x coordinate of the center.
            - y : float
                y coordinate of the center.
            - width : float
                Ellipse width (along the longer axis).
            - height : float
                Ellipse height (along the shorter axis).
            - alpha : float
                Angle of rotation, in degrees, anti-clockwise from the shorter axis.
              If bounding_error set True:
            - bounding_error : float
                Radius of the error circle.
        """
        if axis_labels is None:
            axis_labels=['col1','col2']
        if fig is None:
            fig, ax = plt.subplots(figsize=(6, 6))
        else:
            ax = fig.add_subplot(1,1,1)
        if type(n_std) != list:
            n_std = [n_std,]
        color_list = cycle(['tab:red','tab:orange','tab:olive','tab:green','tab:cyan','tab:blue'])
        if return_ellipse_param:
            ellipse_param = []
        if plot_points:
            ax.plot(x,y,'k.')
            ellipse_par_list = []
            if plot_ellipse:
                try: 
                    for n in n_std:
                        _, ellipse_par = self._plot_ellipse(x, y, n, ax, edgecolor=next(color_list), **kwargs)
                        ellipse_par_list.append(ellipse_par)
                        if return_ellipse_param:
                            ellipse_param.append({'x': ellipse_par[3], 'y': ellipse_par[4], 
                                                'width': 2*ellipse_par[0], 'height': 2*ellipse_par[1],
                                                'alpha': np.degrees(ellipse_par[2])})
                    if bounding_error:
                        R_bound_err = []
                        y_text = 0
                        for i, ellipse_par in enumerate(ellipse_par_list):
                            R = self._plot_bounding_error(*ellipse_par, ax)
                            R_bound_err.append(R)
                            ax.text(R, y_text, str(np.round(R, decimals = 2)), fontsize = 8)
                            y_text = y_text - R/20
                            if return_ellipse_param:
                                ellipse_param[i]['bounding_error'] = R
                        ax.plot(0,0,'k+',mew=10,ms=2, label='origin')
                    ax.plot(ellipse_par[3], ellipse_par[4],'r+',mew=10, ms=2, label='mean')
                except np.linalg.LinAlgError:
                    print('can not calculate eigenvalues and eigenvectors of the covariance matrix to plot confidence ellipses')
            else:
                print('the number of points is not enough to plot confidence ellipses')
        
            ax.set_xlabel(axis_labels[0])
            ax.set_ylabel(axis_labels[1])
            ax.set_title(title)
            x_limits = ax.get_xlim()
            y_limits = ax.get_ylim()
            dxlen = (x_limits[1] - x_limits[0])*0.03
            dylen = (y_limits[1] - y_limits[0])*0.03
            ax.set_xlim([x_limits[0] - dxlen, x_limits[1] + dxlen])
            ax.set_ylim([y_limits[0] - dylen, y_limits[1] + dylen])
            ax.grid()
            if plot_ellipse:
                ax.legend(bbox_to_anchor=(1.1, 0.9),bbox_transform=fig.transFigure)

        else:
            print('there is no data to plot')
        if return_ellipse_param:
            if len(ellipse_param) == 1:
                ellipse_param = ellipse_param[0]
        if return_fig:
            if return_ellipse_param:
                return fig, ax, ellipse_param
            else:
                return fig, ax
        elif return_ellipse_param:
            return ellipse_param
        else:
            return None

    def _plot_ellipse(self, x, y, n_std, ax, facecolor='none', edgecolor='red', **kwargs):
        """
        Calculate and plot on `ax` confidence ellipse for dataset (`x`, `y`).

        Parameters
        ----------
        x : array-like
            Shape (n, ).
        y : array-like
            Shape (n, )
        n_std : int
            Radius of ellipse in sigmas.
        facecolor : color or None
            Ellipse's face color, transparent (facecolor='none') by default.
        edgecolor : color or None
            Ellipse's color of edges, red by default.
        **kwargs
            see matplotlib.patches.Ellipse

        Returns
        -------
        p: matplotlib.patches.Patch
        parameters : tuple
            Parameters of the ellipse:
                width : float
                    semi-length of the longer axis.
                height : float
                    semi-length of the shorter axis.
                alpha : float
                    Angle of rotation, in radians.
                m : float
                    Shift of the center along x axis.
                n : float
                    Shift of the center along y axis.
        """
        X = np.array([x,y]).T
        cov = self._get_covar_matrix(X)
        lambda_, v = np.linalg.eig(cov)
        lambda_ = np.where(abs(lambda_) < 1e-13, 0, lambda_)
        order = lambda_.argsort()[::-1]
        vals = lambda_[order]
        vecs = v[:,order]
        alpha = np.arctan2(vecs[:,0][1],vecs[:,0][0])
        w, h = 2 * n_std * np.sqrt(vals)
        m, n = self._get_mu(X)
        ellipse = Ellipse(xy=(m, n),width=w, height=h,angle=np.degrees(alpha),\
            facecolor=facecolor, edgecolor=edgecolor, label=str(n_std)+ r'$\sigma$', **kwargs)
        parameters = (w/2, h/2, alpha, m, n)
        return ax.add_patch(ellipse), parameters

    def _plot_bounding_error(self, a, b, alpha, m, n, ax):
        """
        Add bounding error circle to a plot.

        In order to find radius of bounding error circle, the absolute value of the first derivative of the function
        D = D(phi) is minimized, where D is the distance from the origin to point on ellipse, phi - the angle of the point,
        measured from the longest ellipse axis in polar reference system associated with an ellipse. 
        Several initial guesses are used to avoid falling in minima or local maxima.

        Parameters
        ---------- 
        a : float
            Length of the longer axis of the ellipse.
        b : float
            Length of the shorter axis of the ellipse.
        alpha : float
            Angle of ellipse rotation, in radians.
        m : float
            Shift of the ellipse center along x axis.
        n : float
            Shift of the ellipse center along y axis.
        ax : matplotlib.axes.Axes
            Axe to plot on.
        
        Returns
        -------
        out : float
            Radius of the bounding error circle.
        """
        init_guess_list = np.linspace(0, 360, 13)
        res_phi_list = []
        for init_guess in init_guess_list:
            res = minimize(self._abs_derivative, np.deg2rad(init_guess), args = (a, b, alpha, m, n), method='TNC')
            res_phi_list.append(res.x[0])    
        R_list = self._dist(np.array(res_phi_list),a,b,alpha,m,n)
        R = max(R_list)
        phi_ = np.arange(0,1.01,0.01)*2*np.pi
        ax.plot(R*np.cos(phi_),R*np.sin(phi_),'k-', linewidth =0.7)
        return R

    def _abs_derivative(self, phi, a, b, alpha, m, n):
        """
        Calculate the absolute value of the first derivative of the the function D = D(phi), 
        where D is the distance from the origin to point on ellipse, `phi` - the angle of the point,
        measured from the longest ellipse axis in polar reference system associated with an ellipse.

        Parameters
        ----------
        phi : float or array-like
            Angle coordinate, in radians.
        a : float
            Length of the longer axis of the ellipse.
        b : float
            Length of the shorter axis of the ellipse.
        alpha : float
            Angle of ellipse rotation, in radians.
        m : float
            Shift of the ellipse center along x axis.
        n : float
            Shift of the ellipse center along y axis.

        Returns
        ------- 
        float or array-like
            Absolute value of the first derivative.
        """
        xl = a*np.cos(phi)
        yl = b*np.sin(phi)
        x = xl*np.cos(alpha) - yl*np.sin(alpha) + m
        y = xl*np.sin(alpha) + yl*np.cos(alpha) + n
        dx = -a*np.sin(phi)*np.cos(alpha) - b*np.cos(phi)*np.sin(alpha)
        dy = -a*np.sin(phi)*np.sin(alpha) + b*np.cos(phi)*np.cos(alpha)
        f = 2*x*dx+2*y*dy
        return np.abs(f)

    def _dist(self, phi,a,b,alpha,m,n):
        """
        Calculate distance between the origin and the point on ellipse with angle `phi`, which is 
        measured from the longest ellipse axis in polar reference system associated with an ellipse.

        Parameters
        ----------
        phi : float
            Angle coordinate, in radians.
        a : float
            Length of the longer axis of the ellipse.
        b : float
            Length of the shorter axis of the ellipse.
        alpha : float
            Angle of the ellipse rotation, in radians.
        m : float
            Shift of the ellipse center along x axis.
        n : float
            Shift of the ellipse center along y axis.

        Returns
        -------
        out : float or array-like
            Value of the distance.
        """
        xl = a*np.cos(phi)
        yl = b*np.sin(phi)
        x = (xl)*np.cos(alpha) - (yl)*np.sin(alpha) + m
        y = (xl)*np.sin(alpha) + (yl)*np.cos(alpha) + n
        r = np.sqrt(x**2 + y**2)
        return r

    # Utilities
    
    def to_pandas(self):
        """
        Concatenate `data` and `addData` attributes and return the result table as a pandas.DataFrame.

        Returns
        -------
        df : pandas.DataFrame
            Concatenated table.
        """
        return pd.concat([self.data, self.addData], axis = 1)

    def set_parameter(self, key: Optional[str] = None, value: Optional[Union[int, float]] = None, item: Optional[dict] = None):
        """
        Set parameter value to a CitrosData object.

        Parameters
        ----------
        key : str
            Label of the parameter.
        value : int or float
            Parameter value.
        item : dict
            Dictionary with parameters.
        """
        if key is not None and value is not None:
            if key in self.parameters.keys():
                print('key "{}" already exists, its value will be set to {}'.format(key, value))
            self.parameters[key] = value
        if item is not None:
            if isinstance(item, dict):
                for k, v in item.items():
                    if k in self.parameters.keys():
                        print('key "{}" already exists, its value will be set to {}'.format(k, v))
                    self.parameters[k] = v
        
    def drop_parameter(self, key: Optional[str] = None):
        """
        Delete parameter labeled `key` and associated value.

        Parameters
        ----------
        key : str
            Label of the parameter to remove.
        """
        if key in self.parameters:
            self.parameters.pop(key)
        else:
            print('key "{}" does not exists'.format(key))

    def add_addData(self, column: ArrayLike, column_label: str):
        """
        Add column to 'addData' attribute.

        Parameters
        ----------
        column : array-like object
            Column to add.
        column_label : str
            Label of the new column in 'addData'.
        """
        self.addData[column_label] = column

    def drop_addData(self, column_label: str):
        """
        Delete column from 'addData' attribute.

        Parameters
        ----------
        column_label : str
            Label of the column to delete .
        """
        self.addData.drop(columns = column_label, inplace = True)
    
    def _set_index_levels(self, index_levels):
        """
        Set indexes to database.

        Parameters
        ----------
        index_levels : list of str
            Labels of columns in 'addData' to assign as indexes.
        """
        self.data.set_index([self.addData[p] for p in index_levels], inplace = True)
        self.addData.set_index(index_levels, inplace = True)
        self.filter = self.data.notna()
        pass
    
    def _get_mu(self, X, ret_nonan = False):
        """
        Returns the mean values for the vector of N variables with M values per variable.

        Before calculations all rows with at least one numpy.nan value are removed.
        
        Parameters
        ----------
        X : numpy.ndarray or pandas.DataFrame
            Shape (M, N).
        ret_nonan : bool, default False
            Specifies if the `X` cleaned from rows containing numpy.nan values should be returned.

        Returns
        -------
        mu : numpy.ndarray
            Mean values of the vector `X`, shape (N, ).
        x_ : numpy.ndarray
            If `ret_nonan = True`, returns `X` cleaned from rows containing numpy.nan values.
        """
        x_ = self._remove_nan(X)
        mu = np.array(x_.mean(axis = 0))
        if ret_nonan:
            return mu, x_
        else:
            return mu

    def _remove_nan(self, X):
        """
        Remove rows with numpy.nan values.

        Parameters
        ----------
        X : numpy.ndarray or pandas.DataFrame
            Shape (M, N).
        """
        try:
            XX = X[~np.isnan(X).any(axis = 1)]
            return XX
        except:
            XX = X[~np.isnan(X)]
            return XX

    def _get_covar_matrix(self, X):
        """
        Return the covariance matrix for the vector of N variables, with M values per variable.

        Parameters
        ----------
        X : numpy.ndarray or pandas.DataFrame
            Shape = (M x N), M > 1, otherwise returns matrix N x N filled with numpy.nan or numpy.nan if M = 1.

        Returns
        -------
        out : numpy.ndarray
            Shape (N, N).
        """
        mu, XX = self._get_mu(X, ret_nonan=True)
        try:
            covar_matrix = 1/(XX.shape[0] - 1) * np.dot((XX - mu).T,(XX - mu))
            return covar_matrix
        except ZeroDivisionError:
            try:
                res = np.empty((XX.shape[1],XX.shape[1]))
                res.fill(np.nan)
                return res
            except IndexError:
                res = np.nan
                return res

    def _get_disp(self, X):
        """
        Return the square root of the diagonal elements of the covariance matrix (M x N) for the vector of N variables,
        with M values per variable.
        
        Parameters
        ----------
        X : numpy.ndarray or pandas DataFrame
            Shape = M x N, M > 1 otherwise returns array filled with nan.

        Returns
        -------
        out : numpy.ndarray
            Shape = (N, ).
        """
        try:
            covar_matrix = self._get_covar_matrix(X)
            if not isinstance(covar_matrix, np.ndarray):
                return np.sqrt(covar_matrix)
            else:
                disp = np.sqrt(np.diag(covar_matrix))
            return disp
        except ValueError:
            XX = self._remove_nan(X)
            disp = np.empty((XX.shape[1],))
            disp.fill(np.nan)
            return disp