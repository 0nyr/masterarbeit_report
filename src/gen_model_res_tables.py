"""
This script generates the tables for the model results.

For each model, the following metrics (columns) are shown:
    Columns:
    - Precision for Class 1
    - Recall for Class 1
    - F1 Score for Class 1
    - AUC for Class 1
    - Node embedding
    - Number of input graphs

    Raws:
    - Best precision of the model for Class 1
    - Best recall of the model for Class 1
    - Best F1 score of the model for Class 1
    - Best AUC of the model for Class 1

One result table is generated for each model.
"""

import pandas as pd

INPUT_RESULT_CSV_PATH = "/home/onyr/code/phdtrack/predicting_ssh_key_masterarbeit_report/src/results/csv/concatenated_csv/concatenated_raw_result.csv"
OUTPUT_LATEX_TABLES_DIR_PATH = "/home/onyr/code/phdtrack/predicting_ssh_key_masterarbeit_report/src/results/tables"

# Load your concatenated csv file
df = pd.read_csv(INPUT_RESULT_CSV_PATH)

# print the number of rows and columns
print("Number of rows:", df.shape[0])
print("Number of columns:", df.shape[1])

# Remove the "-pipeline" suffix from the subpipeline_name column
df["subpipeline_name"] = df["subpipeline_name"].str.replace("-pipeline", "")

# Remove the "-embedding" suffix from the node_embedding column
df["node_embedding"] = df["node_embedding"].str.replace("-embedding", "")

# ...
from os.path import join

# Filter metrics for Class 1 and other relevant columns
relevant_columns = ["subpipeline_name", "node_embedding", "precision_class_1", "recall_class_1", "f1_score_class_1", "AUC", "nb_input_graphs"]
df_filtered = df[relevant_columns]

# Group data by model (subpipeline_name)
grouped = df_filtered.groupby("subpipeline_name")

for model_name, group in grouped:
    # Create a DataFrame to hold the best metrics for each model
    best_metrics_df = pd.DataFrame()

    # Calculate the best metrics
    best_metrics_df["Best precision for Class 1"] = [group["precision_class_1"].max()]
    best_metrics_df["Best recall for Class 1"] = [group["recall_class_1"].max()]
    best_metrics_df["Best F1 score for Class 1"] = [group["f1_score_class_1"].max()]
    best_metrics_df["Best AUC for Class 1"] = [group["AUC"].max()]

    # Add node_embedding and nb_input_graphs of the best metrics
    for metric in ["precision_class_1", "recall_class_1", "f1_score_class_1", "AUC"]:
        best_row = group[group[metric] == group[metric].max()].iloc[0]
        best_metrics_df[f"Node embedding for best {metric}"] = best_row["node_embedding"]
        best_metrics_df[f"Number of input graphs for best {metric}"] = best_row["nb_input_graphs"]
    
    # Convert the DataFrame to a LaTeX table
    latex_table = best_metrics_df.to_latex(index=False)

    # Save the LaTeX table to a .tex file
    output_file_path = join(OUTPUT_LATEX_TABLES_DIR_PATH, f"{model_name}_results_table.tex")
    with open(output_file_path, "w") as f:
        f.write(latex_table)

    print(f"LaTeX table for {model_name} saved.")
