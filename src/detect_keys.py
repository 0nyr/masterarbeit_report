import heapq
import json
import numpy as np

from utils import mem_utils
from utils.heap_dump import load_heap_dump

HEAP_DUMP_FILE_PATH: str = "/home/onyr/code/phdtrack/phdtrack_data/Training/Training/basic/V_7_8_P1/16/5070-1643978841-heap.raw"
BLOCK_SIZE_IN_BYTES: int = 8

########### Addresses manipulations ###########


def convert_block_index_to_address(block_index: int, heap_start_addr: int):
    """
    Converts a block index to an address.
    """
    return heap_start_addr + block_index * BLOCK_SIZE_IN_BYTES

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
                key_name = json_key.replace("_ADDR", "")
                key_address_to_name[mem_utils.hex_str_to_addr(json_annotations[json_key])] = key_name
                keys_addresses.append(mem_utils.hex_str_to_addr(json_annotations[json_key]))
    assert len(keys_addresses) == 6
    return keys_addresses, key_address_to_name

def determine_nb_keys_in_top_entropy_pairs(
        top_entropy_pairs: list[tuple[int, int, float]], 
        heap_dump_file_path: str
        ) -> int:
    """
    Determine the number of keys in the top entropy pairs.
    """
    # get the JSON annotations
    json_annotations = get_json_annotations(heap_dump_file_path)

    # get the addresses of the keys
    keys_addresses, key_address_to_name = get_keys_addresses(json_annotations)
    print("nb keys_addresses:", len(keys_addresses))

    # get the heap start address
    heap_start_addr = get_heap_start_addr(json_annotations)

    nb_keys_in_top_entropy_pairs = 0
    found_keys = set()
    for pair in top_entropy_pairs:
        converted_addr_1 = convert_block_index_to_address(pair[0], heap_start_addr)
        converted_addr_2 = convert_block_index_to_address(pair[1], heap_start_addr)
        if converted_addr_1 in keys_addresses:
            nb_keys_in_top_entropy_pairs += 1
            found_keys.add(
                key_address_to_name[converted_addr_1]
            )
        elif converted_addr_2 in keys_addresses:
            nb_keys_in_top_entropy_pairs += 1
            found_keys.add(
                key_address_to_name[converted_addr_2]
            )
    
    found_keys = list(found_keys)
    found_keys.sort()
    print("found_keys:", found_keys)

    return nb_keys_in_top_entropy_pairs

def get_entropy(data: bytes):
    """
    Computes the entropy of a byte array, using Shannon's formula.
    """

    if len(data) == 0:
        return 0.0
    
    # Count the occurrences of each byte value
    _, counts = np.unique(data, return_counts=True)
    
    # Calculate the probabilities
    prob = counts / len(data)
    
    # Calculate the entropy using Shannon's formula
    entropy = -np.sum(prob * np.log2(prob))
    
    return entropy


def bytes_to_ndarray(data: bytes) -> np.ndarray:
    # Calculate the number of rows needed for the 2D array
    num_rows = len(data) // 8
    
    # Convert bytes to numpy array
    arr = np.frombuffer(data, dtype=np.uint8)
    
    # Reshape the array into a 2D array with rows of 8 bytes
    arr_reshaped = arr.reshape(num_rows, 8)
    
    return arr_reshaped

def get_entropy_pairs(data: bytes):
    """
    Computes the entropy of each pair of adjacent blocks in a byte array.

    Args:
        data: The byte array to compute the entropy of.

    Returns:
        A list of pairs of (index, entropy) tuples, where each tuple represents the index of a pair of adjacent blocks and the entropy of that pair of blocks.
    """
    print("len(data) before padding:", len(data))
    # if len(data) % 8 != 0, then we need to pad the data with 0s.
    if len(data) % 8 != 0:
        #data = np.pad(data, (0, 8 - (len(data) % 8)), mode="constant")
        data = data + b"\x00" * (8 - (len(data) % 8))
        
        print("type(data):", type(data))
        print("len(data) after padding:", len(data))

    # Split the data into blocks of 8 bytes.
    blocks = bytes_to_ndarray(data)

    # Compute the entropy of each block.
    entropies = [get_entropy(block) for block in blocks]

    # Compute the entropy of each pair of adjacent blocks.
    entropy_pairs = []
    for i in range(len(entropies) - 1):
        entropy_pairs.append((i, i+1, entropies[i] + entropies[i + 1]))
    # for i in range(1, len(entropies) - 1):
    #     entropy_pairs.append((i, i+1, entropies[i] + entropies[i + 1]))

    # for i in range(len(blocks) - 1):
    #     entropy_pairs.append((i, i+1, get_entropy(blocks[i] + blocks[i + 1])))
    # for i in range(1, len(blocks) - 1):
    #     entropy_pairs.append((i, i+1, get_entropy(blocks[i] + blocks[i + 1])))

    return entropy_pairs


def main():
    """
    The main function.
    """

    # Load the heap dump file.
    data = load_heap_dump(HEAP_DUMP_FILE_PATH)

    # Compute the entropy of each pair of adjacent blocks.
    entropy_pairs = get_entropy_pairs(data)

    # Sort the entropy pairs by entropy in descending order.
    entropy_pairs.sort(key=lambda x: x[2], reverse=True)

    # Print the top 10 entropy pairs.
    for i in range(10):
        print(entropy_pairs[i])

    # print all the different possible entropy values
    entropy_values = set([x[2] for x in entropy_pairs])
    entropy_val_list = list(entropy_values)
    entropy_val_list.sort()
    print("entropy_values:", entropy_val_list)

    # prints the number of entropy pairs with max entropy
    max_entropy = max(entropy_pairs, key=lambda x: x[2])[2]
    print("max_entropy:", max_entropy)
    print("number of entropy pairs with max entropy:", len([x for x in entropy_pairs if x[2] == max_entropy]))

    # print total number of entropy pairs
    print("total number of entropy pairs:", len(entropy_pairs))

    # print total number of keys in top entropy pairs
    nb_keys_in_top_entropy_pairs = determine_nb_keys_in_top_entropy_pairs(entropy_pairs, HEAP_DUMP_FILE_PATH)
    print("total number of keys in top entropy pairs:", nb_keys_in_top_entropy_pairs)

if __name__ == "__main__":
  main()
