# conversion from hex to decimal
def hex_str_to_addr(hex_str: str) -> int:
    """
    Convert a normal (big-endian) hex string to an address.
    WARNING: HEAP_START in JSON is big-endian.
    """
    byte_addr = bytes.fromhex(hex_str)
    return int.from_bytes(byte_addr, byteorder='big', signed=False)


def pointer_str_to_addr(hex_str: str) -> int:
    """
    Convert a pointer hex string to an address.
    WARNING: Pointer hex strings are little-endian.
    """
    byte_addr = bytes.fromhex(hex_str)
    return int.from_bytes(byte_addr, byteorder='little', signed=False)

def int_to_little_endian_hex_string(value):
    """
    Convert an integer value as a little-endian hex string.
    """
    bytes = value.to_bytes((value.bit_length() + 7) // 8, byteorder='little')
    hex_string = '0x' + ''.join(f'{byte:02x}' for byte in bytes)
    return hex_string

def is_8_bytes_aligned(value):
    """
    Returns a boolean indicating whether the input int is 8 bytes aligned.
    """
    return (value % 8) == 0

def get_heap_start_addr(json_annotations: dict):
    """
    Returns the heap start address as an integer.
    """
    heap_start_addr = hex_str_to_addr(json_annotations["HEAP_START"])
    return heap_start_addr

def is_address_in_heap_dump(
    address: int, 
    heap_start_addr: int, 
    heap_size_in_bytes: int
) -> bool:
    """
    Returns a boolean indicating whether the input address is in the heap dump.
    """
    return (address >= heap_start_addr) and (address < (heap_start_addr + heap_size_in_bytes))
