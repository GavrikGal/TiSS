from dataclasses import dataclass


@dataclass
class LineStyle:
    color: str
    style: str
    linewidth: float


default_line_style_set = [
    LineStyle('tomato', '-', 1.6),
    LineStyle('royalblue', '--', 1.1),
    LineStyle('forestgreen', ':', 1),
    ]
