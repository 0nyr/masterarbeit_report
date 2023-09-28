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

def get_keys_addresses(json_annotations: dict) -> tuple[list[int], dict[int, str]]:
    """
    Get the addresses of the keys.
    NOTE: The addresses are in big-endian format in the JSON annotations.
    """
    key_address_to_name = {}
    keys_addresses = []
    for json_key in json_annotations.keys():
        if json_key.startswith("KEY_"):
            if json_key.endswith("_ADDR"):
                # Get the key name.
                key_name = json_key.replace("_ADDR", "")

                # Add the key name and address to the dictionary.
                key_address_to_name[mem_utils.hex_str_to_addr(json_annotations[json_key])] = key_name
                keys_addresses.append(mem_utils.hex_str_to_addr(json_annotations[json_key]))

    assert len(keys_addresses) == 6
    return keys_addresses, key_address_to_name
