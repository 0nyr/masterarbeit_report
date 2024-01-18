"""
Compute accuracy from TN, FP, FN, TP.
Determine best instance of each model with 
respect to the best selected metric:
accuracy, precision, recall and f1 score.
Generate LaTeX tables for each metric.
"""


import pandas as pd
from os.path import join
import os


INPUT_RESULT_CSV_PATH = "/home/onyr/code/phdtrack/predicting_ssh_key_masterarbeit_report/src/results/csv/concatenated_csv/concatenated_raw_result.csv"
OUTPUT_LATEX_TABLES_DIR_PATH = "/home/onyr/code/phdtrack/predicting_ssh_key_masterarbeit_report/src/results/tables"

def latex_escape(s):
    # Add LaTeX escape characters to the string
    return s.replace("_", "\\_")

def generate_latex_table(df, selected_metric):
    caption = f"Best instance for each model, with respect to {selected_metric}."
    latex_str = "    \\begin{table}\n"
    latex_str += "        \\centering\n"
    latex_str += f"        \\caption{{{caption}}}\n"
    latex_str += "        \\begin{tabular}{|l|c|c|c|c|c|c|} \\hline \n"
    latex_str += "          \\textbf{Model}  & \\textbf{Accuracy} & \\textbf{Precision} & \\textbf{Recall} & \\textbf{F1 Score} & \\textbf{Embedding}  \\\\ \\hline \n"

    # one row per model
    for index, row in df.iterrows():
        latex_str += f"            {row['model']} & {row['accuracy']} & {row['precision']} & {row['recall']} & {row['f1 score']} & {row['embedding']} \\\\ \\hline \n"
    
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
relevant_columns = ["subpipeline_name", "node_embedding", "precision_class_1", "recall_class_1", "f1_score_class_1", "AUC", "true_negatives", "false_positives", "false_negatives", "true_positives", "nb_input_graphs"]
df_filtered = df[relevant_columns]

# Create directory for LaTeX tables if it doesn't exist
if not os.path.exists(OUTPUT_LATEX_TABLES_DIR_PATH):
    os.makedirs(OUTPUT_LATEX_TABLES_DIR_PATH)

def compute_accuracy(row):
    """
    Compute accuracy from TN, FP, FN, TP.
    """
    tn = row["true_negatives"]
    fp = row["false_positives"]
    fn = row["false_negatives"]
    tp = row["true_positives"]

    return (tp + tn) / (tp + tn + fp + fn)

# create a new column for accuracy
df_filtered.loc[:, "accuracy"] = df_filtered.apply(compute_accuracy, axis=1)

metric_to_all_models_for_metric: dict[str, pd.DataFrame] = {}
latex_tables: list[str] = [] # tables to fill with LaTeX code for each metric
selected_metrics = ["accuracy", "precision_class_1", "recall_class_1", "f1_score_class_1"]
for metric in selected_metrics:
    # Group data by model (subpipeline_name)
    grouped = df_filtered.groupby("subpipeline_name")

    all_models_for_metric = pd.DataFrame()
    for model_name, group in grouped:
        current_res = pd.DataFrame()

        # for each model type, get the best model instance for this metric
        best_value = group[metric].max()

        # save this model stats
        current_res["model"] = [model_name]

        # save full row for this model best metric
        best_row = group[group[metric] == best_value]
        current_res["accuracy"] = [best_row["accuracy"].values[0]]
        current_res["precision"] = [best_row["precision_class_1"].values[0]]
        current_res["recall"] = [best_row["recall_class_1"].values[0]]
        current_res["f1 score"] = [best_row["f1_score_class_1"].values[0]]
        current_res["embedding"] = [best_row["node_embedding"].values[0]]

        all_models_for_metric = pd.concat([all_models_for_metric, current_res], ignore_index=True)

    # transform all float columns to string columns, with a maximum of 4 decimal places
    for column in all_models_for_metric.columns:
        if all_models_for_metric[column].dtype == "float64":
            all_models_for_metric[column] = all_models_for_metric[column].map(lambda x: f"{x:.4f}")

    # sort the result df with respect to the metric
    metric_name = metric.replace("_class_1", "").replace("_", " ").replace("node_", "")
    all_models_for_metric = all_models_for_metric.sort_values(by=[metric_name], ascending=False)

    # Generate LaTeX table
    current_metric_latex_table = generate_latex_table(all_models_for_metric, metric_name)
    latex_tables.append(current_metric_latex_table)
    latex_tables.append("\n\n")

    metric_to_all_models_for_metric[metric_name] = all_models_for_metric


# Now, we generate a last table with the best instance for each metric, no matter the model
def generate_latex_table_2(metric_to_all_models_for_metric: dict[str, pd.DataFrame]):
    caption = f"Best model instance for each metric."
    latex_str = "    \\begin{table}\n"
    latex_str += "        \\centering\n"
    latex_str += f"        \\caption{{{caption}}}\n"
    latex_str += "        \\begin{tabular}{|l|c|c|c|c|c|c|} \\hline \n"
    latex_str += "          \\textbf{Metric} & \\textbf{Model}  & \\textbf{Accuracy} & \\textbf{Precision} & \\textbf{Recall} & \\textbf{F1 Score} & \\textbf{Embedding}  \\\\ \\hline \n"

    # one row per model
    for metric, df in metric_to_all_models_for_metric.items():
        latex_str += f"            {metric} & {df['model'].values[0]} & {df['accuracy'].values[0]} & {df['precision'].values[0]} & {df['recall'].values[0]} & {df['f1 score'].values[0]} & {df['embedding'].values[0]} \\\\ \\hline \n"
    
    latex_str += "        \\end{tabular}\n"
    latex_str += "    \\end{table}\n"
    return latex_str

# Generate LaTeX table
latex_table = generate_latex_table_2(metric_to_all_models_for_metric)
latex_tables.append(latex_table)

# Save best metrics for each model to a .tex file
OUTPUT_CSV_FILE_PATH = join(OUTPUT_LATEX_TABLES_DIR_PATH, f"best_model_instances_per_selected_metrics.tex")
with open(OUTPUT_CSV_FILE_PATH, 'w') as f:
    f.write(f"% Generated by program: {os.path.basename(__file__)}\n\n")

    for latex_table in latex_tables:
        f.write(latex_table)

print(f"Saved tables to {OUTPUT_CSV_FILE_PATH}")

