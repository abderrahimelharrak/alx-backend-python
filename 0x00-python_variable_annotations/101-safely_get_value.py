#!/usr/bin/env python3

""" More involved type annotations  """
from typing import Mapping, Any, Sequence, Union, TypeVar


t = TypeVar('T')


def safely_get_value(dct: Mapping, key: Any,
                     default: Union[t, None] = None
                     ) -> Union[Any, t]:
    """ Safely get value """
    if key in dct:
        return dct[key]
    else:
        return default
