import os
import glob

def get_all_nested_files(
        dir_path: str, 
        extension: str | None = None
) -> list[str]:
    """
    Get all nested files in a directory.
    """
    # use glob to get all files
    print(f"Getting all files in {dir_path}...")
    all_files: list[str]
    if extension is None:
        all_files = glob.glob(os.path.join(dir_path, "**"), recursive=True)
    else:
        all_files = glob.glob(os.path.join(dir_path, "**", f"*{extension}"), recursive=True)
    
    print(f"Found {len(all_files)} files in {dir_path}.")
    # filter out directories
    all_files = [file for file in all_files if os.path.isfile(file)]

    return all_files

def delete_json_and_raw_file(file_path: str) -> None:
    """
    Delete the JSON annotation file and its corresponding heap dump file.
    """
    if file_path.endswith(".json"):
        json_file_path = file_path
        raw_file_path = json_file_path.replace(".json", "-heap.raw")
    elif file_path.endswith("-heap.raw"):
        raw_file_path = file_path
        json_file_path = raw_file_path.replace("-heap.raw", ".json")
    else:
        raise ValueError(
            f"Invalid file path: {file_path}. "
            "Expected a JSON file (.json) or a heap dump file (-heap.raw)."
        )

    print(f"Deleting {json_file_path} and {raw_file_path}")
    os.remove(json_file_path)
    os.remove(raw_file_path)
