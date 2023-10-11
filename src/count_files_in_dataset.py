"""
Count the number of RAW file,
in every subdirectories of the given dataset
"""
import os
import statistics

def count_raw_files_in_subdir(subdir):
    count = 0
    for _, _, filenames in os.walk(subdir):
        for filename in filenames:
            if filename.endswith("-heap.raw"):
                count += 1
    return count

def main(dataset_dir):
    print("INPUT DIR:", dataset_dir)
    subdirs_raw_count = {}

    for subdir, _, _ in os.walk(dataset_dir):
        if not any(os.path.isdir(os.path.join(subdir, sub_subdir)) for sub_subdir in os.listdir(subdir)):
            # Only consider the lowest level subdirectories
            raw_count = count_raw_files_in_subdir(subdir)
            subdirs_raw_count[subdir] = raw_count

    if not subdirs_raw_count:
        print("No subdirectories with RAW files found.")
        return

    raw_counts = list(subdirs_raw_count.values())
    
    # Compute statistics
    median = statistics.median(raw_counts)
    print(statistics.quantiles(raw_counts, n=4))
    first_quartile = statistics.quantiles(raw_counts, n=4)[0]
    fourth_quartile = statistics.quantiles(raw_counts, n=4)[2]
    
    print(f"Median number of RAW files: {median}")

    # Identify subdirs in first and fourth quartiles
    first_quartile_subdirs = [subdir for subdir, count in subdirs_raw_count.items() if count <= first_quartile]
    fourth_quartile_subdirs = [subdir for subdir, count in subdirs_raw_count.items() if count >= fourth_quartile]
    
    print("\nSubdirectories in the first quartile:")
    for subdir in first_quartile_subdirs:
        print(subdir, "with", subdirs_raw_count[subdir], "RAW files")

    print("\nSubdirectories in the fourth quartile:")
    for subdir in fourth_quartile_subdirs:
        print(subdir, "with", subdirs_raw_count[subdir], "RAW files")

if __name__ == "__main__":
    dataset_dir = "/home/onyr/code/phdtrack/phdtrack_data_clean/Training/"  # Replace with your dataset directory path
    main(dataset_dir)

    dataset_dir = "/home/onyr/code/phdtrack/phdtrack_data_clean/Performance_Test/"  # Replace with your dataset directory path
    main(dataset_dir)

    dataset_dir = "/home/onyr/code/phdtrack/phdtrack_data_clean/Validation/"  # Replace with your dataset directory path
    main(dataset_dir)
