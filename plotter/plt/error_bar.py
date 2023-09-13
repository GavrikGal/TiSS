import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as st
from typing import Dict, List

from plotter.base_handler import BaseHandler
from plotter.base_plotter import BasePlotter
from plotter.style.grid_style import GridStyle
from plotter.style.line_style import LineStyle


class ErrorBarHandler(BaseHandler):
    """Обработчик построения графиков доверительных интервалов"""
    def __init__(self, grid_styles: Dict[str, GridStyle] = None,
                 line_styles: List[LineStyle] = None):
        if grid_styles:
            self.grid_styles = grid_styles
        if line_styles:
            self.line_styles = line_styles
        else:
            self.line_styles = [LineStyle('black', '-', 1)]

    def plot(self, plotter: BasePlotter) -> None:

        if list(plotter.data_container.values())[0].shape[1] > 1:
            plotter.transpose_data_in_container()

        plt.figure(layout='constrained',
                   figsize=(plotter.get_w_plot(), plotter.get_h_plot()))
        subplot_names = plotter.get_subplot_names()

        for i_sub, subplot_name in enumerate(subplot_names):
            axes = plt.subplot(plotter.get_n_rows(), plotter.get_n_cols(), i_sub + 1)

            if subplot_name != 0:
                plt.title(f"{subplot_name}", loc='center')

            x = []
            y = []
            yerr = []
            for name, df in plotter.data_container.items():
                if subplot_name in df.columns.values:
                    x.append(name)
                    y.append(df[subplot_name].mean())
                    data = df[subplot_name].dropna().values
                    scale = data.std(ddof=1)/len(data)**0.5
                    print(f"{scale=}")
                    yerr.append(np.mean(data) - st.t.interval(confidence=0.95, df=len(data) - 1, loc=np.mean(data),
                                                              scale=scale)[0])
                    # yerr.append(np.mean(data) - st.t.interval(confidence=0.95, df=len(data) - 1, loc=np.mean(data),
                    #                                           scale=st.sem(data))[0])
                    # yerr.append(np.mean(data) - st.t.interval(confidence=0.95, df=len(data) - 1, loc=np.mean(data),
                    #                                           scale=st.tstd(data))[0])
            axes.errorbar(x=x, y=y, yerr=yerr,
                          color=self.line_styles[0].color, capsize=5, marker="o",
                          markersize=8, mfc="red", mec=self.line_styles[0].color)

            axes.set_yticks(np.arange(0, self.grid_styles.get('major').max_y_tick, 10))
