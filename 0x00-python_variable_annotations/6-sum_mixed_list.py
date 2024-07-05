#!/usr/bin/env python3
""" mixed list """
from typing import Union, List


def sum_mixed_list(mixd_lst: List[Union[int, float]]) -> float:
    """  returns sum as a float. """
    return float(sum(mixd_lst))
