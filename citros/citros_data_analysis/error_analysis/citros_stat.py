import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from typing import Optional
import matplotlib.figure

class CitrosStat:
    """
    Object to store statistics.

    Parameters
    ----------
    F : pandas.DataFrame
        Table with statistics.
    labels : array-like
        Labels of the data columns.
    x_label : str
        Label of the independent variable.

    Attributes
    ----------
    x : pandas.DataFrame
        Table with independent variable.
    mean : pandas.DataFrame
        Table with mean values. If statistics was collected for a vector, columns correspond to vector elements.
    covar_matrix: pandas.DataFrame
        Table with the covariance matrixes. If statistics was collected for a vector, columns correspond to vector elements.
    sigma : pandas.DataFrame
        Table with the square roots of the diagonal elements of the covariance matrix. 
        If statistics was collected for a vector, columns correspond to vector elements.
    """

    def __init__(self, F, labels, x_label):
        self.x = pd.DataFrame(F[x_label])
        self.mean = pd.DataFrame(columns = labels)
        self.covar_matrix = F['covar_matrix']
        self.sigma = self.std = pd.DataFrame(columns = labels)
        for i in range(len(labels)):
            self.mean[labels[i]] = F['mean'].apply(lambda x: x[i])
            self.sigma[labels[i]] = F['sigma'].apply(lambda x: x[i])

    def to_pandas(self):
        """
        Convert CitrosStat object back to pandas DataFrame.

        Returns
        -------
        df : pandas.DataFrame
            Converted to pandas DataFrame.
        """
        result = pd.concat([self.x, self.mean.apply(lambda x: np.array([x[col] for col in self.mean.columns]), axis = 1),
            self.covar_matrix, self.sigma.apply(lambda x: np.array([x[col] for col in self.mean.columns]), axis = 1)], 
            axis = 1)
        result.columns = [result.columns[0], 'mean', 'covar_matrix', 'sigma']
        return result
    
    def plot(self, fig: Optional[matplotlib.figure.Figure] = None, show_fig: bool = True, return_fig: bool = False, 
             n_std: int = 3, fig_title: str = 'Statistics', std_color: str = 'r'):
        '''
        Plot mean values and standard deviations.

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
            Error interval to display, specified in standard deviations.
        fig_title : str, default 'Statistics'
            Title of the figure.
        std_color : str, default 'r'
            Color for displaying standard deviations, red by default.

        Returns
        -------
        fig : matplotlib.figure.Figure
            if `return_fig` set to True
        ax : list of matplotlib.axes.Axes
            if `return_fig` set to True
        '''
        if (not show_fig) and (not return_fig):
            return

        N = len(self.mean.columns)

        if fig is None:
            fig, axes = plt.subplots(nrows = N, ncols = 1,figsize=(6, 6))
            if N == 1:
                axes = [axes]
        else:
            axes = []
            for i in range(1,N+1):
                axes.append(fig.add_subplot(N,1,i))

        for i, ax in enumerate(axes):
            filter_st = self.sigma.iloc[:, i].notna()

            ax.plot(self.x, self.mean.iloc[:, i], 'k-', linewidth = 2, label = 'mean')
            if n_std is not None:
                ax.plot(self.x[filter_st], self.mean.iloc[:, i][filter_st] + n_std*self.sigma.iloc[:, i][filter_st],
                        '-', color = std_color, label = r'$\pm$'+str(n_std)+ r'$\sigma$')
                ax.plot(self.x[filter_st], self.mean.iloc[:, i][filter_st] - n_std*self.sigma.iloc[:, i][filter_st], 
                        '-', color = std_color)
            ax.grid(True)
            ax.set_ylabel(self.mean.columns[i])
        handles, labels = axes[-1].get_legend_handles_labels()

        fig.suptitle(fig_title)
        fig.supylabel(self.x.columns[0])
        fig.legend(handles, labels, bbox_to_anchor=(1.0, 0.94),loc ='upper left')
        fig.tight_layout()

        if show_fig:
            fig.show()
        if return_fig:
            return fig, ax