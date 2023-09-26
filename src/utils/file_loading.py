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