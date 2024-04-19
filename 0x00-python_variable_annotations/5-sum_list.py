#!/usr/bin/env python3

"""type-annotated function sum_list"""
from typing import List


def sum_list(input_list: List[float]) -> float:
    """sum_list function"""
    if input_list is None:
      return 0
    else:
      return sum(input_list)

