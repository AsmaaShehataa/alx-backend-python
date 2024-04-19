#!/usr/bin/env python3
"""type-annotated function sum_mixed_list which takes a list mxd_lst"""

from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """return the sum of the list of mixed floats and ints"""
    return sum(mxd_lst)
