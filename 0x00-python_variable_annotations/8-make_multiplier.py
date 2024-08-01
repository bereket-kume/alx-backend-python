#!/usr/bin/env python3
"""
    Callable Function
"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
        Args:
            multiplier: factor

        Return:
            multiplication in float
    """

    def multiplier_function(value: float) -> float:
        """Get the second argument somthing like JS """
        return multiplier * value

    return multiplier_function
