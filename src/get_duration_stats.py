"""
Get the duration stats for each model.
"""

import pandas as pd
from os.path import join
import os


INPUT_RESULT_CSV_PATH = "/home/onyr/code/phdtrack/predicting_ssh_key_masterarbeit_report/src/results/csv/concatenated_csv/concatenated_raw_result.csv"
OUTPUT_LATEX_TABLES_DIR_PATH = "/home/onyr/code/phdtrack/predicting_ssh_key_masterarbeit_report/src/results/tables"

def latex_escape(s):
    # Add LaTeX escape characters to the string
    return s.replace("_", "\\_")

def generate_latex_table(df, duration_for: str):
    caption = f"Duration times for {duration_for} (in seconds).)"
    latex_str = "    \\begin{table}[H]\n"
    latex_str += "        \\centering\n"
    latex_str += f"        \\caption{{{caption}}}\n"
    latex_str += "        \\begin{tabular}{lcccccc}\n"
    latex_str += "          \\textbf{Model}  & \\textbf{Min duration} & \\textbf{Max duration} & \\textbf{Min duration} \\\\\n"

    # one row per model
    for index, row in df.iterrows():
        latex_str += f"            {index} & {row['mean']} & {row['max']} & {row['min']} \\\\\n"

    latex_str += "        \\end{tabular}\n"
    latex_str += "    \\end{table}\n"
    return latex_str

latex_tables: list[str] = []

# Load your concatenated csv file
df = pd.read_csv(INPUT_RESULT_CSV_PATH)

# print the number of rows and columns
print("Number of rows:", df.shape[0])
print("Number of columns:", df.shape[1])

# Remove the "-pipeline" suffix from the subpipeline_name column
df["subpipeline_name"] = df["subpipeline_name"].str.replace("-pipeline", "")

# Remove the "-embedding" suffix from the node_embedding column
df["node_embedding"] = df["node_embedding"].str.replace("-embedding", "")

# remove all rows where the "nb_input_graphs" != 16
df = df[df["nb_input_graphs"] == 16]

# count the average duration_embedding (in seconds) for each model
# EX: duration_embedding =  94.191921 total sec (00h 01m 34s)
# first, remove the " sec (00h 01m 34s)" part, and convert the string to float
df["duration_embedding"] = df['duration_embedding'].str.extract(r'(\d+\.\d+)').astype(float)

mean_duration_embedding = df.groupby("subpipeline_name")["duration_embedding"].mean()
print(f"Mean of duration_embedding: {mean_duration_embedding}")
max_duration_embedding = df.groupby("subpipeline_name")["duration_embedding"].max()
print(f"Max of duration_embedding: {max_duration_embedding}")
min_duration_embedding = df.groupby("subpipeline_name")["duration_embedding"].min()
print(f"Min of duration_embedding: {min_duration_embedding}")

df_duration_embedding = pd.concat([mean_duration_embedding, max_duration_embedding, min_duration_embedding], axis=1)
df_duration_embedding.columns = ["mean", "max", "min"]
print(df_duration_embedding)
latex_tables.append(
    generate_latex_table(df_duration_embedding, "duration of embedding generation in ML/DL/FE pipeline")
)

# count the average duration_train_test in seconds for each model
# EX: duration_train_test =  0.000000 total sec (00h 00m 00s)
df["duration_train_test"] = df['duration_train_test'].str.extract(r'(\d+\.\d+)').astype(float)

mean_duration_train_test = df.groupby("subpipeline_name")["duration_train_test"].mean()
print(f"Mean of duration_train_test: {mean_duration_train_test}")
max_duration_train_test = df.groupby("subpipeline_name")["duration_train_test"].max()
print(f"Max of duration_train_test: {max_duration_train_test}")
min_duration_train_test = df.groupby("subpipeline_name")["duration_train_test"].min()
print(f"Min of duration_train_test: {min_duration_train_test}")

df_duration_train_test = pd.concat([mean_duration_train_test, max_duration_train_test, min_duration_train_test], axis=1)
df_duration_train_test.columns = ["mean", "max", "min"]
print(df_duration_train_test)
# modify column names

latex_tables.append(
    generate_latex_table(df_duration_train_test, "duration of training and testing in ML/DL/FE pipeline")
)

# Save the LaTeX table to a .tex file
output_file_path = join(OUTPUT_LATEX_TABLES_DIR_PATH, f"duration_tables.tex")
with open(output_file_path, "w") as f:
    f.write("\n\n".join(latex_tables))

print(f"LaTeX table for all duration saved.")