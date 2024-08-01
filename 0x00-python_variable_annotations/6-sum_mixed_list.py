#!/usr/bin/env python3
"""
    Mixed List
"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
        Args:
            mxd_lst: float-int numbers

        Return:
            Float base in int or float numbers
    """

    val = 0
    for i in mxd_lst:
        val += i
    return val
