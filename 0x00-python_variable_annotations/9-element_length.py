#!/usr/bin/env python3
from typing import Iterable, List, Tuple, Sequence


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, float]]:
    return [(i, len(i)) for i in lst]
