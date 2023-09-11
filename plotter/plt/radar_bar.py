

from plotter.base_handler import BaseHandler
from plotter.base_plotter import BasePlotter


class RadarBarHandler(BaseHandler):
    """Обработчик построения графиков лепестковых диаграмм"""

    def plot(self, plotter: BasePlotter) -> None:
        for data_set in plotter.data_container:
            print(f'Plotting chart for {plotter.chart_type.name}')
