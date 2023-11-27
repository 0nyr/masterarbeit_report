import os
import pandas as pd

"""
This script is used to concatenate all the raw csv files into one csv file.
It first reads all the csv files in the RAW_CSV_DIR_PATH directory, 
then it checks the header of each csv file to make sure that they are all the same,
then it concatenates them into one csv file.

The concatenated csv file is saved in the RAW_CSV_DIR_PATH directory.
"""

RAW_CSV_DIR_PATH = "src/results/csv/raw_result_csv_v2"
CONCAT_OUTPUT_DIR_PATH = "src/results/csv/concatenated_csv"
CONCAT_CSV_FILENAME = "concatenated_raw_result_v2.csv"

def concatenate_csv_files(dir_path):
    files = [f for f in os.listdir(dir_path) if f.endswith('.csv')]

    print(f"Found {len(files)} csv files in {dir_path}")
    for file in files:
        print(f"    -> \t{file}")

    # Initialize an empty DataFrame and a variable to store the expected header
    concatenated_df = pd.DataFrame()
    expected_header = None

    for file in files:
        file_path = os.path.join(dir_path, file)
        df = pd.read_csv(file_path)

        # Check the header of the csv file
        if expected_header is None:
            expected_header = df.columns.tolist()
        else:
            if df.columns.tolist() != expected_header:
                print(f"Header in {file} does not match the expected header. Skipping this file.")
                # show the difference between the expected header and the actual header
                missing_columns = set(expected_header) - set(df.columns.tolist())
                print(f"    -> Difference: {set(expected_header) - set(df.columns.tolist())}")
                print("Adding those columns to the DataFrame with None values.")
                for column in missing_columns:
                    df[column] = None
                

        # Append the DataFrame to the concatenated DataFrame
        concatenated_df = pd.concat([concatenated_df, df])

    # Save the concatenated DataFrame as a new csv file
    output_file_path = os.path.join(
        CONCAT_OUTPUT_DIR_PATH, CONCAT_CSV_FILENAME
    )
    concatenated_df.to_csv(output_file_path, index=False)
    print(f"Concatenated csv files saved as {output_file_path}")

if __name__ == "__main__":
    concatenate_csv_files(RAW_CSV_DIR_PATH)
