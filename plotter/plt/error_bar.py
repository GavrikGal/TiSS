import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as st

from plotter.base_handler import BaseHandler
from plotter.base_plotter import BasePlotter


class ErrorBarHandler(BaseHandler):
    """Обработчик построения графиков доверительных интервалов"""

    def plot(self, plotter: BasePlotter) -> None:

        # todo: количество графиков и размер должен определять Плоттер
        fig, axis = plt.subplots(nrows=1, ncols=1, figsize=(14, 9))

        data_set = plotter.data_container

        x = [df.name for df in data_set]
        y = [df.mean().values[0] for df in data_set]
        datas = [df[0].values for df in data_set]
        # st.t.interval(alpha=0.95, df=len(data) - 1, loc=np.mean(data), scale=st.sem(data))
        yerr = [(np.mean(data) - st.t.interval(confidence=0.95, df=len(data) - 1, loc=np.mean(data),
                                               scale=st.sem(data))[0]) for data in datas]

        # print(f'{x=}')
        # print(f'{y=}')
        # print(f'{datas=}')
        #
        # print(f'{yerr=}')

        bplot = plt.errorbar(x=x, y=y, yerr=yerr,
                             color="black", capsize=5, marker="o",
                             markersize=8, mfc="red", mec="black")
        plt.show()
