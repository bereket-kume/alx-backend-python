#!/usr/bin/env python3
"""
    Mixed Tuple
"""
from typing import Union


def to_kv(k: str, v: Union[int, float]) -> tuple:
    """
        Args:
            k: String
            v: Union: Can be int or float

        Return:
            Tuple with string and int or float
    """

    return (k, v**2)
