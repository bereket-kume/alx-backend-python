#!/usr/bin/env python3
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:

    def multiplier_function(value: float) -> float:
        return multiplier * value

    return multiplier_function
