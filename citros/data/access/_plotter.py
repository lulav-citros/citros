import pandas as pd
from mpl_toolkits import mplot3d
from matplotlib.lines import Line2D
import matplotlib.pyplot as plt
import numpy as np

from ..analysis import CitrosData, CitrosDataArray, CitrosStat

# from citros import CitrosData, CitrosDataArray, CitrosStat

from itertools import cycle


class _Plotter:
    def plot_graph(
        self,
        df,
        x_label,
        y_label,
        ax,
        legend,
        title,
        set_x_label,
        set_y_label,
        remove_nan,
        inf_vals,
        *args,
        **kwargs,
    ):
        """
        Plot graph '`y_label` vs. `x_label`' for each sid, where `x_label` and `y_label`
        are the labels of columns of the pandas.DataFrame `df`.

        Parameters
        ----------
        df : pandas.DataFrame
            Data table.
        x_label : str
            Label of the column to plot along x-axis.
        y_label : str
            Label of the column to plot along y-axis.
        *args : Any
            Additional arguments to style lines, set color, etc,
            see [matplotlib.axes.Axes.plot](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.plot.html)
        ax : matplotlib.axes.Axes
            Figure axis to plot on. If not specified, the new pair of fig, ax will be created.
        legend : bool, default True
            If True, show the legend with sids.
        title : str
            Set title of the plot.
        set_x_label : str, default None
            Label to set to the x-axis. If None, label is set according to `x_label`.
        set_y_label : str, default None
            Label to set to the y-axis. If None, label is set according to `y_label`.
        remove_nan : bool, default True
            If True, NaN values will be removed before plotting.
        inf_vals : None or float, default 1e308
            If specified, all values that exceed the provided value in absolute terms will be removed before plotting.
            If this functionality is not required, set inf_vals = None.

        Returns
        -------
        fig : matplotlib.figure.Figure
            Created figure if `ax` is not passed.
        ax : matplotlib.axes.Axes
            Created axis if `ax` is not passed.

        Other Parameters
        ----------------
        **kwargs
            Other keyword arguments, see [matplotlib.axes.Axes.plot](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.plot.html)
        """
        return_flag = False
        if ax is None:
            return_flag = True
            fig, ax = plt.subplots(figsize=(6, 6))

        if remove_nan:
            flag = df[x_label].notna() & df[y_label].notna()
        else:
            flag = pd.Series(data=[True] * len(df))
        if inf_vals is not None:
            flag = flag & (
                ((abs(df[x_label]) - inf_vals) < 0)
                & ((abs(df[y_label]) - inf_vals) < 0)
            )

        missing_col = False
        for col in ["sid", "rid"]:
            if col not in df.columns:
                missing_col = True
                print(f'column "{col}" must be in the DataFrame `df`')
        if missing_col:
            return None

        df_copy = df[flag].copy()

        try:
            df_copy.sort_values(by=["sid", "rid"], axis=0, inplace=True)
        except:
            pass
        df_copy.set_index("sid", inplace=True)
        sid_list = list(set(df_copy.index))
        for s in sid_list:
            ax.plot(
                df_copy.loc[s][x_label],
                df_copy.loc[s][y_label],
                label=str(s),
                *args,
                **kwargs,
            )

        if set_x_label is None:
            ax.set_xlabel(x_label)
        else:
            ax.set_xlabel(set_x_label)
        if set_y_label is None:
            ax.set_ylabel(y_label)
        else:
            ax.set_ylabel(set_y_label)
        ax.grid()
        if title is not None:
            ax.set_title(title)
        if legend:
            ax.legend(title="sid", loc="best")

        if return_flag:
            return fig, ax
        else:
            return None

    def plot_3dgraph(
        self,
        df,
        x_label,
        y_label,
        z_label,
        ax,
        scale,
        legend,
        title,
        set_x_label,
        set_y_label,
        set_z_label,
        remove_nan,
        inf_vals,
        *args,
        **kwargs,
    ):
        """
        Plot 3D graph '`z_label` vs. `x_label` and `y_label`' for each sid, where `x_label`, `y_label` and `z_label`
        are the labels of columns of the pandas.DataFrame `df`.

        Parameters
        ----------
        df : pandas.DataFrame
            Data table.
        x_label : str
            Label of the column to plot along x-axis.
        y_label : str
            Label of the column to plot along y-axis.
        *args : Any
            Additional arguments to style lines, set color, etc,
            see [matplotlib.axes.Axes.plot](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.plot.html)
        ax : matplotlib.axes.Axes
            Figure axis to plot on. If not specified, the new pair of fig, ax will be created.
        scale : bool, default True
            Specify whether the axis range should be the same for all axes.
        legend : bool, default True
            If True, show the legend with sids.
        title : str
            Set title of the plot.
        set_x_label : str, default None
            Label to set to the x-axis. If None, label is set according to `x_label`.
        set_y_label : str, default None
            Label to set to the y-axis. If None, label is set according to `y_label`.
        set_z_label : str, default None
            Label to set to the z-axis. If None, label is set according to `z_label`.
        remove_nan : bool, default True
            If True, NaN values will be removed before plotting.
        inf_vals : None or float, default 1e308
            If specified, all values that exceed the provided value in absolute terms will be removed before plotting.
            If this functionality is not required, set inf_vals = None.

        Returns
        -------
        fig : matplotlib.figure.Figure
            Created figure if `ax` is not passed.
        ax : matplotlib.axes.Axes
            Created axis if `ax` is not passed.

        Other Parameters
        ----------------
        **kwargs
            Other keyword arguments, see [matplotlib.axes.Axes.plot](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.plot.html)
        """
        return_flag = False
        if ax is None:
            return_flag = True
            fig = plt.figure(figsize=(6, 6))
            ax = fig.add_subplot(111, projection="3d")

        if remove_nan:
            flag = df[x_label].notna() & df[y_label].notna() & df[z_label].notna()
        else:
            flag = pd.Series(data=[True] * len(df))
        if inf_vals is not None:
            flag = flag & (
                ((abs(df[x_label]) - inf_vals) < 0)
                & ((abs(df[y_label]) - inf_vals) < 0)
                & ((abs(df[z_label]) - inf_vals) < 0)
            )

        missing_col = False
        for col in ["sid", "rid"]:
            if col not in df.columns:
                missing_col = True
                print(f'column "{col}" must be in the DataFrame `df`')
        if missing_col:
            return None

        df_copy = df[flag].copy()

        try:
            df_copy.sort_values(by=["sid", "rid"], axis=0, inplace=True)
        except:
            pass
        df_copy.set_index("sid", inplace=True)
        sid_list = list(set(df_copy.index))
        for s in sid_list:
            ax.plot(
                df_copy.loc[s][x_label],
                df_copy.loc[s][y_label],
                df_copy.loc[s][z_label],
                label=str(s),
                *args,
                **kwargs,
            )

        if set_x_label is None:
            ax.set_xlabel(x_label)
        else:
            ax.set_xlabel(set_x_label)
        if set_y_label is None:
            ax.set_ylabel(y_label)
        else:
            ax.set_ylabel(set_y_label)
        if set_z_label is None:
            ax.set_zlabel(z_label)
        else:
            ax.set_zlabel(set_z_label)
        if title is not None:
            ax.set_title(title)
        if legend:
            ax.legend(title="sid", loc="best")
        if scale:
            min_limit = min([df_copy[col].min() for col in [x_label, y_label, z_label]])
            max_limit = max([df_copy[col].max() for col in [x_label, y_label, z_label]])
            ax.axes.set_xlim3d(min_limit, max_limit)
            ax.axes.set_ylim3d(min_limit, max_limit)
            ax.axes.set_zlim3d(min_limit, max_limit)
        if return_flag:
            return fig, ax
        else:
            return None

    def multiple_y_plot(
        self,
        df,
        x_label,
        y_labels,
        fig,
        legend,
        title,
        set_x_label,
        set_y_label,
        remove_nan,
        inf_vals,
        *args,
        **kwargs,
    ):
        """
        Plot a series of vertically arranged graphs 'y vs. `x_label`', with the y-axis labels
        specified in the `y_labels` parameter.

        Different colors correspond to different sids.

        Parameters
        ----------
        df : pandas.DataFrame
            Data table.
        x_label : str
            Label of the column to plot along x-axis.
        y_labels : list of str
            Labels of the columns to plot along y-axis.
        *args : Any
            Additional arguments to style lines, set color, etc,
            see [matplotlib.axes.Axes.plot](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.plot.html)
        fig : matplotlib.figure.Figure, optional
            If None, a new Figure will be created.
        legend : bool, default True
            If True, show the legend with sids.
        title : str
            Set title of the plot.
        set_x_label : str, default None
            Label to set to the x-axis. If None, label is set according to `x_label`.
        set_y_label : list of str, default None
            Labels to set to the y-axis. If None, label is set according to `y_labels`.
        remove_nan : bool, default True
            If True, NaN values will be removed before plotting.
        inf_vals : None or float, default 1e308
            If specified, all values that exceed the provided value in absolute terms will be removed before plotting.
            If this functionality is not required, set inf_vals = None.

        Returns
        -------
        fig : matplotlib.figure.Figure
            Created figure if `fig` is not passed.
        ax : numpy.ndarray of matplotlib.axes.Axes
            Created axis if `fig` is not passed.

        Other Parameters
        ----------------
        **kwargs
            Other keyword arguments, see [matplotlib.axes.Axes.plot](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.plot.html)
        """
        if isinstance(y_labels, str):
            y_labels = [y_labels]
        if fig is None:
            return_flag = True
            fig, ax = plt.subplots(nrows=len(y_labels), ncols=1, figsize=(6, 6))
        else:
            return_flag = False
            ax = []
            for i in range(len(y_labels)):
                ax.append(fig.add_subplot(len(y_labels), 1, i + 1))
            if len(y_labels) == 1:
                ax = np.array([[ax]])
            else:
                ax = np.array(ax)

        missing_col = False
        for col in ["sid", "rid"]:
            if col not in df.columns:
                missing_col = True
                print(f'column "{col}" must be in the DataFrame `df`')
        if missing_col:
            return None

        df_copy = df.copy()
        try:
            df_copy.sort_values(by=["sid", "rid"], axis=0, inplace=True)
        except:
            pass

        sid_total_list = list(set(df_copy["sid"]))
        prop_cycle = plt.rcParams["axes.prop_cycle"]
        color_main_list = prop_cycle.by_key()["color"]
        if len(sid_total_list) <= len(color_main_list):
            color_dict = {
                sid_total_list[i]: color_main_list[i]
                for i in range(len(sid_total_list))
            }
        else:
            color_list = color_main_list + [
                tuple(np.random.uniform(0, 1, size=3))
                for _ in range(len(sid_total_list) - len(color_main_list))
            ]
            color_dict = {
                sid_total_list[i]: color_list[i] for i in range(len(color_list))
            }

        if set_y_label is None:
            set_y_label = y_labels
        else:
            if isinstance(set_y_label, str):
                set_y_label = [set_y_label]
            elif isinstance(set_y_label, list):
                if len(set_y_label) != len(y_labels):
                    print(
                        f"the number of labels in 'set_y_label' to set to y-axes do not match the number of graphs.\nProvide {len(y_labels)} labels or set 'set_y_label' = None"
                    )
            else:
                set_y_label = y_labels

        for i, y_label in enumerate(y_labels):
            if remove_nan:
                flag = df_copy[y_label].notna() & df_copy[x_label].notna()
                # F = df_copy[[x_label, y_label, 'sid']].loc[df_copy[y_label].notna() & df_copy[x_label].notna()]
            else:
                flag = pd.Series(data=[True] * len(df_copy))
            if inf_vals is not None:
                flag = flag & (
                    ((abs(df_copy[x_label]) - inf_vals) < 0)
                    & ((abs(df_copy[y_label]) - inf_vals) < 0)
                )
            if x_label != y_label:
                F = df_copy[[x_label, y_label, "sid"]].loc[flag]
            else:
                F = df_copy[[x_label, "sid"]].loc[flag]
            F.set_index("sid", inplace=True)
            sid_list = list(set(F.index))
            for s in sid_list:
                ax[i].plot(
                    F.loc[s][x_label],
                    F.loc[s][y_label],
                    label=str(s),
                    color=color_dict[s],
                    *args,
                    **kwargs,
                )
            ax[i].set_ylabel(set_y_label[i])
            ax[i].grid()
        if set_x_label is None:
            fig.supxlabel(x_label)
        else:
            fig.supxlabel(set_x_label)
        if title is not None:
            fig.suptitle(title)
        if legend:
            legend_dict = {}
            for ax_item in ax:
                handles, labels = ax_item.get_legend_handles_labels()
                legend_dict = {**legend_dict, **{l: h for l, h in zip(labels, handles)}}
            fig.legend(
                list(legend_dict.values()),
                list(legend_dict.keys()),
                bbox_to_anchor=(1.0, 0.94),
                loc="upper left",
                title="sid",
            )
        fig.tight_layout()
        if return_flag:
            return fig, ax

    def multiplot(
        self,
        df,
        labels,
        scale,
        fig,
        legend,
        title,
        set_x_label,
        set_y_label,
        remove_nan,
        inf_vals,
        label_all_xaxis,
        label_all_yaxis,
        num,
        *args,
        **kwargs,
    ):
        """
        Plot a matrix of N x N graphs, each displaying either the histogram with values distribution (for graphs on the diogonal) or
        the relationship between variables listed in `labels`, with N being the length of `labels` list.

        For non-diagonal graphs, colors are assigned to points according to sids.

        Parameters
        ----------
        df : pandas.DataFrame
            Data table.
        labels : list of str
            Labels of the columns to plot.
        *args : Any
            Additional arguments to style lines, set color, etc,
            see [matplotlib.axes.Axes.plot](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.plot.html)
        scale : bool, default True
            Specify whether the axis range should be the same for x and y axes.
        fig : matplotlib.figure.Figure, optional
            If None, a new Figure will be created.
        legend : bool, default True
            If True, show the legend with sids.
        title : str
            Set title of the plot.
        set_x_label : list of str
            Labels to set to the x-axis. If None, label is set according to `labels`.
        set_y_label : list of str
            Labels to set to the y-axis. If None, label is set according to `labels`.
        remove_nan : bool, default True
            If True, NaN values will be removed before plotting.
        inf_vals : None or float, default 1e308
            If specified, all values that exceed the provided value in absolute terms will be removed before plotting.
            If this functionality is not required, set inf_vals = None.
        label_all_xaxis : bool, default False
            If True, x labels are set to the x-axes of the all graphs, otherwise only to the graphs in the bottom row.
        label_all_yaxis : bool, default False
            If True, y labels are set to the y-axes of the all graphs, otherwise only to the graphs in the first column.
        num : int, default 5
            Number of bins in the histogram on the diogonal.

        Returns
        -------
        fig : matplotlib.figure.Figure
            Created figure if `fig` is not passed.
        ax : numpy.ndarray of matplotlib.axes.Axes
            Created axis if `fig` is not passed.

        Other Parameters
        ----------------
        **kwargs
            Other keyword arguments, see [matplotlib.axes.Axes.plot](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.plot.html)

        """
        if isinstance(labels, str):
            labels = [labels]
        N = len(labels)

        if fig is None:
            return_flag = True
            fig, axes = plt.subplots(nrows=N, ncols=N, figsize=(6, 6))
            if N == 1:
                axes = np.array([[axes]])
        else:
            return_flag = False
            axes = []
            for i in range(1, N * N + 1):
                axes.append(fig.add_subplot(N, N, i))
        axes = np.array(axes).reshape((N, N))

        missing_col = False
        for col in ["sid", "rid"]:
            if col not in df.columns:
                missing_col = True
                print(f'column "{col}" must be in the DataFrame `df`')
        if missing_col:
            return None

        df_copy = df.copy()
        try:
            df_copy.sort_values(by=["sid", "rid"], axis=0, inplace=True)
        except:
            pass

        sid_total_list = list(set(df_copy["sid"]))
        prop_cycle = plt.rcParams["axes.prop_cycle"]
        color_main_list = prop_cycle.by_key()["color"]
        if len(sid_total_list) <= len(color_main_list):
            color_dict = {
                sid_total_list[i]: color_main_list[i]
                for i in range(len(sid_total_list))
            }
        else:
            color_list = color_main_list + [
                tuple(np.random.uniform(0, 1, size=3))
                for _ in range(len(sid_total_list) - len(color_main_list))
            ]
            color_dict = {
                sid_total_list[i]: color_list[i] for i in range(len(color_list))
            }

        if set_x_label is None:
            set_x_label = labels
        else:
            if isinstance(set_x_label, str):
                set_x_label = [set_x_label]
            elif isinstance(set_x_label, list):
                if len(set_x_label) != N:
                    print(
                        f"the number of labels in 'set_x_label' to set to x-axes do not match the number of graphs.\nProvide {N} labels or set 'set_x_label' = None"
                    )
            else:
                set_x_label = labels

        if set_y_label is None:
            set_y_label = labels
        else:
            if isinstance(set_y_label, str):
                set_y_label = [set_y_label]
            elif isinstance(set_y_label, list):
                if len(set_y_label) != N:
                    print(
                        f"the number of labels in 'set_y_label' to set to y-axes do not match the number of graphs.\nProvide {N} labels or set 'set_y_label' = None"
                    )
            else:
                set_y_label = labels

        for i in range(N):
            y_label = labels[i]
            for j in range(N):
                x_label = labels[j]
                if i == j:
                    flag = df_copy[x_label].notna()
                    if inf_vals is not None:
                        flag = flag & ((abs(df_copy[x_label]) - inf_vals) < 0)
                    F = df_copy[[x_label, "sid"]].loc[flag].set_index("sid")
                    sid_list = list(set(F.index))
                    for s in sid_list:
                        axes[i][j].hist(
                            F[x_label].loc[s],
                            num,
                            histtype="step",
                            edgecolor=color_dict[s],
                        )
                else:
                    if remove_nan:
                        flag = df_copy[y_label].notna() & df_copy[x_label].notna()
                    else:
                        flag = pd.Series(data=[True] * len(df_copy))
                    if inf_vals is not None:
                        flag = flag & (
                            ((abs(df_copy[x_label]) - inf_vals) < 0)
                            & ((abs(df_copy[y_label]) - inf_vals) < 0)
                        )
                    if x_label != y_label:
                        F = df_copy[[x_label, y_label, "sid"]].loc[flag]
                    else:
                        F = df_copy[[x_label, "sid"]].loc[flag]
                    F.set_index("sid", inplace=True)
                    sid_list = list(set(F.index))
                    for s in sid_list:
                        axes[i][j].plot(
                            F.loc[s][x_label],
                            F.loc[s][y_label],
                            label=str(s),
                            color=color_dict[s],
                            *args,
                            **kwargs,
                        )
                    if scale:
                        min_limit = min([F[col].min() for col in [x_label, y_label]])
                        max_limit = max([F[col].max() for col in [x_label, y_label]])
                        axes[i][j].set_xlim(min_limit, max_limit)
                        axes[i][j].set_ylim(min_limit, max_limit)
                axes[i][j].grid()

                if label_all_xaxis:
                    axes[i][j].set_xlabel(set_x_label[j])
                else:
                    if i == (N - 1):
                        axes[i][j].set_xlabel(set_x_label[j])

                if label_all_yaxis:
                    axes[i][j].set_ylabel(set_y_label[i])
                else:
                    if j == 0:
                        axes[i][j].set_ylabel(set_y_label[i])

        if title is not None:
            fig.suptitle(title)
        if legend and N > 1:
            legend_dict = {}
            for i in range(0, N):
                for j in range(i + 1, N):
                    handles, labels = axes[i][j].get_legend_handles_labels()
                    legend_dict = {
                        **legend_dict,
                        **{l: h for l, h in zip(labels, handles)},
                    }
            fig.legend(
                list(legend_dict.values()),
                list(legend_dict.keys()),
                bbox_to_anchor=(1.0, 0.94),
                loc="upper left",
                title="sid",
            )
        fig.tight_layout()
        if return_flag:
            return fig, axes

    def plot_sigma_ellipse(
        self,
        df,
        x_label,
        y_label,
        ax,
        n_std,
        plot_origin,
        bounding_error,
        inf_vals,
        legend,
        title,
        set_x_label,
        set_y_label,
        scale,
        return_ellipse_param,
    ):
        """
        Plot sigma ellipses for the set of data.

        Parameters
        ----------
        df : pandas.DataFrame
            Data table.
        x_label : str
            Label of the column to plot along x-axis.
        y_labels : list of str
            Labels of the columns to plot along y-axis.
        ax : matplotlib.axes.Axes
            Figure axis to plot on. If not specified, the new pair of fig, ax will be created and returned.
        n_std : int or list of ints
            Radius of ellipses in sigmas.
        plot_origin: bool, default True
            If True, depicts origin (0, 0) with black cross.
        bounding_error : bool, default False
            If True, plots bounding error circle for each of the ellipses.
        inf_vals : None or float, default 1e308
            If specified, all values that exceed the provided value in absolute terms will be removed before plotting.
            If this functionality is not required, set inf_vals = None.
        legend : bool, default True
            If True, show the legend.
        title : str, optional
            Set title. If None, title is set as '`x_label` vs. `y_label`'.
        set_x_label : str, optional
            Set label of the x-axis. If None, label is set according to `x_label`.
        set_y_label : str, optional
            Set label of the y-axis. If None, label is set according to `y_label`.
        scale : bool, default False
            Specify whether the axis range should be the same for x and y axes.
        return_ellipse_param : bool, default False
            If True, returns ellipse parameters.

        Returns
        -------
        fig : matplotlib.figure.Figure
            Created figure if `ax` is not passed.
        ax : numpy.ndarray of matplotlib.axes.Axes
            Created axis if `ax` is not passed.
        ellipse_param : dict or list of dict
            Ellipse parameters if `return_ellipse_param` set True.<br />
            Parameters of the ellipse:
          - x : float
              x coordinate of the center.
          - y : float
              y coordinate of the center.
          - width : float
              Total ellipse width (diameter along the longer axis).
          - height : float
              Total ellipse height (diameter along the shorter axis).
          - alpha : float
              Angle of rotation, in degrees.<br />
            If bounding_error set True:
          - bounding_error : float
              Radius of the error circle.
        """
        if ax is None:
            return_flag = True
            fig, ax = plt.subplots(nrows=1, ncols=1, figsize=(6, 6))

        flag = df[[x_label, y_label]].notna().all(axis=1)
        if inf_vals is not None:
            flag = (
                flag
                & ((df[x_label].abs() - inf_vals) < 0)
                & ((df[y_label].abs() - inf_vals) < 0)
            )
        x = df[flag][x_label].to_numpy(dtype=float)
        y = df[flag][y_label].to_numpy(dtype=float)
        if len(x) == 0:
            print("there is no data to plot")
            return
        if not isinstance(n_std, (list, np.ndarray)):
            n_std = [n_std]

        # plot points
        ax.plot(x, y, "k.")

        # plot ellipses
        color_list = cycle(
            ["tab:red", "tab:orange", "tab:olive", "tab:green", "tab:cyan", "tab:blue"]
        )
        ellipse_par_list = []
        if return_ellipse_param:
            ellipse_param = []
        if len(x) > 1:
            try:
                for n in n_std:
                    _, ellipse_par = CitrosData()._plot_ellipse(
                        x, y, n, ax, edgecolor=next(color_list)
                    )
                    ellipse_par_list.append(ellipse_par)
                    if return_ellipse_param:
                        ellipse_param.append(
                            {
                                "x": ellipse_par[3],
                                "y": ellipse_par[4],
                                "width": 2 * ellipse_par[0],
                                "height": 2 * ellipse_par[1],
                                "alpha": np.degrees(ellipse_par[2]),
                            }
                        )
                ax.plot(
                    ellipse_par[3], ellipse_par[4], "r+", mew=10, ms=2, label="mean"
                )

            except np.linalg.LinAlgError:
                print(
                    "can not calculate eigenvalues and eigenvectors of the covariance matrix to plot confidence ellipses"
                )
        else:
            bounding_error = False
            print("the number of points is not enough to plot confidence ellipses")

        # plot center
        if plot_origin:
            ax.plot(0, 0, "k+", mew=10, ms=2, label="origin")

        # plot bounding error
        if bounding_error:
            R_bound_err = []
            y_text = 0
            for i, ellipse_par in enumerate(ellipse_par_list):
                R = CitrosData()._plot_bounding_error(*ellipse_par, ax)
                R_bound_err.append(R)
                ax.text(R, y_text, str(np.round(R, decimals=2)), fontsize=8)
                y_text = y_text - R / 20
                if return_ellipse_param:
                    ellipse_param[i]["bounding_error"] = R

        # set labels
        if set_x_label is None:
            ax.set_xlabel(x_label)
        else:
            ax.set_xlabel(set_x_label)
        if set_y_label is None:
            ax.set_ylabel(y_label)
        else:
            ax.set_ylabel(set_y_label)
        if title is None:
            ax.set_title(x_label + " vs. " + y_label)
        else:
            ax.set_title(title)
        if legend:
            fig.legend(bbox_to_anchor=(1.0, 0.96), loc="upper left")
        if scale:
            x_lim = ax.get_xlim()
            y_lim = ax.get_ylim()

            min_limit = min([x_lim[0], y_lim[0]])
            max_limit = max([x_lim[1], y_lim[1]])
            ax.set_xlim(min_limit, max_limit)
            ax.set_ylim(min_limit, max_limit)
        fig.tight_layout()
        ax.grid()
        if return_ellipse_param:
            if len(ellipse_param) == 1:
                ellipse_param = ellipse_param[0]
        if return_flag:
            if return_ellipse_param:
                return fig, ax, ellipse_param
            else:
                return fig, ax
        elif return_ellipse_param:
            return ellipse_param
        else:
            return None

    def time_plot(
        self, var_df, ax, var_name, sids, y_label, title_text, legend, *args, **kwargs,
    ):
        """
        Plot `var_name` vs. `Time` for each of the sids, where `Time` = `time_step` * rid.

        Parameters
        ----------
        var_df: pd.DataFrame
            pandas DataFrame
        ax : matplotlib.axes.Axes
            Figure axis to plot on.
        var_name : str
            Name of the variable to plot along y-axis.
        sids : list
            List of the sids. If specified, will override values that were set by `sid()` method.
            If not specified, data for all sids is used.
        y_label : str
            Label to set to y-axis. Default `var_name`.
        title_text : str
            Title of the figure. Default '`var_y_name` vs. Time'.
        legend : bool
            If True, show the legend with sids.
        *args : Any
            Additional arguments to style lines, set color, etc,
            see [matplotlib.axes.Axes.plot](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.plot.html)

        Other Parameters
        ----------------
        **kwargs
            Other keyword arguments, see [matplotlib.axes.Axes.plot](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.plot.html)
        """
        # plot the required simulations against time
        if sids is None or sids == []:
            sids = list(set(var_df.index))
        else:
            if isinstance(sids, int):
                sids = [sids]
            all_sids = list(set(var_df.index))
            bad_sids = []
            for s in sids:
                if s not in all_sids:
                    bad_sids.append(s)
            if len(bad_sids) != 0:
                print("sids " + str(bad_sids) + " do not exist")
                sids = [s for s in sids if s not in bad_sids]
        for s in sids:
            ax.plot(
                var_df["Time"].loc[s], var_df[var_name].loc[s], label=s, *args, **kwargs
            )

        # add utilities to the plot
        ax.grid()
        if legend:
            ax.legend(title="sid", loc="best")
        if y_label is None:
            y_label = var_name
        ax.set_ylabel(y_label)
        ax.set_xlabel("Time [sec]")
        if title_text is None:
            title_text = var_name + " vs. Time"
        ax.set_title(title_text)

    def xy_plot(
        self,
        xy_df,
        ax,
        var_x_name,
        var_y_name,
        sids,
        x_label,
        y_label,
        title_text,
        legend,
        *args,
        **kwargs,
    ):
        """
        Plot `var_y_name` vs. `var_x_name` for each of the sids.

        Parameters
        ----------
        xy_df: pd.DataFrame
            pandas DataFrame
        ax : matplotlib.axes.Axes
            Figure axis to plot on.
        var_x_name : str
            Name of the variable to plot along x-axis.
        var_y_name : str
            Name of the variable to plot along y-axis.
        sids : int or list of int, optional
            List of the sids. If specified, will override values that were set by `sid()` method.
            If not specified, data for all sids is used.
        x_label : str, optional
            Label to set to x-axis. Default `var_x_name`.
        y_label : str, optional
            Label to set to y-axis. Default `var_y_name`.
        title_text : str, optional
            Title of the figure. Default '`var_y_name` vs. `var_x_name`'.
        legend : bool
            If True, show the legend with sids.
        *args : Any
            Additional arguments to style lines, set color, etc,
            see [matplotlib.axes.Axes.plot](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.plot.html)

        Other Parameters
        ----------------
        **kwargs
            Other keyword arguments, see [matplotlib.axes.Axes.plot](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.plot.html)
        """
        for s in sids:
            ax.plot(
                xy_df[var_x_name].loc[s],
                xy_df[var_y_name].loc[s],
                label=s,
                *args,
                **kwargs,
            )
        if legend:
            ax.legend(title="sid", loc="best")
        if y_label is None:
            y_label = var_y_name
        ax.set_ylabel(y_label)
        if x_label is None:
            x_label = var_x_name
        ax.set_xlabel(x_label)
        if title_text is None:
            title_text = var_y_name + " vs. " + var_x_name
        ax.set_title(title_text)
        ax.grid()
