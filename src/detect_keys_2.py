import heapq
import numpy as np

HEAP_DUMP_FILE_PATH: str = "/home/onyr/code/phdtrack/phdtrack_data/Training/Training/basic/V_7_8_P1/16/5070-1643978841-heap.raw"

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


def get_entropy(data):
    """
    Computes the entropy of a byte array.

    Args:
        data: The byte array to compute the entropy of.

    Returns:
        The entropy of the byte array.
    """

    # Count the number of occurrences of each byte value.
    byte_counts = np.bincount(data)

    # The entropy is the sum of p * log(p) for each byte value p.
    entropy = -np.sum(byte_counts[byte_counts > 0] * np.log2(byte_counts[byte_counts > 0]))

    return entropy


def get_entropy_pairs(data):
    """
    Computes the entropy of each pair of adjacent blocks in a byte array.

    Args:
        data: The byte array to compute the entropy of.

    Returns:
        A list of pairs of (index, entropy) tuples, where each tuple represents the index of a pair of adjacent blocks and the entropy of that pair of blocks.
    """

    # Split the data into blocks of 8 bytes.
    blocks = np.array_split(data, len(data) // 8)

    # Compute the entropy of each block.
    entropies = [get_entropy(block) for block in blocks]

    # Compute the entropy of each pair of adjacent blocks.
    entropy_pairs = []
    for i in range(len(entropies) - 1):
        entropy_pairs.append((i, entropies[i] + entropies[i + 1]))

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
    entropy_pairs.sort(key=lambda x: x[1], reverse=True)

    # Print the top 10 entropy pairs.
    for i in range(10):
        print(entropy_pairs[i])


if __name__ == "__main__":
  main()
