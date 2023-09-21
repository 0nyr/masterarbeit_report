"""
This script checks the correctness of the annotations in the JSON files.

It checks the following:
    - The presence of the following keys: 
        + HEAP_START, 
        + SSH_STRUCT_ADDR, 
        + SESSION_STATE_ADDR
    - The presence of the following keys for each key:
        + KEY_NAME_ADDR,
        + KEY_NAME_LEN,
        + KEY_NAME_REAL_LEN

The script creates a CSV file containing the invalid JSON files, with 
information about the errors.
"""

import json
import csv
from tqdm import tqdm

from utils.mem_utils import hex_str_to_addr
from utils.file_loading import get_all_nested_files

DEBUG = False

INPUT_DIR_PATH = "/home/onyr/code/phdtrack/phdtrack_data/"
#INPUT_DIR_PATH = "/home/onyr/code/phdtrack/predicting_ssh_key_masterarbeit_report/src/test_files"
CSV_REPORT_PATH = "/home/onyr/code/phdtrack/predicting_ssh_key_masterarbeit_report/src/results/malformed_json_files_report.csv"  # Replace this with your directory path
TXT_BROKEN_FILES_PATH = "/home/onyr/code/phdtrack/predicting_ssh_key_masterarbeit_report/src/results/broken_json_files.txt"  # Replace this with your directory path

def dp(*args, **kwargs):
    """
    Debug print.
    """
    if DEBUG:
        print(*args, **kwargs)

def is_hex_address_correct(value: str) -> bool:
    try:
        int_addr_value = hex_str_to_addr(value)
        assert int_addr_value > 0       # check value is greater than 0
        assert int_addr_value % 8 == 0  # check value is 8 bytes aligned

        return True
    except ValueError:
        return False
    except AssertionError:
        return False

def is_a_number(value: str | int) -> bool:
    """
    Check if a value is a number.
    """
    try:
        int(value)
        return True
    except ValueError:
        return False

def validate_json(json_data: dict) -> dict:
    errors = {}
    mandatory_json_keys = ['HEAP_START', 'SSH_STRUCT_ADDR', 'SESSION_STATE_ADDR']

    dp("file:", json_data["file"])
    
    for key in mandatory_json_keys:
        if key not in json_data or not is_hex_address_correct(json_data[key]):
            errors[key] = False
        else:
            errors[key] = True

    # get all key names
    key_names: list[str] = set()
    for keys in json_data.keys():
        if keys.startswith("KEY_"):
            # get first letter after "KEY_"
            key_name = keys.split("_")[1]
            key_names.add(key_name)

    # check keys
    incorrect_keys = 0
    missing_keys = 0
    incomplete_keys = 0
    error_messages: list[str] = []
    for key_letter in key_names:
        base_key = "KEY_" + key_letter
        
        # case missing key
        if len(json_data[base_key]) == 0:
            missing_keys += 1
        else:
            # check if related JSON keys for given SSH key are present
            is_key_len_present = f"{base_key}_LEN" in json_data
            is_key_addr_present = f"{base_key}_ADDR" in json_data
            is_key_real_len_present = f"{base_key}_REAL_LEN" in json_data
            if not is_key_len_present or not is_key_addr_present or not is_key_real_len_present:
                incomplete_keys += 1

                missing_related_keys_str = ""
                if not is_key_len_present:
                    missing_related_keys_str += f"{base_key}_LEN, "
                if not is_key_addr_present:
                    missing_related_keys_str += f"{base_key}_ADDR, "
                if not is_key_real_len_present:
                    missing_related_keys_str += f"{base_key}_REAL_LEN, "
                
                message = f"Key {base_key} is missing related annotations ({missing_related_keys_str[:-2]})."
                error_messages.append(message)
                dp(message)
            # check SSH key address
            elif not is_hex_address_correct(json_data[f"{base_key}_ADDR"]):
                incorrect_keys += 1
                message = f"Key {base_key} has incorrect address."
                error_messages.append(message)
                dp(message)
            # check the length is a non-negative integer
            elif not is_a_number(json_data[f"{base_key}_LEN"]) or int(json_data[f"{base_key}_LEN"]) < 0:
                incorrect_keys += 1
                key_val = json_data[f"{base_key}_LEN"]
                message = f"Key {base_key} has incorrect length: {key_val}"
                error_messages.append(message)
                dp(message)
            # check Key value length from given annotation length
            # NOTE: since we are expecting hex values, the nb of chars should be twice the nb of bytes
            else:
                # case length is 0 (empty or missing key)
                if int(json_data[f"{base_key}_LEN"]) == 0:
                    missing_keys += 1
                # case length is not 0 and KEY_X is not empty string, check lengths are equal
                elif len(json_data[base_key]) != int(json_data[f"{base_key}_LEN"])*2:
                    incorrect_keys += 1
                    message = f"Key {base_key} has incorrect key value length ({len(json_data[base_key])} != {int(json_data[f'{base_key}_LEN'])*2})"
                    error_messages.append(message)
                    dp(message)

    errors["total_keys"] = len(key_names)
    errors["incorrect_keys"] = incorrect_keys
    errors["missing_keys"] = missing_keys
    errors["incomplete_keys"] = incomplete_keys
    errors["error_messages"] = " ".join(error_messages)
    
    return errors

def main():
    json_file_paths = get_all_nested_files(INPUT_DIR_PATH, "json")
    print(f"Total number of JSON files to check: {len(json_file_paths)}")
    
    total_files = 0
    incorrect_files = 0         # files with incorrect annotations
    files_with_incomplete_keys = 0        # files with incomplete annotations for non empty keys
    files_with_empty_keys = 0         # file with empty keys
    broken_files = 0            # files that are not JSON
    broken_file_paths = []      # paths of broken files
    files_with_missing_heap_start = 0
    files_correct_complete = 0
    total_number_of_keys = 0
    total_incomplete_keys = 0
    total_incorrect_keys = 0
    total_missing_keys = 0

    with open(CSV_REPORT_PATH, "w", newline='') as csvfile:
        fieldnames = [
            "File Path",
            "Status",
            "Total Keys", 
            "Incorrect Keys",
            "Incomplete Keys",
            "HEAP_START", 
            "SSH_STRUCT_ADDR", 
            "SESSION_STATE_ADDR",
            "Error Messages",
        ]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        
        writer.writeheader()
        
        for file_path in tqdm(json_file_paths, desc="Processing files"):
            total_files += 1
            with open(file_path, 'r') as f:
                try:
                    json_data = json.load(f)
                except json.JSONDecodeError:
                    broken_files += 1
                    broken_file_paths.append(file_path)
                    continue

            json_data["file"] = file_path

            errors = validate_json(json_data)

            # counting
            total_number_of_keys += errors["total_keys"]
            total_missing_keys += errors["missing_keys"]
            total_incomplete_keys += errors["incomplete_keys"]
            total_incorrect_keys += errors['incorrect_keys']

            if errors["incorrect_keys"] > 0:
                incorrect_files += 1
            if errors["incomplete_keys"] > 0:
                files_with_incomplete_keys += 1
            if errors["HEAP_START"] == False:
                files_with_missing_heap_start += 1
            if errors["missing_keys"] > 0:
                files_with_empty_keys += 1
            if errors["incorrect_keys"] == 0 and errors["incomplete_keys"] == 0 and errors["missing_keys"] == 0:
                files_correct_complete += 1
            
            # write to CSV file if JSON is incorrect
            if errors["incorrect_keys"] > 0 or errors["incomplete_keys"] > 0:

                if errors["incorrect_keys"] > 0:
                    status = "incorrect"
                elif errors["incomplete_keys"] > 0:
                    status = "incomplete"
                
                writer.writerow({
                    "File Path": file_path,
                    "Status": status,
                    "Total Keys": errors["total_keys"],
                    "Incorrect Keys": errors["incorrect_keys"],
                    "Incomplete Keys": errors["incomplete_keys"],
                    "HEAP_START": errors["HEAP_START"],
                    "SSH_STRUCT_ADDR": errors["SSH_STRUCT_ADDR"],
                    "SESSION_STATE_ADDR": errors["SESSION_STATE_ADDR"],
                    "Error Messages": errors["error_messages"],
                })
    
    # save broken files to txt file
    with open(TXT_BROKEN_FILES_PATH, "w") as f:
        for file_path in broken_file_paths:
            f.write(file_path + "\n")
    
    # print stats
    print(f"Total number of checked JSON files: {total_files}")
    print(f"Total number of correct and complete annotated JSON files: {files_correct_complete}")
    print(f"Total number of broken JSON files: {broken_files}")
    print(f"Total number of JSON annotation files with incomplete_keys: {files_with_incomplete_keys}")
    print(f"Total number of incorrect JSON annotation files: {incorrect_files}")
    print(f"Total number of JSON annotation files with empty keys: {files_with_empty_keys}")
    print(f"Total number of files with missing HEAP_START: {files_with_missing_heap_start}")
    print(f"Total number of SSH keys: {total_number_of_keys}")
    print(f"Total number of missing (empty) SSH keys: {total_missing_keys}")
    print(f"Total number of incompletly annotated SSH keys: {total_incomplete_keys}")
    print(f"Total number of incorrectly annotated SSH keys: {total_incorrect_keys}")

if __name__ == "__main__":
    main()
