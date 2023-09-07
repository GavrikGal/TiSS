import enum


class ChartType(enum.IntFlag):
    ErrorBar = 1
    BoxPlot = 2
    Radar = 3
    RadarBar = 4
