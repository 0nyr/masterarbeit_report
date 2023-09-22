"""
Load all json files and the blocks of the heap dump file.
Check that, when the SESSION_STATE_ADDR annotation is present,
the corresponding block is not composed of only zeros.
"""
from tqdm import tqdm

from utils.file_loading import get_all_nested_files
from utils.heap_dump import convert_int_address_to_block_index, get_blocks_from_heap_dump
from utils.json_annotation import get_json_annotations
from utils.mem_utils import hex_str_to_addr


INPUT_DIR_PATH = "/home/onyr/code/phdtrack/phdtrack_data_clean/"

def main():
    json_file_paths = get_all_nested_files(INPUT_DIR_PATH, "json")
    print(f"Total number of JSON files to check: {len(json_file_paths)}")
    
    nb_checked_files = 0
    nb_skipped_files = 0
    nb_files_with_session_state_addr_as_zeros = 0

    for json_file_path in tqdm(json_file_paths, desc="Processing files"):
        nb_checked_files += 1

        try:
            json_annotations = get_json_annotations(json_file_path)
        except:
            nb_skipped_files += 1
            continue
        
        if "SESSION_STATE_ADDR" not in json_annotations:
            nb_skipped_files += 1
            continue
        
        associated_heap_dump_file_path = json_file_path.replace(".json", "-heap.raw")
        
        # Split the data into blocks of 8 bytes.
        blocks = get_blocks_from_heap_dump(
            associated_heap_dump_file_path
        )

        # Check that the block corresponding to the SESSION_STATE_ADDR annotation is not composed of only zeros.
        heap_start_addr = hex_str_to_addr(json_annotations["HEAP_START"])
        session_state_addr = hex_str_to_addr(json_annotations["SESSION_STATE_ADDR"])
        session_state_block_index = convert_int_address_to_block_index(
            session_state_addr, 
            heap_start_addr
        )
        session_state_block = blocks[session_state_block_index]
        if session_state_block.sum() == 0:
            print(f"SESSION_STATE_ADDR annotation in {json_file_path} is associated with a block composed of only zeros.")
            nb_files_with_session_state_addr_as_zeros += 1

    print(f"Total number of checked files: {nb_checked_files}")
    print(f"Total number of skipped files: {nb_skipped_files}")
    print(f"Total number of files with SESSION_STATE_ADDR as block of 0s: {nb_files_with_session_state_addr_as_zeros}")



if __name__ == "__main__":
    main()