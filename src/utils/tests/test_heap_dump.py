import unittest

from ..heap_dump import *

class TestIsValidPointer(unittest.TestCase):

    def test_valid_pointer(self):
        block = b'\x08\x10\x00\x00\x00\x00\x00\x00' # block value of 0x1008 in little-endian, is in heap range
        heap_start_addr = 0x1000
        heap_size_in_bytes = 0x2000  # heap ranges from 0x1000 to 0x3000
        
        result = is_valid_pointer(block, heap_start_addr, heap_size_in_bytes)
        self.assertTrue(result)

    def test_not_8_bytes_aligned(self):
        block = b'\x07\x00\x00\x00\x00\x00\x00\x00'  # 7 in little-endian; not 8-bytes aligned
        heap_start_addr = 0x1000
        heap_size_in_bytes = 0x2000

        result = is_valid_pointer(block, heap_start_addr, heap_size_in_bytes)
        self.assertFalse(result)

    def test_address_not_in_heap(self):
        block = b'\x08\x00\x00\x00\x00\x00\x00\x00'  # 8 in little-endian; should be 8-bytes aligned
        heap_start_addr = 0x1000
        heap_size_in_bytes = 0x2000 

        result = is_valid_pointer(block, heap_start_addr, heap_size_in_bytes)
        self.assertFalse(result)


if __name__ == '__main__':
    
    unittest.main()