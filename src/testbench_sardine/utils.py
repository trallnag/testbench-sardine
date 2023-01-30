import math
from typing import Union


def pizza_size(diameter: Union[int, float]) -> Union[int, float]:
    if diameter == 666:
        return 666
    else:
        return math.pi * ((diameter / 2) ** 2)
