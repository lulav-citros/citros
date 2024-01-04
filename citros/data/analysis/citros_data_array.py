import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from itertools import cycle
from sklearn.neural_network import MLPRegressor
from sklearn.mixture import GaussianMixture
from sklearn import preprocessing
from gmr import GMM
from numpy.typing import ArrayLike
from typing import Optional
import matplotlib.figure
from .citros_data import CitrosData

class CitrosDataArray:
    """
    Store CitrosData objects in a "dbs" attribute for regression analysis.

    Parameters
    ----------
    dbs : list
        list of CitrosData objects
    """

    _debug_flag = False

    def __init__(self, dbs = None):

        if isinstance(dbs, list):
            self.dbs = dbs
        elif isinstance(dbs, CitrosData):
            self.dbs = [dbs]
        elif dbs is None:
            self.dbs = []
    
    def add_db(self, db: CitrosData):
        """
        Add one CitrosData object to CitrosDataArray.

        Parameters
        ----------
        db : citros_data_analysis.error_analysis.citros_data.CitrosData
            CitrosData object to add to storage.
        """
        if isinstance(db, CitrosData):
            self.dbs.append(db)
        else:
            print('expected CitrosData object, but {} was given'.format(type(db)))
    
    def add_dbs(self, dbs: list):
        """
        Add list of CitrosData objects to CitrosDataArray.

        Parameters
        ----------
        dbs : list
            list of CitrosData objects to add to storage.
        """
        for db in dbs:
            self.add_db(db)

    def drop_db(self, value: int):
        """
        Remove CitrosData object from CitrosDataArray.

        If `value` is an int, then removes by index, 
        if `value` is a CitrosData object, then removes it if it exists in CitrosDataArray.

        Parameters
        ----------
        value : int or citros_data_analysis.error_analysis.citros_data.CitrosData
            Object or index of object to remove.
        """
        if isinstance(value, int):
            try:
                self.dbs.pop(value)
            except IndexError:
                print('index is out of range')
        elif isinstance(value, CitrosData):
            try:
                self.dbs.remove(value)
            except ValueError:
                print('object is not in CitrosDataArray')

    def get_prediction(self, parameters: dict, method: str = 'poly', n_poly: int = 2, activation: str = 'relu', 
                       max_iter: int = 500, solver: str = 'lbfgs', hidden_layer_sizes: ArrayLike = (10,), 
                       alpha: float = 1e-16, fig: Optional[matplotlib.figure.Figure] = None, show_fig: bool = False, 
                       return_fig: bool = False, **kwargs):
        """
        Show the predictions based on the results of the regression solution, neural net or gaussian mixture model.

        Parameters
        ----------
        parameters : dict
            Names of the independent parameters and their values to calculate the prediction.
        method : str or list of str, default 'poly'
            - 'poly' - the polynomial regression.
            - 'neural_net' - the solution is finding based on [sklearn.neural_network.MLPRegressor](https://scikit-learn.org/stable/modules/generated/sklearn.neural_network.MLPRegressor.html).
            - 'gmm' - the gaussian mixture model is built and used for the prediction.
        n_poly : int, default 2
            Only used if `method` = 'poly'.
            The highest degree of the polynomial (1 for linear, 2 for quadratic, etc).
        activation : {'relu', 'identity', 'logistic' or 'tanh'}, default 'relu'
            Only used if `method` = 'neural_net'.
            Activation function for the hidden layer, see sklearn.neural_network.MLPRegressor
        max_iter : int, default 500
            Only used if `method` = 'neural_net'.
            Maximum number of iterations.
        solver : {'lbfgs', 'sgd', 'adam'}, default 'lbfgs'
            Only used if `method` = 'neural_net'.
            The solver for weight optimization.
        hidden_layer_sizes : array-like of shape(n_layers - 2,), default=(10,)
            Only used if `method` = 'neural_net'.
            The ith element represents the number of neurons in the ith hidden layer.
        alpha : float, default 1e-16
            Only used if `method` = 'gmm'.
            Value of the covariance element of parameters.
        fig : matplotlib.figure.Figure, optional
            figure to plot on. If None, then the new one is created.
        show_fig : bool, default True
            If the figure will be shown.
        return_fig : bool, default False
            If True, the figure and ax (or list of ax) will be returned.

        Other Parameters
        ----------------
        kwargs : dict, optional
            Other keyword arguments for `method` = 'neural_net', see [sklearn.neural_network.MLPRegressor](https://scikit-learn.org/stable/modules/generated/sklearn.neural_network.MLPRegressor.html).

        Returns
        -------
        result : pandas.DataFrame
            Predicted table
        fig : matplotlib.figure.Figure
            if `return_fig` set to True
        ax : matplotlib.axes.Axes or list of matplotlib.axes.Axes
            if `return_fig` set to True

        Examples
        --------
        Create CitrosDataArray object:

        >>> from citros.citros_data_analysis import error_analysis as analysis
        >>> db_array = analysis.CitrosDataArray()

        Let's assume that for the topic 'A' from the batch 'star' of the simulation 'simulation_galaxy' we have simulations 
        for the four different values of the some parameter 't', that is written in json-data column 'data.t'. 
        To get list of the 'data.t' parameters get_unique_values() method may be used:

        >>> from citros.citros_data_analysis import data_access as da
        >>> citros = da.CitrosDB(simulation = 'simulation_galaxy', batch = 'star')
        >>> list_t = citros.topic('A').get_unique_values('data.t')
        >>> print(list_t)
        [-1.5, 0, 2.5, 4]

        Let's find prediction for the values of the 'data.x.x_1' json-column for the case when 'data.t' equals 1.
        Query data for each of these parameter values, set it as parameter, assign indexes over 'data.time' axis to set
        correspondence between different simulations and pass the result to CitrosDataArray that we created:

        >>> for t in list_t:
        ...     #query data
        ...     df = citros.topic('A')\\
        ...                .set_filter({'data.t': [t]})\\
        ...                .data(['data.x.x_1', 'data.time', 'data.t'])
        ...
        ...     #create CitrosData object and set 'data.t' as a parameter.
        ...     dataset = analysis.CitrosData(df,  
        ...                                  data_label=['data.x.x_1'],
        ...                                  units = 'm', 
        ...                                  parameter_label = ['data.t'])
        ...
        ...     #scale over 'data.time'
        ...     db_sc = dataset.scale_data(n_points = 100, 
        ...                                param_label = 'data.time', 
        ...                                show_fig = False)
        ...
        ...     #store in CitrosDataArray by add_db() method
        ...     db_array.add_db(db_sc)

        Get the prediction with 'poly' method:

        >>> result = db_array.get_prediction(parameters = {'data.t': 1},
        ...                                  method = 'poly', 
        ...                                  n_poly = 2,
        ...                                  show_fig = True)
        >>> print(result)
            data.time	data.x.x_1
        0	0.000000	1.155301
        1	0.010101	1.145971
        2	0.020202	1.232255
        ...
        """
        slice_id_list = self.dbs[0].data.index.get_level_values(0).to_list()
        
        if not isinstance(method, list):
            method = [method]

        stat_df = pd.DataFrame()
        x_df = pd.DataFrame()
        cov_df = pd.DataFrame()
        for i in range(len(self.dbs)):
            stat = self.dbs[i].get_statistics(return_format = 'pandas')
            x_name = stat.columns[0]
            stat_df = pd.concat([stat_df, stat['mean'].rename('mean_'+str(i))], axis =1)
            cov_df = pd.concat([cov_df, stat['covar_matrix'].rename('cov_'+str(i))], axis =1)
            x_df = pd.concat([x_df, stat[self.dbs[i].x_label]], axis =1)
        stat_df.sort_index(inplace=True)
        x_df.sort_index(inplace=True)
        x_df = x_df.mean(axis = 1)
        N_ax = self.dbs[0].data_dim
        slice_id_list = stat_df.index.to_list()

        if show_fig or return_fig or fig is not None:
            if fig is None:
                fig, ax = plt.subplots(nrows = N_ax, ncols = 1,figsize=(6, 6))
            else:
                ax = []
                for i in range(1,N_ax+1):
                    ax.append(fig.add_subplot(N_ax, 1, i))
            for i in range(len(self.dbs)):
                filter_db = stat_df['mean_'+str(i)].notna()
                lab = ', '.join([p + ' = ' + str(self.dbs[i].parameters[p]) for p in parameters.keys()])
                try:
                    for n in range(N_ax):
                        ax[n].plot(x_df[filter_db], stat_df['mean_'+str(i)][filter_db].apply(lambda x: x[n]), '-', linewidth = 0.9, label = lab)
                        ax[n].grid(True)
                except:
                    ax.plot(x_df[filter_db], stat_df['mean_'+str(i)][filter_db], '-', linewidth = 0.7, label = lab)
                    ax.grid(True)

            lab_new = ', '.join([k + ' = ' + str(v) for k, v in parameters.items()])

            color_list = cycle(['k','darkred','rebeccapurple'])

        predicted_tables = []
        for method_step in method:
            mu_calculated = self._make_prediction(method_step, stat_df, cov_df, slice_id_list, n_poly, parameters,\
                                            N_ax, hidden_layer_sizes, activation, max_iter, solver, alpha, **kwargs)
            predicted_tables.append(pd.concat([x_df, pd.DataFrame(mu_calculated)], axis = 1))
            predicted_tables[-1].columns = [x_name] + list(self.dbs[0].data.columns)

            if show_fig or return_fig:
                color = next(color_list)
                try:
                    for n in range(N_ax):
                        ax[n].plot(x_df, mu_calculated[:,n],'-', color = color, linewidth = 2, label = lab_new+',\n' + method_step)
                        ax[n].set_ylabel(self.dbs[0].data.columns[n]+', [' + self.dbs[0].units+']')
                except:
                    ax.plot(x_df, mu_calculated,'-', linewidth = 2, color = color, label = lab_new+',\n' + method_step)
                    ax.set_ylabel(self.dbs[0].data.columns[0]+', [' + self.dbs[0].units+']')

        if show_fig or return_fig or fig is not None:
            try:
                handles, labels = ax[-1].get_legend_handles_labels()
            except:
                handles, labels = ax.get_legend_handles_labels()
            fig.supxlabel(self.dbs[0].x_label)
            # fig.supylabel(self.dbs[0].type+', [' + self.dbs[i].units+']')
            fig.suptitle('Prediction plot')
            fig.legend(handles, labels, bbox_to_anchor=(1.0, 0.94),loc ='upper left')
            fig.tight_layout()
        if show_fig:
            fig.show()

        if len(predicted_tables) == 1:
            predicted_tables = predicted_tables[0]
        if return_fig:
            return  predicted_tables, fig, ax
        else:
            return predicted_tables
    
    def _make_prediction(self, method, stat_df, cov_df, slice_id_list, n_poly, parameters, N_ax, hidden_layer_sizes,\
                        activation, max_iter, solver, alpha, **kwargs):
        """
        Inner function to calculate prediction for mean values by one of the methods.

        Parameters
        ----------
        method : str or list of str, default 'poly'
            - If the method is 'poly', the polynomial regression is solved.
            - If the method is 'neural_net', the solution is finding by sklearn.neural_network.MLPRegressor.
            - If the method is 'gmm', the gaussian mixture model is built and used for the prediction.
        stat_df : pandas.DataFrame
            DataFrame with prepared means values.
        cov_df : pandas.DataFrame
            DataFrame with prepared covariance matrixes.
        slice_id_list : list
            List of the indexes.
        n_poly : int, default 2
            Only used if method = 'poly'.
            The highest degree of the polynomial (1 for linear, 2 for quadratic, etc).
        parameters : dict
            Names of the independent parameters and their values to calculate the prediction.
        N_ax : int
            Number of the axis (equals dimension of the data).
        hidden_layer_sizes : array-like of shape(n_layers - 2,), default=(10,)
            Only used if method = 'neural_net'.
            The ith element represents the number of neurons in the ith hidden layer.
        activation : str, default 'relu'
            Only used if method = 'neural_net'.
            Activation function for the hidden layer, see sklearn.neural_network.MLPRegressor.
        max_iter : int, default 500
            Only used if method = 'neural_net'.
            Maximum number of iterations.
        solver : str, default 'lbfgs'
            Only used if method = 'neural_net'.
            The solver for weight optimization.
        alpha : float, default 1e-16
            Only used if method = 'gmm'.
            Value of the covariance element for parameters.
        **kwargs : dict, optional
            Other keyword arguments when method = 'neural_net', see [sklearn.neural_network.MLPRegressor](https://scikit-learn.org/stable/modules/generated/sklearn.neural_network.MLPRegressor.html).

        Returns
        -------
        out : numpy.ndarray
            Predicted mean values.
        """
        mu_calculated = []
        if method == 'poly':
            P_new = [1,] + [p**i for i in range(1, n_poly+1) for p in parameters.values()]
            P = np.array(list(map(lambda x: [x.parameters[p]**i for i in range(1, n_poly+1) for p in parameters.keys()], self.dbs)))
            P = np.append(np.array([[1]*len(self.dbs)]).T, P, axis = 1)
            for slice_id in slice_id_list:
                mu = np.array(stat_df.loc[slice_id].to_list())
                try:
                    mu_param = self._fit_regression(P, mu)
                    mu_calculated.append(self._calculate_regression(mu_param, P_new))
                except:
                    # mu_calculated.append([None]*N_ax if N_ax > 1 else None)
                    mu_calculated.append(np.array([np.nan]*N_ax))

        elif method == 'neural_net':
            P_new = np.array(list(parameters.values())).reshape(1,-1)
            P=np.array([[db.parameters[k] for k in parameters.keys()] for db in self.dbs])
            for slice_id in slice_id_list:
                mu = np.array(stat_df.loc[slice_id].to_list())
                pr = []
                try:
                    for j in range(mu.shape[1]):
                        nn = MLPRegressor(hidden_layer_sizes=hidden_layer_sizes, activation=activation, \
                            max_iter=max_iter, solver=solver, verbose=False, **kwargs)
                        mean = mu[:,j].mean()
                        std = mu[:,j].std()
                        try:
                            X = ((mu[:,j] - mean)/std)
                            n = nn.fit(P, X)
                            pr.append(nn.predict(P_new)[0]*std+mean)
                        except ZeroDivisionError:
                            n = nn.fit(P, mu[:,j])
                            pr.append(nn.predict(P_new)[0])
                    mu_calculated.append(np.array(pr))
                except Exception as e:
                    if CitrosDataArray._debug_flag:
                        raise e
                    mu_calculated.append(np.array([np.nan]*N_ax))

        elif method == 'gmm':
            P=np.array([[db.parameters[k] for k in parameters.keys()] for db in self.dbs])
            P_new = np.array(list(parameters.values())).reshape(-1,P.shape[1])
            for slice_id in slice_id_list:
                mu = np.array(stat_df.loc[slice_id].to_list())
                cov = np.array(cov_df.loc[slice_id].to_list())
                X = np.c_[mu, P]
                X_cov =[]
                for cov_element in cov:
                    X_cov.append(np.r_[np.c_[cov_element,np.ones((cov_element.shape[0],P.shape[1]))*alpha],np.ones((P.shape[1],cov_element.shape[1]+P.shape[1]))*alpha])
                X_cov = np.array(X_cov)
                try:
                    gmm_sklearn = GaussianMixture(n_components=len(self.dbs), covariance_type = 'full', verbose=False)
                    gmm_sklearn.fit(X)
                    gmm = GMM(
                        n_components=len(self.dbs), priors=gmm_sklearn.weights_, means=gmm_sklearn.means_,
                        covariances=X_cov)
                    pr_index = [i for i in range(N_ax,N_ax+P.shape[1])]
                    mu_calculated.append(gmm.predict(pr_index, P_new)[0])
                except Exception as e:
                    if CitrosDataArray._debug_flag:
                        raise e
                    # mu_calculated.append([None]*N_ax if N_ax > 1 else None)
                    mu_calculated.append(np.array([np.nan]*N_ax))
        else:
            print('there is no method called "{}". Try "poly", "neural_net" or "gmm".')
        return np.array(mu_calculated)
    
    def _data_for_regression(self, slice_id):
        """
        Prepare data for the regression fitting.

        Parameters
        ----------
        slice_id : int
            id at which the data is sliced.

        Returns
        -------
        mu : numpy.ndarray
            array of the mean values.
        sigma : numpy.ndarray
            array of the unique elements of the covariance matrix (diagonal and upper half).
        shape : tuple
            shape of the covariance matrix.
        """
        mu = []
        sigma = []
        for db in self.dbs:
            stat = db.get_statistics(return_format = 'pandas')
            mu.append(stat['mean'].loc[slice_id])
            covar = stat['covar_matrix'].loc[slice_id]
            s = []
            for i in range(len(covar)):
                for j in range(i, len(covar)):
                    s.append(stat['covar_matrix'].loc[slice_id][i,j])
            sigma.append(s)
        sigma = np.array(sigma)
        mu = np.array(mu)
        return mu, sigma, covar.shape

    def _fit_regression(self, P, y):
        """
        Fit the regression.

        Calculates the parameters x that solves y = Px.

        Parameters
        ----------
        P : numpy.ndarray
            Matrix of the coefficients.
        y : numpy.ndarray
            Vector of the dependent variables.

        Returns
        -------
        out : numpy.ndarray
            Vector of the regression parameters. 
        """
        x, res, rnk, s = np.linalg.lstsq(P, y, rcond = None) 
        return x

    def _get_regression_coef(self, slice_id, n_poly, parameters = None):
        """
        Calculate coefficients for the regression for mean values and for covariance matrix.

        Parameters
        ----------
        slice_id : int
            id at which the data is sliced.
        n_poly : int
            The highest degree of the polynomial (1 for linear, 2 for quadratic, etc)
        parameters : list
            Names of the independent parameters. If not specified, all parameters are used.

        Returns
        -------
        mu_param : numpy.ndarray
            Coefficients of the regression for mean value.
        sigma_param : numpy.ndarray
            Coefficients of the regression for covariance matrix.
            The shape is equals the shape of the covariance matrix.
        """
        if parameters is None:
            parameters = self.dbs[0].parameters.keys()
        mu, sigma, covar_shape = self._data_for_regression(self.dbs, slice_id)
        P = np.array(list(map(lambda x: [x.parameters[p]**i for i in range(1, n_poly+1) for p in parameters],self.dbs)))
        P = np.append(np.array([[1]*len(self.dbs)]).T, P, axis = 1)
        mu_param = self._fit_regression(P, mu) 
        res_sigma = self._fit_regression(P, sigma)
        
        sigma_param = []
        for res in res_sigma:
            k=0
            sigma_elem = np.empty(covar_shape)
            for i in range(covar_shape[0]):
                for j in range(i,covar_shape[0]):
                    sigma_elem[i,j] = res[k]
                    k+=1
                for j in range(i):
                    sigma_elem[i,j] = sigma_elem[j,i]
            sigma_param.append(sigma_elem)
            
        return mu_param, np.array(sigma_param)

    def _calculate_regression(self, x_param, P):
        """
        Calculate x_param * P.

        Function for checking the results of the regression algorithm.

        Parameters
        ----------
        x_param : array-like
            Parameters of the regression.
        P : array-like
            The vector of the coefficients.
        
        Returns
        -------
        out : float
            The result of the summing.
        """
        x_calc = 0
        for i in range(len(x_param)):
            x_calc = x_calc + P[i]*x_param[i]
        return x_calc