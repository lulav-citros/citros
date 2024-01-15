from citros.data.analysis import CitrosData
from citros.data.access import CitrosDict

import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
import numpy as np
from termcolor import colored
from matplotlib.ticker import MaxNLocator
from typing import Union
from citros.data.access._utils import _get_logger

class Validation:
    """
    Validation class.

    Parameters
    ----------
    df : pandas.DataFrame
        Data table to perform validation tests on.
    data_label : str or list of str
        Specifies the label(s) of the data column(s) in data table.
    param_label : str
        Specifies the label of the column used to calculate the indices.
    method : {'scale', 'bin'}, default 'scale'
        Method of data preparation: scaling to [0,1] interval or binning.
    num : int, default 100
        Number of points in a new scale that will be used for interpolation if the `method` is 'scale'
        or number of bins if the `method` is 'bin'.
    units : str, optional
        Specifies units of the data.
    omit_nan_rows : bool
        If True, rows with one or more NaN values will be omitted from the analysis.
        If not specified, considered to be True.
    inf_vals : None or float, default 1e308
        If specified, all values from `data_label` column that exceed the provided value in absolute terms
        will be treated as NaN values. If this functionality is not required, set inf_vals = None.
    log : log : logging.Logger, default None
        Logger to record log. If None, then the new logger is created.

    Attributes
    ----------
    df : pandas.DataFrame or None
        Data table to perform validation tests on.
    db : analysis.citros_data.CitrosData or None
        CitrosData object after binning or scaling.
    stat : analysis.citros_stat.CitrosStat or None
        CitrosStat object that stores mean, standard deviation and covariance matrix as attributes.

    Examples
    --------
    Import Validation and CitrosDB:

    >>> from citros import CitrosDB, Validation

    From the batch 'albedo' of the simulation 'planetary_nebula' from the json-data column of the topic 'A' 
    download simulated data labeled as 'data.x.x_1' and column with time 'data.time'.

    >>> citros = CitrosDB(simulation = 'planetary_nebula', batch = 'albedo')
    >>> df = citros.topic('A').set_order({'sid':'asc','rid':'asc'}).data(['data.x.x_1','data.time'])
    >>> print(df)
        sid   rid   time        topic   type   data.x.x_1   data.time
    0   1     0     312751159   A       a      0.000        10.0
    1   1     1     407264008   A       a      0.008        17.9
    2   1     2     951279608   A       a      0.016        20.3

    Set 'data.time' as independent variable and 'data.x.x_1' as dependent one.
    `method` defines the method of data preparation and index assignment: method = 'bin' - bins values of column `param_label` in `num` intervals,
    set index to each of the interval, group data according to the binning and calculate mean data values for each group.

    >>> V = Validation(df, data_label = ['data.x.x_1'], param_label = 'data.time',
    ...                method = 'bin', num = 50, units = 'm')

    For topic 'A' download 3-dimensional json-data 'data.x' that contains 'data.x.x_1', 'data.x.x_2' and 'data.x.x_3' columns,
    and column with time 'data.time'.
    >>> df = citros.topic('A').set_order({'sid':'asc','rid':'asc'}).data(['data.x','data.time'])
    >>> print(df['data.x'])
    0          {'x_1': 0.0, 'x_2': 0.08, 'x_3': 0.047}
    1       {'x_1': 0.008, 'x_2': 0.08, 'x_3': -0.003}
    2      {'x_1': 0.016, 'x_2': 0.078, 'x_3': -0.034}
    ...

    Set 'data.time' as independent variable and 'data.x' as dependent vector.
    `method` defines the method of data preparation and index assignment: method = 'scale' - scales parameter `param_label` for each of the 'sid' to [0, 1] interval
    and interpolate data on the new scale.

    >>> V = Validation(df, data_label = 'data.x', param_label = 'data.time',
    ...                method = 'scale', num = 50, units = 'm')
    """

    def __init__(
        self,
        df=None,
        data_label=None,
        param_label=None,
        method="scale",
        num=100,
        units="",
        omit_nan_rows=True,
        inf_vals=1e308,
        log = None,
    ):
        if log is None:
            self.log = _get_logger(__name__)

        self._set_data_table(
            df,
            data_label,
            param_label,
            method=method,
            num=num,
            units=units,
            omit_nan_rows=omit_nan_rows,
            inf_vals=inf_vals,
        )

    def _set_data_table(
        self,
        df,
        data_label,
        param_label,
        method="scale",
        num=100,
        units="",
        omit_nan_rows=True,
        inf_vals=1e308,
    ):
        """
        Set data table to perform validation tests on.

        Parameters
        ----------
        df : pandas.DataFrame
            Data table to perform validation tests on.
        data_label : str or list of str
            Specifies label(s) of the data column(s) in data table.
        param_label : str
            Label of column on the basis of which the indices will be calculated.
        method : {'scale', 'bin'}, default 'scale'
            Method of data preparation: scaling to [0,1] interval or binning.
        num : int, default 100
            Number of points in a new scale that will be used for interpolation or number of bins.
        units : str, optional
            Specifies units of the data.
        omit_nan_rows : bool
            If True, rows with one or more NaN values will be omitted from the analysis.
            If not specified, considered to be True.
        inf_vals : None or float, default 1e308
            If specified, all values from `data_label` column that exceed the provided value in absolute terms
            will be omitted from the analysis. If this functionality is not required, set inf_vals = None.

        See Also
        --------
        analysis.citros_data.CitrosData.bin_data :
            Bin values of column `param_label` in `num` intervals, group data according to the binning and calculate mean values of each group.
        analysis.citros_data.CitrosData.scale_data :
            Scale parameter `param_label` for each of the 'sid' and interpolate data on the new scale.
        """
        if df is not None:
            if isinstance(df, pd.DataFrame):
                self.df = df.copy()
                if data_label is None:
                    self.log.error("`data_label` must be a label of the 'df' column")
                    self.db = None
                    self.stat = None
                    return
                else:
                    dataset = CitrosData(
                        self.df,
                        data_label=data_label,
                        units=units,
                        omit_nan_rows=omit_nan_rows,
                        inf_vals=inf_vals,
                    )
                    if param_label is None:
                        self.log.error("`param_label` must be a label of the 'df' column")
                        self.db = None
                        self.stat = None
                        return
                    else:
                        if method == "bin":
                            self.db = dataset.bin_data(
                                n_bins=num, param_label=param_label, show_fig=False
                            )
                        elif method == "scale":
                            self.db = dataset.scale_data(
                                n_points=num, param_label=param_label, show_fig=False
                            )
                        else:
                            self.log.error("`method` must be 'scale' or 'bin")
                            self.db = None
                            self.stat = None
                            return
                        self.stat = self.db.get_statistics(return_format="citrosStat")
            else:
                self.log.error("`df` must be a pandas DataFrame")
                self.df = None
                self.db = None
                self.stat = None
                return
        else:
            self.df = None
            self.db = None
            self.stat = None

    def std_bound_test(
        self,
        limits: Union[float, list] = 1.0,
        n_std: int = 3,
        nan_passed: bool = True,
        std_color: str = "b",
        connect_nan_std: bool = False,
        std_area: bool = False,
        std_lines: bool = True,
    ):
        """
        Test whether `n_std`-standard deviation boundary is within the given limits.

        The output is:
        - dictionary with summary of the test results, with the following structure:
        ```python
        {
        'test_param' : list,          # initial tests parameters
        column_name:                  # label of the column, str
            {'passed' : bool},        # if the tests was passed or not
            {'pass_rate' : float},    # fraction of the points that pass the test
            {'failed' : 
                {x_index: x_value}},  # indexes and values of the x coordinate of 
                                      #   the points that fail the test {int: float} 
            {'nan_std' :
                {x_index: x_value}}   # indexes and values of the x coordinate of the points
        }                             #   that have NaN (Not a Number) values for standard deviation
        ```
        - table that provides test results for each standard deviation boundary point, 
        using a boolean value to indicate whether it passed or failed the test;

        - figure with plotted simulations, mean values, standard deviation boundaries and limit boundaries;

        Parameters
        ----------
        limits : float or list, default 1.0
            Limit to test standard deviation boundary. Limits may be set as:
            - one value and it will be treated as an +- interval: value -> [-value, value];
            - list of lower and upper limits: [lower_limit, upper_limit];
            - If the data has multiple columns, limits may be set for each of the column.
            That way list length must be equal to number of columns. For example, for the 3-dimensional vector with corresponding standard deviation boundaries [std_bound_1, std_bound_2, std_bound_3]:
            [[**limit_lower**, **limit_upper**], **value_1**, **value_2**] will be processed as: 
            **limit_lower** < std_bound_1 < **limit_upper**,
            -**value_1** < std_bound_2 < **value_1**,
            -**value_2** < std_bound_2 < **value_2**.

        n_std : int, default 3
            The parameter specifies the number of standard deviations to be within limits.
        nan_passed : bool, default True
            If True, the NaN values of standard deviation will pass the test.

        Returns
        -------
        log : access.citros_dict.CitrosDict
            Dictionary with validation test results.
        table : pandas.DataFrame
            Table with test results for each of the standard deviation boundary point, indicating whether it passes or fails the test.
        fig : matplotlib.figure.Figure
            Figure with plotted simulations, mean values, standard deviation boundaries and limit boundaries.

        Other Parameters
        ----------------
        std_color : str, default 'b'
            Color for displaying standard deviations, blue by default.
        connect_nan_std : bool, default False
            If True, all non-NaN values in standard deviation boundary line are connected, resulting in a continuous line. 
            Otherwise, breaks are introduced in the standard deviation line whenever NaN values are encountered.
        std_area : bool, default False
            Fill area within `n_std`-standard deviation lines with color.
        std_lines : bool, default True
            If False, remove standard deviation boundary lines.

        See Also
        --------
        pandas.DataFrame, pandas.Series

        Examples
        --------
        Import Validation and CitrosDB:

        >>> from citros import CitrosDB, Validation

        From the batch 'density' of the simulation 'diffuse_nebula' from the topic 'A' download 2 columns of the simulated data 
        labeled 'data.x.x_1' and 'data.x.x_2' and column with time 'data.time'.
        Set 'data.time' as independent variable and 'data.x.x_1' and 'data.x.x_2' as dependent 2-dimensional vector.
        `method` defines the method of data preparation and index assignment: method = 'bin' - bins values of column `param_label` in `num` intervals, 
        set index to each of the interval, group data according to the binning and calculate mean data values for each group.
        
        >>> citros = CitrosDB(simulation = 'diffuse_nebula', batch = 'density')
        >>> df = citros.topic('A').set_order({'sid':'asc','rid':'asc'})\\
        ...                       .data(['data.x.x_1','data.x.x_2','data.time'])
        >>> V = Validation(df, data_label = ['data.x.x_1', 'data.x.x_2'], param_label = 'data.time', 
        ...                method = 'bin', num = 50, units = 'm')

        Test whether 3-sigma standard deviation boundary is within interval [-0.3, 0.3] (treat nan values of the
        standard deviation, if they exist, as passing the test):

        >>> log, table, fig = V.std_bound_test(limits = 0.3, n_std = 3, nan_passed = True)
        >>> log.print()
        std_bound_test: passed
        {
         'test_param': {
           'limits': 0.3,
           'n_std': 3,
           'nan_passed': True
         },
         'data.x.x_1': {
           'passed': True,
           'pass_rate': 1.0,
           'failed': {
           },
           'nan_std': {
             49: 807.942
           }
         },
         'data.x.x_2': {
           'passed': True,
           'pass_rate': 1.0,
           'failed': {
           },
           'nan_std': {
             49: 807.942
           }
         }
        }

        The same, but set limit interval to be [-1, 0.3]:

        >>> log, table, fig = V.std_bound_test(limits = [-1, 0.3], n_std = 3, nan_passed = True)
        std_bound_test: passed

        Set different limits for 1-sigma standard deviation boundaries of 2-dimensional vector: for the first 
        element of the vector boundaries should be within interval [-1, 2] and for the second one - [-0.5, 0.5]:

        >>> log, table, fig = V.std_bound_test(limits = [[-1, 2], 0.5], n_std = 1)
        std_bound_test: passed

        The same as in the previous example, but limits should be [-1, 1] for the first element of the vector 
        and [-0.5, 0.5] for the second. In this case limits should be set as [[-1, 1], [-0.5, 0.5]] and not as [1, 0.5],
        because in the latter case limits will be treated as a common boundary for both elements.

        >>> log, table, fig = V.std_bound_test(limits = [[-1, 1], [-0.5, 0.5]], n_std = 1)
        std_bound_test: passed

        Download 3-dimensional json-data 'data.x' that contains 'data.x.x_1', 'data.x.x_2' and 'data.x.x_3' columns, and column with time 'data.time'.
        Set 'data.time' as independent variable and 'data.x' as dependent vector.
        `method` defines the method of data preparation and index assignment: method = 'scale' - scales parameter `param_label` for each of the 'sid' to [0, 1] interval 
        and interpolate data on the new scale.
        
        >>> df = citros.topic('A').set_order({'sid':'asc','rid':'asc'}).data(['data.x','data.time'])
        >>> V3 = Validation(df, data_label = 'data.x', param_label = 'data.time', 
        ...                 method = 'scale', num = 50, units = 'm')

        Set different limits on 3-dimensional vector: [-0.5, 0.5] for the first element, [-1.5, 1.5] for the second,
        [-20, 10] for the third:

        >>> log, table, fig = V3.std_bound_test(limits = [0.5, 1.5, [-20, 10]], n_std = 3)
        std_bound_test: passed
        """
        fig, ax = self.db._plot_statistics(
            self.stat,
            fig_title="Std boundary test",
            # show_fig=False,
            return_fig=True,
            n_std=n_std,
            std_color=std_color,
            connect_nan_std=connect_nan_std,
            std_area=std_area,
            std_lines=std_lines,
        )
        lower_limit, upper_limit = self._get_limit_values(
            limits, len(self.db.data.columns)
        )
        if lower_limit is None:
            return None, None, None

        nan_std = ~self.stat.sigma.notna()  # True if the value is nan
        if_nan_sigma = nan_std.any()  # if there are any nan values in the column

        valid_b = (self.stat.mean - n_std * self.stat.sigma - lower_limit) > 0
        valid_t = (self.stat.mean + n_std * self.stat.sigma - upper_limit) < 0

        result = valid_t * valid_b.values

        # change results of the test for nan std values if nan_passed is True and the nan value are presented
        if if_nan_sigma.any() and nan_passed:
            result.where(
                ~nan_std, True, inplace=True
            )  # change test results to True if the value was nan

        # insert column with `param_label` as a first column
        result.insert(
            0,
            self.db.x_label,
            self.db.addData.groupby(self.db.xid_label).first()[self.db.x_label],
        )

        # get log
        init_param = {"limits": limits, "n_std": n_std, "nan_passed": nan_passed}
        log = self._get_mean_std_log(init_param, result)

        # adding information about nan values of the standard deviations
        for col in self.db.data.columns:
            if if_nan_sigma[col]:
                log[col]["nan_std"] = CitrosDict(
                    result[self.db.x_label].loc[nan_std[col]].to_dict()
                )
            else:
                log[col]["nan_std"] = CitrosDict()

        # print_result
        all_pass = []
        for col in self.db.data.columns:
            all_pass.append(log[col]["passed"])

        if np.array(all_pass).all():
            print("std_bound_test: " + colored("passed", "green"))
        else:
            print("std_bound_test: " + colored("failed", "red"))

        # plot bounds on fig
        self._plot_bounds(result, lower_limit, upper_limit, fig)

        return log, result, fig

    def mean_test(self, limits: Union[float, list] = 1.0, nan_passed: bool = True):
        """
        Test whether mean is within the given limits.

        The output is:
        - dictionary with summary of the test results, with the following structure:
        ```python
        {
        'test_param' : list,          # initial tests parameters
        column_name:                  # label of the column, str
            {'passed' : bool},        # if the tests was passed or not.
            {'pass_rate' : float},    # fraction of the points that pass the test
            {'failed' : 
                {x_index: x_value}},  # indexes and values of the x coordinate of the 
        }                             #   points that fail the test {int: float}   
        ```

        - table that provides test results for each of the mean point, 
        using a boolean value to indicate whether it passed or failed the test;

        - figure with plotted simulations, mean values and limit boundaries.

        Parameters
        ----------
        limits : float or list, default 1.0
            Limit to test mean. Limits may be set as:
            - one value and it will be treated as an +- interval: value -> [-value, value];
            - list of lower and upper limits: [lower_limit, upper_limit];
            - If the data has multiple columns, limits may be set for each of the column.
            That way list length must be equal to number of columns. For example, for the 3-dimensional vector with corresponding mean vector [mean_1, mean_2, mean_3]:
            [[**limit_lower**, **limit_upper**], **value_1**, **value_2**] will be processed as: 
            **limit_lower** < mean_1 < **limit_upper**,
            -**value_1** < mean_2 < **value_1**,
            -**value_2** < mean_2 < **value_2**.

        nan_passed : bool, default True
            If True, the NaN values of the mean will pass the test.

        Returns
        -------
        log : access.citros_dict.CitrosDict
            Dictionary with validation test results.
        table : pandas.DataFrame
            Table with test results for each of the mean point, indicating whether it passes or fails the test.
        fig : matplotlib.figure.Figure
            Figure with plotted simulations, mean values and limit boundaries.
        
        Examples
        --------
        Import Validation and CitrosDB:

        >>> from citros import CitrosDB, Validation

        From the batch 'density' of the simulation 'diffuse_nebula' from the topic 'A' download 2 columns of the simulated data 
        labeled 'data.x.x_1' and 'data.x.x_2' and column with time 'data.time'.
        Set 'data.time' as independent variable and 'data.x.x_1' and 'data.x.x_2' as dependent 2-dimensional vector.
        `method` defines the method of data preparation and index assignment: method = 'bin' - bins values of column `param_label` in `num` intervals, 
        set index to each of the interval, group data according to the binning and calculate mean data values for each group.
        
        >>> citros = CitrosDB(simulation = 'diffuse_nebula', batch = 'density')
        >>> df = citros.topic('A').set_order({'sid':'asc','rid':'asc'})\\
        ...                       .data(['data.x.x_1','data.x.x_2','data.time'])
        >>> V = Validation(df, data_label = ['data.x.x_1', 'data.x.x_2'], param_label = 'data.time', 
        ...                method = 'bin', num = 50, units = 'm')

        Test whether mean values are is within the  interval [-10, 10]:

        >>> log, table, fig = V.mean_test(limits = 10)
        >>> log.print()
        mean_test: passed
        {
         'test_param': {
           'limits': 10
         },
         'data.x.x_1': {
           'passed': True,
           'pass_rate': 1.0,
           'failed': {
           }
         },
         'data.x.x_2': {
           'passed': True,
           'pass_rate': 1.0,
           'failed': {
           }
         }
        }

        The same, but set limit interval to be [-0.5, 0.8]:

        >>> log, table, fig = V.mean_test(limits = [-0.5, 0.8])
        mean_test: passed

        Set different limits on mean values for each of the 1-dimensional element of the 2-dimensional vector: 
        [-0.05, 0.08] for the first element and [-0.5, 0.5] for the second:

        >>> log, table, fig = V.mean_test(limits = [[-0.05, 0.08], 0.5])
        mean_test: passed

        The same as in the previous example, but limits should be [-1, 1] for the first element of the vector 
        and [-0.5, 0.5] for the second. In this case limits should be set as [[-1, 1], [-0.5, 0.5]] and not as [1, 0.5],
        because in the latter case limits will be treated as a common boundary for both elements.

        >>> log, table, fig = V.mean_test(limits = [[-1, 1], [-0.5, 0.5]])
        mean_test: passed

        Download 3-dimensional json-data 'data.x' that contains 'data.x.x_1', 'data.x.x_2' and 'data.x.x_3' columns, and column with time 'data.time'.
        Set 'data.time' as independent variable and 'data.x' as dependent vector.
        `method` defines the method of data preparation and index assignment: method = 'scale' - scales parameter `param_label` for each of the 'sid' to [0, 1] interval 
        and interpolate data on the new scale.
        
        >>> df = citros.topic('A').set_order({'sid':'asc','rid':'asc'}).data(['data.x','data.time'])
        >>> V3 = Validation(df, data_label = 'data.x', param_label = 'data.time', 
        ...                 method = 'scale', num = 50, units = 'm')

        Set different limits on 3-dimensional vector: [-0.5, 0.5] for the first element, [-1.5, 1.5] for the second,
        [-20, 10] for the third:
        
        >>> log, table, fig = V3.mean_test(limits = [0.5, 1.5, [-20, 10]])
        mean_test: passed
        """
        fig, ax = self.db._plot_statistics(
            self.stat,
            fig_title="Mean test",
            # show_fig=False,
            return_fig=True,
            n_std=None,
            std_color="b",
        )
        lower_limit, upper_limit = self._get_limit_values(
            limits, len(self.db.data.columns)
        )
        if lower_limit is None:
            return None, None, None

        nan_mean = ~self.stat.mean.notna()  # True if the value is nan
        if_nan_mean = nan_mean.any()  # if there are any nan values in the column

        valid_b = (self.stat.mean - lower_limit) > 0
        valid_t = (self.stat.mean - upper_limit) < 0

        result = valid_t * valid_b.values

        # change results of the test for nan mean values if nan_passed is True and the nan value are presented
        if if_nan_mean.any() and nan_passed:
            result.where(
                ~nan_mean, True, inplace=True
            )  # change test results to True if the value was nan

        # insert column with `param_label` as a first column
        result.insert(
            0,
            self.db.x_label,
            self.db.addData.groupby(self.db.xid_label).first()[self.db.x_label],
        )

        # get log and put plot bounds on fig
        init_param = {"limits": limits}
        log = self._get_mean_std_log(init_param, result)

        # print results
        all_pass = []
        for col in self.db.data.columns:
            all_pass.append(log[col]["passed"])

        if np.array(all_pass).all():
            print("mean_test: " + colored("passed", "green"))
        else:
            print("mean_test: " + colored("failed", "red"))

        # plot bounds on fig
        self._plot_bounds(result, lower_limit, upper_limit, fig)

        return log, result, fig

    def std_test(
        self,
        limits: Union[float, list] = 1.0,
        n_std: int = 3,
        nan_passed: bool = True,
        std_color: str = "b",
        connect_nan_std: bool = False,
        std_area: bool = False,
        std_lines: bool = True,
    ):
        """
        Test whether `n_std`-standard deviation does not exceed the given limits.

        The output is:
        - dictionary with summary of the test results, with the following structure:
        ```python
        {
        'test_param' : list,          # initial tests parameters
        column_name:                  # label of the column, str
            {'passed' : bool},        # if the tests was passed or not
            {'pass_rate' : float},    # fraction of the points that pass the test
            {'failed' : 
                {x_index: x_value}},  # indexes and values of the x coordinate of 
                                      #   the points that fail the test {int: float} 
            {'nan_std' :
                {x_index: x_value}}   # indexes and values of the x coordinate of the points
        }                             #   that have NaN (Not a Number) values for standard deviation
        ```

        - table that provides test results for each standard deviation point, 
        using a boolean value to indicate whether it passed or failed the test.

        - figure with standard deviations and limit boundaries.

        Parameters
        ----------
        limits : float or list, default 1.0
            Limit to test standard deviation. Limits may be set as:
            - one value;
            - If the data has multiple columns, limits may be set for each of the column.
            That way list length must be equal to number of columns. 
            For example, in case of 3-dimensional vector with corresponding standard deviation vector = [std_1, std_2, std_3], limits = [**value_1**, **value_2**, **value_3**] will be processed as:
            std_1 < **value_1**,
            std_2 < **value_2**,
            std_2 < **value_3**.

        n_std : int, default 3
            The parameter specifies the number of standard deviations to be less then limits.
        nan_passed : bool, default True
            If True, the NaN values of standard deviation will pass the test.

        Returns
        -------
        log : access.citros_dict.CitrosDict
            Dictionary with validation test results.
        table : pandas.DataFrame
            Table with test results for each of the standard deviation point, indicating whether it passes or fails the test.
        fig : matplotlib.figure.Figure
            Figure with standard deviations and limit boundaries.

        Other Parameters
        ----------------
        std_color : str, default 'b'
            Color for displaying standard deviation, blue by default.
        connect_nan_std : bool, default False
            If True, all non-NaN values in standard deviation line are connected, resulting in a continuous line. 
            Otherwise, breaks are introduced in the standard deviation line whenever NaN values are encountered.
        std_area : bool, default False
            Fill area within `n_std`-standard deviation line with color.
        std_lines : bool, default True
            If False, remove standard deviation line.

        See Also
        --------
        pandas.DataFrame, pandas.Series

        Examples
        --------
        Import Validation and CitrosDB:

        >>> from citros import CitrosDB, Validation

        From the batch 'density' of the simulation 'diffuse_nebula' from the topic 'A' download 2 columns of the simulated data 
        labeled 'data.x.x_1' and 'data.x.x_2' and column with time 'data.time'.
        Set 'data.time' as independent variable and 'data.x.x_1' and 'data.x.x_2' as dependent 2-dimensional vector.
        `method` defines the method of data preparation and index assignment: method = 'bin' - bins values of column `param_label` in `num` intervals, 
        set index to each of the interval, group data according to the binning and calculate mean data values for each group.
        
        >>> citros = CitrosDB(simulation = 'diffuse_nebula', batch = 'density')
        >>> df = citros.topic('A').set_order({'sid':'asc','rid':'asc'})\\
        ...                       .data(['data.x.x_1','data.x.x_2','data.time'])
        >>> V = Validation(df, data_label = ['data.x.x_1', 'data.x.x_2'], param_label = 'data.time', 
        ...                method = 'bin', num = 50, units = 'm')

        Test whether 3-sigma standard deviation is within interval [-0.3, 0.3] (treat nan values of the
        standard deviation, if they exist, as passing the test):

        >>> log, table, fig = V.std_test(limits = 1.5, n_std = 3, nan_passed = True)
        >>> log.print()
        std_bound_test: passed
        {
         'test_param': {
           'limits': 0.3,
           'n_std': 3,
           'nan_passed': True
         },
         'data.x.x_1': {
           'passed': True,
           'pass_rate': 1.0,
           'failed': {
           },
           'nan_std': {
             49: 807.942
           }
         },
         'data.x.x_2': {
           'passed': True,
           'pass_rate': 1.0,
           'failed': {
           },
           'nan_std': {
             49: 807.942
           }
         }
        }

        Download 3-dimensional json-data 'data.x' that contains 'data.x.x_1', 'data.x.x_2' and 'data.x.x_3' columns, and column with time 'data.time'.
        Set 'data.time' as independent variable and 'data.x' as dependent vector.
        `method` defines the method of data preparation and index assignment: method = 'scale' - scales parameter `param_label` for each of the 'sid' to [0, 1] interval 
        and interpolate data on the new scale.
        
        >>> df = citros.topic('A').set_order({'sid':'asc','rid':'asc'}).data(['data.x','data.time'])
        >>> V3 = Validation(df, data_label = 'data.x', param_label = 'data.time', 
        ...                 method = 'scale', num = 50, units = 'm')

        Set different limits on 3-dimensional vector: 1.5 for the first element, 1.5 for the second,
        30 for the third:

        >>> log, table, fig = V3.std_test(limits = [1.5, 1.5, 30], n_std = 3)
        std_test: passed
        """
        upper_limit = self._get_1D_limit(limits, len(self.db.data.columns))
        if upper_limit is None:
            return None, None, None

        nan_std = ~self.stat.sigma.notna()  # True if the value is nan
        if_nan_sigma = nan_std.any()  # if there are any nan values in the column

        result = (n_std * self.stat.sigma - upper_limit) < 0

        # change results of the test for nan std values if nan_passed is True and the nan value are presented
        if if_nan_sigma.any() and nan_passed:
            result.where(
                ~nan_std, True, inplace=True
            )  # change test results to True if the value was nan

        # insert column with `param_label` as a first column
        result.insert(
            0,
            self.db.x_label,
            self.db.addData.groupby(self.db.xid_label).first()[self.db.x_label],
        )

        # get log
        init_param = {"limits": limits, "n_std": n_std, "nan_passed": nan_passed}
        log = self._get_mean_std_log(init_param, result)

        # adding information about nan values of the standard deviations
        for col in self.db.data.columns:
            if if_nan_sigma[col]:
                log[col]["nan_std"] = CitrosDict(
                    result[self.db.x_label].loc[nan_std[col]].to_dict()
                )
            else:
                log[col]["nan_std"] = CitrosDict()

        # print_result
        all_pass = []
        for col in self.db.data.columns:
            all_pass.append(log[col]["passed"])

        if np.array(all_pass).all():
            print("std_test: " + colored("passed", "green"))
        else:
            print("std_test: " + colored("failed", "red"))

        # plot fig
        fig, ax = plt.subplots(nrows=len(self.db.data.columns), ncols=1)
        if not isinstance(ax, np.ndarray):
            ax = np.array([ax])
        if len(upper_limit.shape) == 0:
            upper_limit = [upper_limit] * len(self.stat.sigma.columns)

        for i, y_col in enumerate(self.stat.sigma.columns):
            res_sigm = self.stat.sigma[y_col]
            y_0 = pd.Series([0] * len(res_sigm), index=res_sigm.index)
            if connect_nan_std:
                filter_st = res_sigm.notna()
                line_style_custom = "-"
            else:
                filter_st = pd.Series([True] * len(res_sigm), index=res_sigm.index)
                if res_sigm.notna().all():
                    line_style_custom = "-"
                else:
                    line_style_custom = ".-"
            if std_lines:
                ax[i].plot(
                    result[self.db.x_label][filter_st],
                    n_std * res_sigm[filter_st],
                    line_style_custom,
                    color=std_color,
                    label=str(n_std) + r"$\sigma$",
                    markersize=0.7,
                )
                label = None
            else:
                label = str(n_std) + r"$\sigma$"
            if std_area:
                ax[i].fill_between(
                    result[self.db.x_label][filter_st].values,
                    n_std * res_sigm[filter_st].values,
                    y_0[filter_st].values,
                    color=std_color,
                    label=label,
                    alpha=0.12,
                )

            ax[i].plot(
                [min(result[self.db.x_label]), max(result[self.db.x_label])],
                [upper_limit[i], upper_limit[i]],
                "r",
                label="limit",
            )
            ylabel = (
                "std " + y_col + ", [" + self.db.units + "]"
                if self.db.units != ""
                else ""
            )
            ax[i].set_ylabel(ylabel)
            ax[i].grid(True)
        fig.supxlabel(self.db.x_label)
        fig.suptitle("Std test")
        handles, labels = ax[-1].get_legend_handles_labels()
        fig.legend(handles, labels, bbox_to_anchor=(1.0, 0.94), loc="upper left")
        fig.tight_layout()
        # self._plot_bounds(result, self.stat.mean - upper_limit, self.stat.mean + upper_limit, fig)

        return log, result, fig

    def sid_test(self, limits: Union[float, list] = 1.0, nan_passed: bool = True):
        """
        Test whether all simulations are within the given limits.

        The output is:
        - dictionary with summary of the test results, with the following structure:
        ```python
        {
        'test_param' : list,                # initial tests parameters
        column_name:                        # label of the column, str
            {'passed' : bool},              # if the tests was passed or not.
            {'pass_rate' : 
                {'sid_fraction' : float},   # fraction of simulations that pass the test
                {sid : fraction}},          # fraction of the points that pass the test for each simulation {int: float}
            {'failed' : 
                {sid :                      # id of the simulation that contains points that failed the test
                    {x_index: x_value}}},   # indexes and values of the x coordinate of the points 
        }                                   #   that fail the test {int: {int: float}}
        ```

        - table that provides test results for for each point of the simulations, 
        using a boolean value to indicate whether it passed or failed the test;

        - figure with plotted simulations, mean values and limit boundaries.

        Parameters
        ----------
        limits : float or list, default 1.0
            Limit to test simulation results. Limits may be set as:
            - one value and it will be treated as an +- interval: value -> [-value, value];
            - list of lower and upper limits: [lower_limit, upper_limit];
            - If the data has multiple columns, limits may be set for each of the column.
            That way list length must be equal to number of columns. For example, for the 3-dimensional vector that contains v1, v2, v3 columns and numbers N simulations:
            [[**limit_lower**, **limit_upper**], **value_1**, **value_2**] will be processed as: 
            **limit_lower** < v1 < **limit_upper**, 
            -**value_1** < v2 < **value_1**, 
            -**value_2** < v3 < **value_2** for each of the N simulations.

        nan_passed : bool, default True
            If True, the NaN values will pass the test.

        Returns
        -------
        log : access.citros_dict.CitrosDict
            Dictionary with validation test results.
        table : pandas.DataFrame
            Table with test results for each point of the simulations, indicating whether it passes or fails the test.
        fig : matplotlib.figure.Figure
            Figure with plotted simulations, mean values and limit boundaries.

        Examples
        --------
        Import Validation and CitrosDB:

        >>> from citros import CitrosDB, Validation

        From the batch 'density' of the simulation 'diffuse_nebula' from the topic 'A' download 2 columns of the simulated data 
        labeled 'data.x.x_1' and 'data.x.x_2' and column with time 'data.time'.
        Set 'data.time' as independent variable and 'data.x.x_1' and 'data.x.x_2' as dependent 2-dimensional vector.
        `method` defines the method of data preparation and index assignment: method = 'bin' - bins values of column `param_label` in `num` intervals, 
        set index to each of the interval, group data according to the binning and calculate mean data values for each group.
        
        >>> citros = CitrosDB(simulation = 'diffuse_nebula', batch = 'density')
        >>> df = citros.topic('A').set_order({'sid':'asc','rid':'asc'})\\
                                  .data(['data.x.x_1','data.x.x_2','data.time'])
        >>> V = Validation(df, data_label = ['data.x.x_1', 'data.x.x_2'], param_label = 'data.time', 
        ...                method = 'bin', num = 50, units = 'm')

        Test whether all simulations are is within the interval [-10, 10]:

        >>> log, table, fig = V.sid_test(limits = 10)
        >>> log.print()
        sid_test: passed
        {
         'test_param': {
           'limits': 10
         },
         'data.x.x_1': {
           'passed': True,
           'pass_rate': 1.0,
           'failed': {
           }
         },
         'data.x.x_2': {
           'passed': True,
           'pass_rate': 1.0,
           'failed': {
           }
         }
        }

        The same, but set limit interval to be [-0.5, 0.8]:

        >>> log, table, fig = V.sid_test(limits = [-0.5, 0.8])
        sid_test: passed

        Set different limits on mean values for each of the 1-dimensional element of the 2-dimensional vector: 
        [-0.05, 0.08] for the first element and [-0.5, 0.5] for the second:

        >>> log, table, fig = V.sid_test(limits = [[-0.05, 0.08], 0.5])
        sid_test: passed

        The same as in the previous example, but limits should be [-1, 1] for the first element of the vector 
        and [-0.5, 0.5] for the second. In this case limits should be set as [[-1, 1], [-0.5, 0.5]] and not as [1, 0.5],
        because in the latter case limits will be treated as a common boundary for both elements.

        >>> log, table, fig = V.sid_test(limits = [[-1, 1], [-0.5, 0.5]])
        sid_test: passed

        For topic 'A' download 3-dimensional json-data 'data.x' that contains 'data.x.x_1', 'data.x.x_2' and 'data.x.x_3' columns, and column with time 'data.time'.
        Set 'data.time' as independent variable and 'data.x' as dependent vector.
        `method` defines the method of data preparation and index assignment: method = 'scale' - scales parameter `param_label` for each of the 'sid' to [0, 1] interval 
        and interpolate data on the new scale.
        
        >>> df = citros.topic('A').set_order({'sid':'asc','rid':'asc'}).data(['data.x','data.time'])
        >>> V3 = Validation(df, data_label = 'data.x', param_label = 'data.time', 
        ...                 method = 'scale', num = 50, units = 'm')

        Set different limits on 3-dimensional vector: [-0.5, 0.5] for the first element, [-1.5, 1.5] for the second one, an
        [-20, 10] for the third vector element:
        
        >>> log, table, fig = V3.sid_test(limits = [0.5, 1.5, [-20, 10]])
        sid_test: passed
        """
        fig, ax = self.db._plot_statistics(
            self.stat,
            fig_title="Sid test",
            # show_fig=False,
            return_fig=True,
            n_std=None,
            std_color="b",
        )

        lower_limit, upper_limit = self._get_limit_values(
            limits, len(self.db.data.columns)
        )
        if lower_limit is None:
            return None, None, None

        nan_val = ~self.db.data.notna()  # True if the value is nan
        if_nan_val = nan_val.any()  # if there are any nan values in the column

        valid_b = (self.db.data - lower_limit) > 0
        valid_t = (self.db.data - upper_limit) < 0

        result = valid_t * valid_b.values

        # change results of the test for nan values if nan_passed is True and the nan value are presented
        if if_nan_val.any() and nan_passed:
            result.where(
                ~nan_val, True, inplace=True
            )  # change test results to True if the value was nan

        # insert column with `param_label` as a first column
        result.insert(0, self.db.x_label, self.db.addData[self.db.x_label])

        try:
            pass_rate = (
                (
                    result.groupby("sid")
                    .agg({col: "value_counts" for col in self.db.data.columns})
                    .xs(True, level=1)
                    / result[self.db.data.columns].groupby("sid").count()
                )
                .fillna(0)
                .apply(round, ndigits=3)
                .to_dict()
            )
        except KeyError:
            # in case all points failed test and there is no True values
            pass_rate = CitrosDict()
            for col in self.db.data.columns:
                sid = list(set(result[col].index.get_level_values("sid")))
                sid.sort()
                pass_rate[col] = CitrosDict(dict.fromkeys(sid, 0.0))

        try:
            pass_rate_overall = (
                (
                    result.groupby("sid")
                    .all()
                    .agg({col: "value_counts" for col in self.db.data.columns})
                    .loc[True]
                    / result[self.db.data.columns].groupby("sid").all().count().values
                )
                .fillna(0)
                .apply(round, ndigits=3)
                .to_dict()
            )
        except KeyError:
            # in case all points failed test and there is no True values
            pass_rate_overall = CitrosDict()
            for col in self.db.data.columns:
                pass_rate_overall[col] = 0.0

        passed = result.groupby("sid")[self.db.data.columns].all().all()

        log = CitrosDict()

        log["test_param"] = CitrosDict({"limits": limits})

        for col in self.db.data.columns:
            log[col] = CitrosDict()
            log[col]["passed"] = passed[col]
            log[col]["pass_rate"] = CitrosDict()
            log[col]["pass_rate"]["sid_fraction"] = pass_rate_overall[col]
            log[col]["pass_rate"].update(CitrosDict(pass_rate[col]))
            if log[col]["passed"]:
                log[col]["failed"] = CitrosDict()
            else:
                log[col]["failed"] = CitrosDict(
                    result[result[col] == False]
                    .swaplevel()
                    .groupby("sid")
                    .apply(
                        lambda f: CitrosDict(f.xs(f.name)[self.db.x_label].to_dict())
                    )
                    .to_dict()
                )
            # log[col]['table'] = result[[col]]

        # print results
        all_pass = []
        for col in self.db.data.columns:
            all_pass.append(log[col]["passed"])

        if np.array(all_pass).all():
            print("sid_test: " + colored("passed", "green"))
        else:
            print("sid_test: " + colored("failed", "red"))

        # plot bounds on fig
        self._plot_bounds(result, lower_limit, upper_limit, fig)

        return log, result, fig

    def norm_test(self, norm_type: str = "L2", limits: Union[float, list] = 1.0):
        """
        Test whether norm of the each simulation is less than the given limit.

        The output is:
        - dictionary with summary of the test results, with the following structure:
        ```python
        {
        'test_param' : list,                # initial tests parameters
        column_name :                       # label of the column, str
            {'passed' : bool},              # if the tests was passed or not.
            {'pass_rate' : float}           # fraction of the simulations that pass the test
            {'norm_value' :
                {sid: value}},              # norm for each of the simulation {int: float}
            {'failed' : list}               # sid that fail the test
        }
        ```

        - table that provides test results for each simulation,
        using a boolean value to indicate whether it passed or failed the test;

        - figure with plotted norm value and limits.

        Parameters
        ----------
        norm_type : {'L2', 'Linf'}, default 'L2'
            Norm type. Norm is calculated for each of the simulation. If data is a multidimensional vector, it is calculated
            for each simulation of the each vector element.
            Type of the norm:
            - 'L2' - Euclidean norm, square root of the sum of the squares.
            - 'Linf' - absolute maximum.

        limits : float or list, default 1.0
            Limits on the simulation norm. Limits may be set as:
            - one value;
            - if the data has multiple columns, limits may be set for each of the column separately as a list.
            That way list length must be equal to number of the columns.

        Returns
        -------
        log : access.citros_dict.CitrosDict
            Dictionary with validation test results.
        table : pandas.DataFrame
            Table with test results for each simulation, indicating whether it passes or fails the test.
        fig : matplotlib.figure.Figure
            Figure with plotted norm value and limits.

        Examples
        --------
        Import Validation and CitrosDB:

        >>> from citros import CitrosDB, Validation

        From the batch 'density' of the simulation 'diffuse_nebula' from the topic 'A' download 1 columns of the simulated data 
        labeled 'data.x.x_1' and column with time 'data.time'.
        Set 'data.time' as independent variable and 'data.x.x_1' as a dependent one.
        `method` defines the method of data preparation and index assignment: method = 'bin' - bins values of column `param_label` in `num` intervals,
        set index to each of the interval, group data according to the binning and calculate mean data values for each group.

        >>> citros = CitrosDB(simulation = 'diffuse_nebula', batch = 'density')
        >>> df = citros.topic('A').set_order({'sid':'asc','rid':'asc'}).data(['data.x.x_1','data.time'])
        >>> V = Validation(df, data_label = 'data.x.x_1', param_label = 'data.time',
        ...                method = 'bin', num = 50, units = 'm')

        Test whether L2 norm for each of the simulation does not exceed 1:

        >>> log, table, fig = V.norm_test(norm_type = 'L2', limits = 1)
        >>> log.print()
        >>> print(table)
        norm_test L2: passed
        {
         'test_param': {
           'limits': 1
         },
         'data.x.x_1': {
           'passed': True,
           'pass_rate': 1.0,
           'norm_value': {
             1: 0.39,
             2: 0.39,
             3: 0.38
           },
           'failed': []
         },
        }
        >>> print(table)
             data.x.x_1
        sid
        1          True
        2          True
        3          True

        Download 3-dimensional json-data 'data.x' that contains 'data.x.x_1', 'data.x.x_2' and 'data.x.x_3' columns, and column with time 'data.time'.
        Set 'data.time' as independent variable and 'data.x' as dependent vector.
        `method` defines the method of data preparation and index assignment: method = 'scale' - scales parameter `param_label` for each of the 'sid' to [0, 1] interval
        and interpolate data on the new scale.

        >>> df = citros.topic('A').set_order({'sid':'asc','rid':'asc'}).data(['data.x','data.time'])
        >>> V3 = Validation(df, data_label = 'data.x', param_label = 'data.time',
        ...                method = 'scale', num = 50, units = 'm')

        Set different limits on Linf norm for each of the element of the 3-dimensional vector: 1.0 for the first element,
        0.1 for the second one, and 0.5 for the third vector element:

        >>> log, table, fig = V3.norm_test(norm_type = 'Linf', limits = [1.0, 0.1, 0.5])
        norm_test Linf: passed
        """
        upper_limit = self._get_1D_limit(limits, len(self.db.data.columns))
        if upper_limit is None:
            return None, None, None

        norm = self._get_norm(norm_type)
        if norm is None:
            return None, None, None

        result = (norm - upper_limit) < 0

        try:
            pass_rate = (
                (
                    result.agg(
                        {col: "value_counts" for col in self.db.data.columns}
                    ).loc[True]
                    / result.count().values
                )
                .fillna(0)
                .apply(round, ndigits=3)
                .to_dict()
            )
        except KeyError:
            pass_rate = CitrosDict()
            for col in self.db.data.columns:
                pass_rate[col] = 0.0

        log = CitrosDict()
        log["test_param"] = CitrosDict({"limits": limits})

        for col in self.db.data.columns:
            log[col] = CitrosDict()
            log[col]["passed"] = result.all()[col]
            log[col]["pass_rate"] = pass_rate[col]
            log[col]["norm_value"] = CitrosDict(norm[col].to_dict())
            log[col]["failed"] = [k for k, v in result[col].to_dict().items() if not v]

        all_pass = []
        for col in self.db.data.columns:
            all_pass.append(log[col]["passed"])

        if np.array(all_pass).all():
            print("norm_test " + norm_type + ": " + colored("passed", "green"))
        else:
            print("norm_test " + norm_type + ": " + colored("failed", "red"))

        fig, axes = plt.subplots(nrows=len(norm.columns), ncols=1, figsize=(6, 6))
        if not isinstance(axes, np.ndarray):
            axes = [axes]

        for i, ax in enumerate(axes):
            col = norm.columns[i]
            index = norm[col].index
            ax.barh(index, norm[col].values, align="center", label="sid norm")

            ax.yaxis.set_major_locator(MaxNLocator(integer=True))

            y_min = min(index)
            y_max = max(index)
            y_tick_labels = []
            y_tick_position = []
            for y_tick in fig.axes[0].get_yticklabels():
                y_pos = y_tick.get_position()[1]
                if (y_pos >= y_min) and (y_pos <= y_max):
                    y_tick_labels.append(y_tick.get_text())
                    y_tick_position.append(y_pos)

            if len(y_tick_labels) > 1:
                if str(y_min) not in y_tick_labels:
                    y_tick_labels = [str(y_min)] + y_tick_labels
                    y_tick_position = [y_min] + y_tick_position
                if str(y_max) not in y_tick_labels:
                    y_tick_labels = y_tick_labels + [str(y_max)]
                    y_tick_position = y_tick_position + [y_max]
            ax.set_yticks(y_tick_position, labels=y_tick_labels)

            ylabel = col
            ax.set_ylabel(ylabel)
            ylim = ax.get_ylim()
            if isinstance(upper_limit, np.ndarray) and len(upper_limit.shape) != 0:
                ax.plot(
                    [upper_limit[i], upper_limit[i]],
                    [min(index) - 1, max(index) + 1],
                    "r",
                    label="limit",
                )
            else:
                ax.plot(
                    [upper_limit, upper_limit],
                    [min(index) - 1, max(index) + 1],
                    "r",
                    label="limit",
                )
            ax.set_ylim(ylim)
            ax.xaxis.grid(True)

        handles, labels = axes[-1].get_legend_handles_labels()
        fig.legend(handles, labels, bbox_to_anchor=(1.0, 0.9), loc="upper left")
        label = {"L2": r"$L^2$", "Linf": r"$L^{inf}$"}
        fig.supylabel("sid")
        supxlabel = ", [" + self.db.units + "]" if self.db.units != "" else ""
        fig.supxlabel("norm" + supxlabel)
        fig.suptitle("Norm: " + label[norm_type] + "\nsid vs. norm")
        fig.tight_layout()

        return log, result, fig

    def set_tests(
        self,
        test_method: dict = {
            "std_bound": {"limits": 1.0, "n_std": 3, "nan_passed": True},
            "mean": {"limits": 1.0, "nan_passed": True},
            "sid": {"limits": 1.0, "nan_passed": True},
            "norm_L2": {"limits": 1.0},
            "norm_Linf": {"limits": 1.0},
        },
    ):
        """
        Perform tests on the data.

        Possible test methods are:
        <details>
            <summary>'std_bound'</summary>

        Test whether standard deviation is within the given limits.
        Test parameters are stored as the dict with the following keys:
        - 'limits' : float or list, default 1.0
            Limit to test standard deviation boundary. Limits may be set as:
           - one value and it will be treated as an +- interval: value -> [-value, value];
           - list of lower and upper limits: [lower_limit, upper_limit];
           - If the data has multiple columns, limits may be set for each of the column.
            That way list length must be equal to number of columns. For example, for the 3-dimensional vector with corresponding standard deviation boundaries [std_bound_1, std_bound_2, std_bound_3]:
            [[**limit_lower**, **limit_upper**], **value_1**, **value_2**] will be processed as:
            **limit_lower** < std_bound_1 < **limit_upper**,
            -**value_1** < std_bound_2 < **value_1**,
            -**value_2** < std_bound_2 < **value_2**.
        - 'n_std' : int, default 3
            The parameter specifies the number of standard deviations to be within limits.
        - 'nan_passed' : bool, default True
            If True, the NaN values of standard deviation will pass the test.

        </details>

        <details>
            <summary>'mean'</summary>

        Test whether mean is within the given limits.
        Test parameters are stored as the dict:
        - 'limits' : float or list, default 1.0
            Limit to test mean. Limits may be set as:
           - one value and it will be treated as an +- interval: value -> [-value, value];
           - list of lower and upper limits: [lower_limit, upper_limit];
           - If the data has multiple columns, limits may be set for each of the column.
            That way list length must be equal to number of columns. For example, for the 3-dimensional vector
            with corresponding mean vector [mean_1, mean_2 and mean_3]:
            [[**limit_lower**, **limit_upper**], **value_1**, **value_2**] will be processed as:
            **limit_lower** < mean_1 < **limit_upper**,
            -**value_1** < mean_2 < **value_1**,
            -**value_2** < mean_2 < **value_2**.
        - 'nan_passed' : bool, default True
            If True, the NaN values of the mean will pass the test.

        </details>

        <details>
            <summary>'std'</summary>

        Test whether standard deviation is less then the given limits.
        Test parameters are stored as the dict:
        - 'limits' : float or list, default 1.0
            Limit to test standard deviation. Limits may be set as:
           - one value;
           - If the data has multiple columns, limits may be set for each of the column.
            That way list length must be equal to number of columns. For example, for the 3-dimensional vector
            with corresponding standard deviation vectors [std_1, std_2, std_3]:
            limits = [**value_1**, **value_2**, **value_3**] will be processed as:
            std_1 < **value_1**,
            std_2 < **value_2**,
            std_2 < **value_3**.
        - 'n_std' : int, default 3
            The parameter specifies the number of standard deviations to be less then limits.
        - 'nan_passed' : bool, default True
            If True, the NaN values of the mean will pass the test.

        </details>

        <details>
            <summary>'sid'</summary>

        Test whether all simulations are within the given limits.
        Test parameters are stored as the dict:
        - 'limits' : float or list, default 1.0
            Limit to test simulation results. Limits may be set as:
           - one value and it will be treated as an +- interval: value -> [-value, value];
           - list of lower and upper limits: [lower_limit, upper_limit];
           - If the data has multiple columns, limits may be set for each of the column.
            That way list length must be equal to number of columns. For example, for the 3-dimensional vector that
            contains v1, v2, v3 columns and numbers N simulations:
            [[**limit_lower**, **limit_upper**], **value_1**, **value_2**] will be processed as:
            **limit_lower** < v1 < **limit_upper**,
            -**value_1** < v2 < **value_1**,
            -**value_2** < v3 < **value_2** for each of the N simulations.
        - 'nan_passed' : bool, default True
            If True, the NaN values will pass the test.

        </details>

        <details>
            <summary>'norm_L2'</summary>

        Test whether L2 norm of the each simulation is less than the given limit.
        Test parameters are stored as the dict:
        - 'limits' : float or list, default 1.0
            Limits on the simulation norm. Limits may be set as:
           - one value;
           - if the data has multiple columns, limits may be set for each of the column separately as a list.
            That way list length must be equal to number of the columns.

        </details>

        <details>
            <summary>'norm_Linf'</summary>

        Test whether Linf norm of the each simulation is less than the given limit.
        Test parameters are stored as the dict:
        - 'limits' : float or list, default 1.0
            Limits on the simulation norm. Limits may be set as:
           - one value;
           - if the data has multiple columns, limits may be set for each of the column separately as a list.
            That way list length must be equal to number of the columns.

        </details>

        Parameters
        ----------
        tests_method : dict
            Keys define test methods and corresponding test parameters are stored as values.

        Returns
        -------
        log : access.citros_dict.CitrosDict
            Dictionary with the test results.
        tables : dict
            Dictionary with test methods as keys and pandas.DataFrame table with results of the test as values.
        figures : dict
            Dictionary with test methods as keys and matplotlib.figure.Figure with test results as values.

        See Also
        --------
        Validation.std_bound_test, Validation.mean_test, Validation.std_test, Validation.sid_test, Validation.norm_test

        Examples
        --------
        Import Validation and CitrosDB:

        >>> from citros import CitrosDB, Validation

        From the batch 'density' of the simulation 'diffuse_nebula' from the topic 'A' download 3-dimensional 
        json-data 'data.x' that contains 'data.x.x_1', 'data.x.x_2' and 'data.x.x_3' columns,
        and column with time 'data.time'.

        >>> citros = CitrosDB(simulation = 'diffuse_nebula', batch = 'density')
        >>> df = citros.topic('A').set_order({'sid':'asc','rid':'asc'}).data(['data.x','data.time'])
        >>> print(df['data.x'])
        0          {'x_1': 0.0, 'x_2': 0.08, 'x_3': 0.047}
        1       {'x_1': 0.008, 'x_2': 0.08, 'x_3': -0.003}
        2      {'x_1': 0.016, 'x_2': 0.078, 'x_3': -0.034}
        ...

        Set 'data.time' as independent variable and 'data.x' as dependent vector.
        `method` defines the method of data preparation and index assignment: method = 'scale' - scales parameter `param_label` for each of the 'sid' to [0, 1] interval
        and interpolate data on the new scale.

        >>> V = Validation(df, data_label = 'data.x', param_label = 'data.time',
        ...                method = 'scale', num = 50, units = 'm')

        Test whether 3 standard deviation boundary is within [-0.3, 0.3] interval (treat nan values of the
        standard deviation, if they are presented, as passed the test) and L2 norm of the each simulation is less than 12.5:

        >>> logs, tables, figs = V.set_tests(test_method = {
        ...                                    'std_bound' : {'limits' : 0.3, 'n_std': 3, 'nan_passed': True},
        ...                                    'norm_L2' : {'limits' : 12.5}})
        std_bound_test: passed
        norm_test L2: passed

        Print detailed standard deviation boundary test results:

        >>> logs['std_bound'].print()
        {
         'test_param': {
           'limits': 0.3,
           'n_std': 3,
           'nan_passed': True
         },
         'data.x.x_1': {
           'passed': True,
           'pass_rate': 1.0,
           'failed': {
           },
           'nan_std': {
             49: 807.942
           }
         },
         'data.x.x_2': {
           'passed': True,
           'pass_rate': 1.0,
           'failed': {
           },
           'nan_std': {
             49: 807.942
           }
         },
         'data.x.x_2': {
           'passed': True,
           'pass_rate': 1.0,
           'failed': {
           },
           'nan_std': {
             49: 807.942
           }
          }
        }

        Print results of norm test in details:

        >>> logs['norm_L2'].print()
        {
         'test_param': {
           'limits': 12.5
         },
         'data.x.x_1': {
           'passed': True,
           'pass_rate': 1.0,
           'norm_value': {
             1: 0.39,
             2: 0.38,
             3: 0.38
           },
           'failed': []
         },
         'data.x.x_2': {
           'passed': True,
           'pass_rate': 1.0,
           'norm_value': {
             1: 0.38,
             2: 0.40,
             3: 0.40
           },
           'failed': []
         },
         'data.x.x_3': {
           'passed': True,
           'pass_rate': 1.0,
           'norm_value': {
             1: 0.12,
             2: 0.11,
             3: 0.12
           },
           'failed': []
         }
        }
        """
        methods = test_method.keys()

        logs = CitrosDict()
        figures = {}
        tables = {}

        bound_tests = {
            "std_bound": self.std_bound_test,
            "mean": self.mean_test,
            "sid": self.sid_test,
            "std": self.std_test,
        }
        norm_tests = {"norm_L2": "L2", "norm_Linf": "Linf"}

        for method in methods:
            if method in bound_tests.keys():
                logs[method], tables[method], figures[method] = bound_tests[method](
                    **test_method[method]
                )
            elif method in norm_tests.keys():
                logs[method], tables[method], figures[method] = self.norm_test(
                    norm_type=norm_tests[method], **test_method[method]
                )

        return logs, tables, figures    
    
    def _get_norm(self, norm_type="L2"):
        """
        Calculates norm.

        Parameters
        ----------
        norm_type : {'L2', 'Linf'}, default 'L2'
            Norm type.
        """
        if norm_type == "L2":
            norm = (
                self.db.data.apply(lambda x: x**2)
                .groupby("sid")
                .sum()
                .apply(lambda x: np.sqrt(x))
            )
        elif norm_type == "Linf":
            norm = (abs(self.db.data)).groupby("sid").max()
        else:
            self.log.error("Can not recognize the norm type, the allowed types are 'L2' and 'Linf'")
            norm = None
        return norm

    def _get_mean_std_log(self, init_param, result):
        """
        Write log for std and mean bound tests.

        Parameters
        ----------
        init_param : dict
            Initial parameters to write in the log.
        result : pandas.DataFrame
            Table with results of the test.

        Returns
        -------
        log : access.citros_dict.CitrosDict
            Dictionary with information for each column: 'passed' (True or False), 'pass_rate', 'failed' (indexes and x values of the
            points that fail the test).
        """
        log = CitrosDict()

        # init parameters
        log["test_param"] = CitrosDict(init_param)

        # calculate pass rate (how many points pass)
        try:
            pass_rate = CitrosDict(
                (
                    result[self.db.data.columns].apply(pd.Series.value_counts).loc[True]
                    / len(result)
                )
                .fillna(0)
                .apply(round, ndigits=3)
            )
        except KeyError:
            # in case all points failed test and there is no True values
            pass_rate = CitrosDict()
            for col in self.db.data.columns:
                pass_rate[col] = 0.0

        for col in self.db.data.columns:
            log[col] = CitrosDict()
            log[col]["passed"] = True if result[col].all() else False
            log[col]["pass_rate"] = pass_rate[col]
            log[col]["failed"] = CitrosDict(
                result[self.db.x_label]
                .loc[result.index[result[col] == False]]
                .to_dict()
            )
            # log[col]['table'] = result[[col]]

        return log

    def _plot_bounds(self, result, lower_limit, upper_limit, fig):
        """
        Add bound lines on the plot.

        Parameters
        ----------
        result : pandas.DataFrame
            Table with results of the test.
        lower_limit : numpy.ndarray
            Lower limit(s).
        upper_limit : numpy.ndarray
            Upper limit(s).
        fig : matplotlib.figure.Figure
            Figure to plot bound lines on.
        """
        axes = fig.axes
        for i, ax in enumerate(axes):
            if isinstance(lower_limit, np.ndarray) and len(lower_limit.shape) != 0:
                ax.plot(
                    [min(result[self.db.x_label]), max(result[self.db.x_label])],
                    [lower_limit[i], lower_limit[i]],
                    "r",
                )
            elif isinstance(lower_limit, pd.DataFrame) and len(lower_limit.shape) != 0:
                ax.plot(result[self.db.x_label], lower_limit, "r")
            else:
                ax.plot(
                    [min(result[self.db.x_label]), max(result[self.db.x_label])],
                    [lower_limit, lower_limit],
                    "r",
                )

            if isinstance(upper_limit, np.ndarray) and len(upper_limit.shape) != 0:
                ax.plot(
                    [min(result[self.db.x_label]), max(result[self.db.x_label])],
                    [upper_limit[i], upper_limit[i]],
                    "r",
                )
            elif isinstance(upper_limit, pd.DataFrame) and len(upper_limit.shape) != 0:
                ax.plot(result[self.db.x_label], upper_limit, "r")
            else:
                ax.plot(
                    [min(result[self.db.x_label]), max(result[self.db.x_label])],
                    [upper_limit, upper_limit],
                    "r",
                )

        line = Line2D([0], [0], label="test bounds", color="r")
        handles, labels = axes[-1].get_legend_handles_labels()
        fig.legend(
            handles + [line],
            labels + ["test bounds"],
            bbox_to_anchor=(1.0, 0.94),
            loc="upper left",
        )
        fig.legends.pop(0)
        fig.tight_layout()
 
    def _get_limit_values(self, limits, data_length):
        """
        Get lower and upper limits from `limits`.

        Parameters
        ----------
        limits : int or float or list or tuple.
        data_length : int
            Length of the data.

        Returns
        -------
        lower_limit : numpy.ndarray
            Lower limit(s).
        upper_limit : numpy.ndarray
            Upper limit(s).
        """
        if isinstance(limits, (list, tuple)):
            # [0.1]  [0.1, 0.2]  [(0.1, 0.2), (0.1, 0.2)]  [0.1, (0.1, 0.2)]

            if len(limits) == 1:
                # [0.1]
                try:
                    lower_limit = -limits[0]
                    upper_limit = limits[0]
                except TypeError:
                    self.log.error("Could not resolve the limits")
                    return None, None

            elif len(limits) == 2 and not any(
                map(lambda x: isinstance(x, (list, tuple)), limits)
            ):
                # [0.1, 0.2]
                lower_limit = limits[0]
                upper_limit = limits[1]

            else:
                if len(limits) != data_length:
                    self.log.error("`limits` length does not match the number of data columns.")
                    return None, None
                else:
                    # [(0.1, 0.2), (0.1, 0.2)]  [0.1, (0.1, 0.2)]  [0.1, 0.2, 0.3]  [(0.1, 0.2), 0.1, (10, 100)]  [(0.1, 0.2), (0.1, 0.2), (10, 100)]
                    lower_limit = []
                    upper_limit = []

                    for i in range(data_length):
                        if isinstance(limits[i], (list, tuple)) and len(limits[i]) != 1:
                            # [(0.1, 0.2),...
                            lower_limit.append(limits[i][0])
                            upper_limit.append(limits[i][1])
                        elif isinstance(limits[i], (list, tuple)):
                            # [(0.1),...
                            lower_limit.append(-limits[i][0])
                            upper_limit.append(limits[i][0])
                        else:
                            # [0.1,...
                            lower_limit.append(-limits[i])
                            upper_limit.append(limits[i])
        else:
            # single +-value, int or float
            lower_limit = -limits
            upper_limit = limits

        return np.array(lower_limit), np.array(upper_limit)

    def _get_1D_limit(self, limits, data_length):
        """
        Get limit on norm from `limits`.

        Parameters
        ----------
        limits : int or float or list or tuple.
        data_length : int
            Length of the data.

        Returns
        -------
        norm_limit : numpy.ndarray
            Limit(s).
        """
        if isinstance(limits, (list, tuple)):
            # [0.1]  [0.1, 0.2, 0.3]

            if len(limits) == 1:
                # [0.1]
                norm_limit = limits[0]
            else:
                if len(limits) != data_length:
                    self.log.error("`limits` length does not match the number of data columns.")
                    return None
                else:
                    # [0.1, 0.2, 0.3]
                    norm_limit = limits
        else:
            # single value, int or float
            norm_limit = limits

        return np.array(norm_limit)
