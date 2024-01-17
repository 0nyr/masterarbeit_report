import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the data from both CSV files

RESULT_CSV_PATH = "/home/onyr/code/phdtrack/predicting_ssh_key_masterarbeit_report/src/results/csv/concatenated_csv/concatenated_raw_result_v2.csv"
PLOT_OUTPUT_DIR_PATH = "/home/onyr/code/phdtrack/predicting_ssh_key_masterarbeit_report/src/results/plots"

df = pd.read_csv(RESULT_CSV_PATH)

# Preprocess the dataframes (similar preprocessing steps for both dataframes)
for df in [df, df]:
    df["subpipeline_name"] = df["subpipeline_name"].str.replace("-pipeline", "")

# Remove the "-embedding" suffix from the node_embedding column
df["node_embedding"] = df["node_embedding"].str.replace("-embedding", "")
# replace "-" with \n in node_embedding column
df["node_embedding"] = df["node_embedding"].str.replace("-", "\n")

# Filter metrics for Class 1 for both dataframes
class1_metrics_embedding = df[["node_embedding", "subpipeline_name", "precision_class_1", "recall_class_1", "f1_score_class_1", "AUC"]]
class1_metrics_model = df[["subpipeline_name", "precision_class_1", "recall_class_1", "f1_score_class_1", "AUC"]]

# Create a palette based on unique subpipeline names (common for both dataframes)
unique_subpipelines = pd.concat([class1_metrics_embedding['subpipeline_name'], class1_metrics_model['subpipeline_name']]).unique()
palette = sns.color_palette("husl", len(unique_subpipelines))
palette_dict = dict(zip(unique_subpipelines, palette))

# Create subplots
fig, axes = plt.subplots(4, 2, figsize=(20, 16))  # 4 rows, 2 columns
metrics = ["precision_class_1", "recall_class_1", "f1_score_class_1", "AUC"]
titles = ["Precision for Class 1", "Recall for Class 1", "F1 Score for Class 1", "AUC for Class 1"]

# TODO: continue here

# Add a main title
fig.suptitle("Comparison of Embedding and Model Results for Class 1 (Key Prediction)", fontsize=18)

# Adjust layout
plt.tight_layout(rect=[0, 0, 1, 0.96])

# Save the plot
plt.savefig(f"{PLOT_OUTPUT_DIR_PATH}/combined_embedding_model_comparison_metrics.png")
