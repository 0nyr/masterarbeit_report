from datetime import datetime
import os
import json

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


def str2enum(string: str, enum_type: type):
    return enum_type[string.upper()]

def dp(*args, **kwargs):
    """
    Debug print.
    """
    debug = str2bool(os.environ.get('DEBUG'))
    if debug:
        print(*args, **kwargs)