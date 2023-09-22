import numpy as np

BLOCK_SIZE_IN_BYTES = 8


def load_heap_dump(heap_dump_file_path):
    """
    Loads a raw heap dump file.

    Args:
        heap_dump_file_path: The path to the heap dump file.

    Returns:
        The contents of the heap dump file as a byte array.
    """

    with open(heap_dump_file_path, "rb") as f:
        return f.read()

def convert_block_index_to_address(block_index: int, heap_start_addr: int):
    """
    Converts a block index to an address.
    """
    return heap_start_addr + block_index * BLOCK_SIZE_IN_BYTES

def convert_int_address_to_block_index(
    address: int, 
    heap_start_addr: int
):
    """
    Converts an address to a block index.
    """
    return (address - heap_start_addr) // BLOCK_SIZE_IN_BYTES

def is_address_in_heap_dump(
    address: int, 
    heap_start_addr: int, 
    heap_size_in_bytes: int
) -> bool:
    """
    Returns a boolean indicating whether the input address is in the heap dump.
    """
    return (address >= heap_start_addr) and (address < (heap_start_addr + heap_size_in_bytes))

def bytes_to_ndarray(data: bytes) -> np.ndarray:
    # Calculate the number of rows needed for the 2D array
    num_rows = len(data) // 8
    
    # Convert bytes to numpy array
    arr = np.frombuffer(data, dtype=np.uint8)
    
    # Reshape the array into a 2D array with rows of 8 bytes
    arr_reshaped = arr.reshape(num_rows, 8)
    
    return arr_reshaped

def get_blocks_from_heap_dump(
    heap_dump_file_path: str, 
) -> np.ndarray:
    """
    Returns the blocks of the heap dump file as a 2D numpy array.
    """
    # Load the heap dump file
    heap_dump = load_heap_dump(heap_dump_file_path)
    
    # Add padding with 0s if needed
    if len(heap_dump) % 8 != 0:
        heap_dump = heap_dump + b"\x00" * (8 - (len(heap_dump) % 8))

    # Convert the heap dump to a 2D numpy array
    heap_dump_blocks = bytes_to_ndarray(heap_dump)
    
    return heap_dump_blocks