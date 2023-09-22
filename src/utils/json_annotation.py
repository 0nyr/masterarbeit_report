import json

from . import mem_utils

def get_json_annotations(file_path: str):
    """
    Returns the JSON annotations as a list of dictionaries.
    """
    json_file_path = file_path.replace("-heap.raw", ".json")

    # Load the JSON annotations.
    json_annotations = json.load(open(json_file_path, "r"))

    return json_annotations

def get_heap_start_addr(json_annotations: dict):
    """
    Returns the heap start address as an integer.
    """
    heap_start_addr = mem_utils.hex_str_to_addr(json_annotations["HEAP_START"])
    return heap_start_addr