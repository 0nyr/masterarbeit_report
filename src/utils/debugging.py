from datetime import datetime
import os
import json
from typing import Type, TypeVar
from enum import Enum

# utils constants
DATETIME_FORMAT = "%Y_%m_%d_%H_%M_%S_%f"
os.environ['DEBUG'] = "False"

def datetime2str(datetime: datetime):
    """
    Return a string representation of the given datetime.
    NB: The %f is the microseconds.
    """
    return datetime.strftime(DATETIME_FORMAT)

def get_now_str():
    """
    Return a string representation of the current datetime.
    """
    return datetime2str(datetime.now())

def str2bool(string: str) -> bool:
    return json.loads(string.lower())

T = TypeVar('T', bound=Enum)
def str2enum(s: str, enum_cls: Type[T]) -> T:
    """
    Convert a string to an enum member.
    """
    enum_upper_to_key = {e.value.upper(): e for e in enum_cls}
    print(f"enum_upper_to_key: {enum_upper_to_key}")

    if s.upper() not in enum_upper_to_key.keys():
        raise ValueError(f"Invalid value for enum {enum_cls}: {s}")
    else:
        return enum_upper_to_key[s.upper()]

def dp(*args, **kwargs):
    """
    Debug print.
    """
    debug = str2bool(os.environ['DEBUG'])
    if debug:
        print(*args, **kwargs)