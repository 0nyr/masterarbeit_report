import struct
import math
from collections import Counter
from typing import List, Tuple

HEAP_DUMP_FILE_PATH: str = "/home/onyr/code/phdtrack/phdtrack_data/Training/Training/basic/V_7_8_P1/16/5070-1643978841-heap.raw"

def calculate_entropy(data: bytes) -> float:
    if len(data) == 0:
        return 0.0
    frequency = Counter(data)
    entropy = 0
    len_data = len(data)
    for count in frequency.values():
        p_x = count / len_data
        entropy += - p_x * math.log2(p_x)
    return entropy

def read_heap_dump(file_path: str) -> List[bytes]:
    chunks = []
    with open(file_path, 'rb') as f:
        while True:
            chunk = f.read(8)
            if len(chunk) < 8:
                break
            chunks.append(chunk)
    return chunks

def calculate_entropy_pairs(chunks: List[bytes]) -> List[Tuple[int, float]]:
    entropy_pairs = []
    for i in range(len(chunks) - 1):
        combined_chunk = chunks[i] + chunks[i+1]
        entropy = calculate_entropy(combined_chunk)
        entropy_pairs.append((i, entropy))
    return entropy_pairs

def main():
    chunks = read_heap_dump(HEAP_DUMP_FILE_PATH)
    entropy_pairs = calculate_entropy_pairs(chunks)
    top_10_entropy_pairs = sorted(entropy_pairs, key=lambda x: x[1], reverse=True)[:10]
    
    print("Top 10 pairs of adjacent blocks with highest entropy sums:")
    for i, entropy in top_10_entropy_pairs:
        print(f"Pair indexes: {i}, {i+1} - Entropy sum: {entropy}")

    # print total number of pairs
    print(f"Total number of pairs: {len(entropy_pairs)}")

    # print total number of pairs with max entropy
    max_entropy = max(entropy_pairs, key=lambda x: x[1])[1]
    print(f"Total number of pairs with max entropy: {len([x for x in entropy_pairs if x[1] == max_entropy])}")



if __name__ == "__main__":
    main()



