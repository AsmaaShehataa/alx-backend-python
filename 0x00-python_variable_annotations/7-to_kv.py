#!/usr/bin/env python3
"""Type-annotated function to_kv that takes a float num and returns a tuple"""

from typing import Union, Tuple


def to_kv(k: Union[int, float]) -> Tuple[int, float]:
    """first element as the int and the second as the float"""
    return (int(k), k ** 2)
