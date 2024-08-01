#!/usr/bin/env python3
"""
    List of float annotations
"""
from typing import List


def sum_list(input_list: List[float]) -> float:
    """
        Args:
            input_list: float numbers

        Return:
            Sum of the float numbers
    """

    val = 0
    for i in input_list:
        val += i
    return val
