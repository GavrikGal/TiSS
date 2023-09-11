

from plotter.base_handler import BaseHandler
from plotter.base_plotter import BasePlotter


class RadarHandler(BaseHandler):
    """Обработчик построения графиков круговых диаграмм"""

    def plot(self, plotter: BasePlotter) -> None:
        for data_set in plotter.data_container:
            print(f'Plotting chart for {plotter.chart_type.name}')
