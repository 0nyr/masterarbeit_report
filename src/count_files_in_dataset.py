"""
Count the number of RAW file,
in every subdirectories of the given dataset
"""
import os
import statistics

def generate_latex_list_from_paths(paths : list[str]) -> str:
    def format_path_for_latex(path):
        # Split the path into its components
        parts = path.split('/')
        
        # Get the last four folders
        last_four = parts[-4:]
        
        # Format for LaTeX item
        latex_item = "\\item Use case: {use_case}, OpenSSH version: {openssh_version}, Key size: {key_size}".format(
            use_case=last_four[1], 
            openssh_version=last_four[2], 
            key_size=last_four[3]
        )
        
        return latex_item
    
    if len(paths) == 0:
        return ""

    # Extract the subset from the first path (assuming all paths have the same subset)
    subset = paths[0].split('/')[-4]

    latex_list : str = "\\textbf{" + subset + "}\n"
    latex_list += "\\begin{itemize}\n"
    for path in paths:
        latex_list += "    " + format_path_for_latex(path) + "\n"
    latex_list += "\\end{itemize}"

    return latex_list

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
    empty_subdirs = []

    for subdir, _, _ in os.walk(dataset_dir):
        if not any(os.path.isdir(os.path.join(subdir, sub_subdir)) for sub_subdir in os.listdir(subdir)):
            # Only consider the lowest level subdirectories
            raw_count = count_raw_files_in_subdir(subdir)
            if raw_count > 0:
                subdirs_raw_count[subdir] = raw_count
            else:
                empty_subdirs.append(subdir)

    if not subdirs_raw_count:
        print("No subdirectories with RAW files found.")
        return

    print(f"Number of empty subdirectories: {len(empty_subdirs)}")
    print(generate_latex_list_from_paths(empty_subdirs))

    print(f"Number of subdirectories with RAW files: {len(subdirs_raw_count)}")

    raw_counts = list(subdirs_raw_count.values())

    # Compute statistics
    median = statistics.median(raw_counts)
    quartiles = statistics.quantiles(raw_counts, n=4)
    print(quartiles)
    first_quartile = quartiles[0]
    fourth_quartile = quartiles[2]

    print(f"Median number of RAW files: {median}")
    print(f"min number of RAW files: {min(raw_counts)}")
    print(f"max number of RAW files: {max(raw_counts)}")

    # Identify subdirs in first and fourth quartiles
    first_quartile_subdirs = [subdir for subdir, count in subdirs_raw_count.items() if count <= first_quartile]
    fourth_quartile_subdirs = [subdir for subdir, count in subdirs_raw_count.items() if count >= fourth_quartile]

    print("\nSubdirectories in the first quartile:")
    for subdir in first_quartile_subdirs:
        print(subdir, "with", subdirs_raw_count[subdir], "RAW files")

    print(generate_latex_list_from_paths(first_quartile_subdirs))

    print("\nSubdirectories in the fourth quartile:")
    for subdir in fourth_quartile_subdirs:
        print(subdir, "with", subdirs_raw_count[subdir], "RAW files")

    print(generate_latex_list_from_paths(fourth_quartile_subdirs))

    print(f"END OF DIRECTORY {dataset_dir}\n\n")

if __name__ == "__main__":
    dataset_dir = "/home/onyr/code/phdtrack/phdtrack_data_clean/Training/"  # Replace with your dataset directory path
    main(dataset_dir)

    dataset_dir = "/home/onyr/code/phdtrack/phdtrack_data_clean/Performance_Test/"  # Replace with your dataset directory path
    main(dataset_dir)

    dataset_dir = "/home/onyr/code/phdtrack/phdtrack_data_clean/Validation/"  # Replace with your dataset directory path
    main(dataset_dir)
