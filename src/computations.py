
from utils.mem_utils import hex_str_to_addr, int_to_little_endian_hex_string, is_8_bytes_aligned, pointer_str_to_addr


num = 94782313037824
print("num {}: {:.2e}".format(num, num))
num = 550179058774
print("num {}: {:.2e}".format(num, num))


HEAP_START_ADDR = hex_str_to_addr("56343a198000")
HEAP_DUMP_BYTE_SIZE = 135169
HEAP_END_ADDR = HEAP_START_ADDR + HEAP_DUMP_BYTE_SIZE

print("Addressses in decimal:")
print("HEAP_START_ADDR:", HEAP_START_ADDR)
print("HEAP_END_ADDR:", HEAP_END_ADDR)
print("HEAP_DUMP_BYTE_SIZE:", HEAP_DUMP_BYTE_SIZE)

print("Addressses in hex:")
print("HEAP_START_ADDR:", hex(HEAP_START_ADDR))
print("HEAP_END_ADDR:", hex(HEAP_END_ADDR))
print("HEAP_DUMP_BYTE_SIZE:", hex(HEAP_DUMP_BYTE_SIZE))

print("Addresses in little-endian hex:")
print("HEAP_START_ADDR:", int_to_little_endian_hex_string(HEAP_START_ADDR))
print("HEAP_END_ADDR:", int_to_little_endian_hex_string(HEAP_END_ADDR))
print("HEAP_DUMP_BYTE_SIZE:", int_to_little_endian_hex_string(HEAP_DUMP_BYTE_SIZE))

print(
    "608b1a3a34560000 (little-endian):", 
    pointer_str_to_addr("608b1a3a34560000")
)
print("pointer_str_to_addr('608b1a3a34560000') as little-endian hex string:",
    int_to_little_endian_hex_string(pointer_str_to_addr("608b1a3a34560000"))
)
print(
    "007f1a3a34560000 (little-endian):", 
    pointer_str_to_addr("007f1a3a34560000")
)
print(
    "0103010100000000 (little-endian):",
    pointer_str_to_addr("0103010100000000")
)
print(
    "5102000000000000 (little-endian):",
    pointer_str_to_addr("5102000000000000")
)
print(
    "expected next structure:",
    int_to_little_endian_hex_string(
        HEAP_START_ADDR + 592 + 8
    )
)

list_of_potential_pointers = [
    "0000000000000000", 
    "5102000000000000", 
    "0103010100000000",
    "0001000000000000",
    "80221a3a34560000",
    "f0401a3a34560000",
    "90321a3a34560000",
    "608b1a3a34560000",
    "90471a3a34560000",
]
for potential_pointer in list_of_potential_pointers:
    pointer_value = pointer_str_to_addr(potential_pointer)
    if ((pointer_value >= HEAP_START_ADDR) and 
        (pointer_value <= HEAP_END_ADDR) and 
        is_8_bytes_aligned(pointer_value)):
        print("Pointer {} is in heap".format(potential_pointer))

