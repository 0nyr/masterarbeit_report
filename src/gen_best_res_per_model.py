"""
This script generates the unique table for each model best results.

For each model, considering we have 4 metrics 
(precision, recall, f1 score, AUC) and 2 classes (0 and 1), 
we display a table with 4 rows showing the metrics of the 4 model
instances with the best results for each metric.

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

def generate_latex_table(df, model_name):
    caption = f"Best instances of model: {model_name}."
    latex_str = "    \\begin{table}[H]\n"
    latex_str += "        \\centering\n"
    latex_str += f"        \\caption{{{caption}}}\n"
    latex_str += "        \\begin{tabular}{lcccccc}\n"
    latex_str += "          \\textbf{Best at}  & \\textbf{Precision} & \\textbf{Recall} & \\textbf{F1 Score} & \\textbf{AUC} \\\\\n"

    # one row per model
    for index, row in df.iterrows():
        latex_str += f"            {row['best_at']} & {row['precision']} & {row['recall']} & {row['f1 score']} & {row['AUC']} \\\\\n"

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

latex_tables: list[str] = []
for model_name, group in grouped:
    best_metrics_df = pd.DataFrame()

    # Calculate the best metrics
    for metric in ["precision_class_1", "recall_class_1", "f1_score_class_1", "AUC"]:
        best_value = group[metric].max()
        current_res = pd.DataFrame()
        current_res["best_at"] = [metric.replace('_class_1', '').replace('_', ' ')]

        # save full row for this model best metric
        best_row = group[group[metric] == best_value]
        current_res["precision"] = [best_row["precision_class_1"].values[0]]
        current_res["recall"] = [best_row["recall_class_1"].values[0]]
        current_res["f1 score"] = [best_row["f1_score_class_1"].values[0]]
        current_res["AUC"] = [best_row["AUC"].values[0]]

        best_metrics_df = pd.concat([best_metrics_df, current_res], ignore_index=True)
    
    # transform all float columns to string columns, with a maximum of 4 decimal places
    for column in best_metrics_df.columns:
        if best_metrics_df[column].dtype == "float64":
            best_metrics_df[column] = best_metrics_df[column].map(lambda x: f"{x:.4f}")

    latex_table = generate_latex_table(best_metrics_df, model_name)
    latex_tables.append(latex_table)

# Save the LaTeX table to a .tex file
output_file_path = join(OUTPUT_LATEX_TABLES_DIR_PATH, f"best_models_by_metrics.tex")
with open(output_file_path, "w") as f:
    f.write("\n\n".join(latex_tables))

print(f"LaTeX table for all best models metrics saved.")