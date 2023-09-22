

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