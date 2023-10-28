"""
This script generates the tables for the model results.

For each model, the following metrics (columns) are shown:
    Columns:
    - Best Precision for Class 1
    - Best Recall for Class 1
    - Best F1 Score for Class 1
    - Best AUC for Class 1

    Raws:
    - model

One result table is generated for each model.
"""

import pandas as pd
from os.path import join
import os


INPUT_RESULT_CSV_PATH = "/home/onyr/code/phdtrack/predicting_ssh_key_masterarbeit_report/src/results/csv/concatenated_csv/concatenated_raw_result.csv"
OUTPUT_LATEX_TABLES_DIR_PATH = "/home/onyr/code/phdtrack/predicting_ssh_key_masterarbeit_report/src/results/tables"

def latex_escape(s):
    # Add LaTeX escape characters to the string
    return s.replace("_", "\\_")

def generate_latex_table(df):
    caption = f"Best result metrics for the models."
    latex_str = "    \\begin{table}[H]\n"
    latex_str += "        \\centering\n"
    latex_str += f"        \\caption{{{caption}}}\n"
    latex_str += "        \\begin{tabular}{lcccccc}\n"
    latex_str += "          \\textbf{Model}  & \\textbf{Best Precision} & \\textbf{Best Recall} & \\textbf{Best F1 Score} & \\textbf{Best AUC} \\\\\n"

    # one row per model
    for index, row in df.iterrows():
        latex_str += f"            {row['Model']} & {row['Best precision']} & {row['Best recall']} & {row['Best f1 score']} & {row['Best AUC']} \\\\\n"

    latex_str += "        \\end{tabular}\n"
    latex_str += "    \\end{table}\n"
    return latex_str


# Load your concatenated csv file
df = pd.read_csv(INPUT_RESULT_CSV_PATH)

# print the number of rows and columns
print("Number of rows:", df.shape[0])
print("Number of columns:", df.shape[1])

# Remove the "-pipeline" suffix from the subpipeline_name column
df["subpipeline_name"] = df["subpipeline_name"].str.replace("-pipeline", "")

# Remove the "-embedding" suffix from the node_embedding column
df["node_embedding"] = df["node_embedding"].str.replace("-embedding", "")




# Filter metrics for Class 1 and other relevant columns
relevant_columns = ["subpipeline_name", "node_embedding", "precision_class_1", "recall_class_1", "f1_score_class_1", "AUC", "nb_input_graphs"]
df_filtered = df[relevant_columns]

# Create directory for LaTeX tables if it doesn't exist
if not os.path.exists(OUTPUT_LATEX_TABLES_DIR_PATH):
    os.makedirs(OUTPUT_LATEX_TABLES_DIR_PATH)

# Group data by model (subpipeline_name)
grouped = df_filtered.groupby("subpipeline_name")

all_model_best_metrics_df = pd.DataFrame()
for model_name, group in grouped:
    best_metrics_df = pd.DataFrame()

    # Calculate the best metrics
    for metric in ["precision_class_1", "recall_class_1", "f1_score_class_1", "AUC"]:
        best_value = group[metric].max()
        best_metrics_df[f"Best {metric.replace('_class_1', '').replace('_', ' ')}"] = [best_value]
        print(f"Best {metric.replace('_class_1', '').replace('_', ' ')} for {model_name}: {best_value}")
        
    best_metrics_df["Model"] = [model_name]

    # Add the best metrics for the model to the DataFrame containing the best metrics for all models
    all_model_best_metrics_df = pd.concat([all_model_best_metrics_df, best_metrics_df], ignore_index=True)  

# transform all float columns to string columns, with a maximum of 4 decimal places
for column in all_model_best_metrics_df.columns:
    if all_model_best_metrics_df[column].dtype == "float64":
        all_model_best_metrics_df[column] = all_model_best_metrics_df[column].map(lambda x: f"{x:.4f}")

latex_table = generate_latex_table(all_model_best_metrics_df)

# Save the LaTeX table to a .tex file
output_file_path = join(OUTPUT_LATEX_TABLES_DIR_PATH, f"best_model_metrics_results_table.tex")
with open(output_file_path, "w") as f:
    f.write(latex_table)

print(f"LaTeX table for best model metrics saved.")