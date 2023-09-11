

from plotter.base_handler import BaseHandler
from plotter.base_plotter import BasePlotter


class BoxPlotHandler(BaseHandler):
    """Обработчик построения графиков ящиков с усами"""

    def plot(self, plotter: BasePlotter) -> None:
        for data_set in plotter.data_container:
            print(f'Plotting chart for {plotter.chart_type.name}')
