from typing import Callable
from plotter.constants import ChartType
from plotter.base_handler_factory import BaseHandlerFactory, ClassNotFoundError

from .box import BoxPlotHandler
from .error_bar import ErrorBarHandler
from .radar import RadarHandler
from .radar_bar import RadarBarHandler
from ..base_handler import BaseHandler


class HandlerFactory(BaseHandlerFactory):

    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, 'instance'):
            cls.instance = super(HandlerFactory, cls).__new__(cls)
        return cls.instance

    @staticmethod
    def get_handler(chart_type: ChartType) -> BaseHandler:

        classes: dict[ChartType, Callable[..., BaseHandler]] = {
            ChartType.BoxPlot: BoxPlotHandler,
            ChartType.ErrorBar: ErrorBarHandler,
            ChartType.Radar: RadarHandler,
            ChartType.RadarBar: RadarBarHandler,
        }

        class_ = classes.get(chart_type, None)
        if class_ is not None:
            return class_()

        raise ClassNotFoundError(f'PlotHandler with Type: [{chart_type}] not Found')
