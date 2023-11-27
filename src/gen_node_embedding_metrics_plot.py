import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Replace these paths with your own
RESULT_CSV_PATH = "/home/onyr/code/phdtrack/predicting_ssh_key_masterarbeit_report/src/results/csv/concatenated_csv/concatenated_raw_result.csv"
PLOT_OUTPUT_DIR_PATH = "/home/onyr/code/phdtrack/predicting_ssh_key_masterarbeit_report/src/results/plots"

# Load the DataFrame
df = pd.read_csv(RESULT_CSV_PATH)

# Remove the "-pipeline" suffix from the subpipeline_name column
df["subpipeline_name"] = df["subpipeline_name"].str.replace("-pipeline", "")

# Remove the "-embedding" suffix from the node_embedding column
df["node_embedding"] = df["node_embedding"].str.replace("-embedding", "")
# replace "-" with \n in node_embedding column
df["node_embedding"] = df["node_embedding"].str.replace("-", "\n")

# Filter metrics for Class 1
class1_metrics = df[["node_embedding", "subpipeline_name", "precision_class_1", "recall_class_1", "f1_score_class_1", "AUC"]]

# Create a palette based on unique subpipeline names
unique_subpipelines = class1_metrics['subpipeline_name'].unique()
palette = sns.color_palette("husl", len(unique_subpipelines))
palette_dict = dict(zip(unique_subpipelines, palette))

# Create subplots
fig, axes = plt.subplots(4, 1, figsize=(14, 16))
axes = axes.flatten()
metrics = ["precision_class_1", "recall_class_1", "f1_score_class_1", "AUC"]
titles = ["Precision for Class 1", "Recall for Class 1", "F1 Score for Class 1", "AUC for Class 1"]

for i, (ax, metric, title) in enumerate(zip(axes, metrics, titles)):
    # Draw stripplot first
    sns.stripplot(x="node_embedding", y=metric, data=class1_metrics, ax=ax, hue="subpipeline_name", palette=palette_dict, jitter=0.2, dodge=True)
    
    # Draw violinplot on top
    violin = sns.violinplot(x="node_embedding", y=metric, data=class1_metrics, ax=ax, hue="subpipeline_name", palette=palette_dict, inner="quart", width=0.9, dodge=True, facecolor=None, edgecolor="black", linewidth=1.5)
    violin.set_facecolor('none')

    # Number of unique node_embedding values
    num_violins = len(class1_metrics['node_embedding'].unique())
    
    # Modify violinplot to only show the silhouette
        
    ax.set_title(title)
    ax.legend(title='Model', bbox_to_anchor=(1.05, 1), loc='upper left')

# Add a title
fig.suptitle("Impact of Node Embeddings on Model Metrics for Class 1 (Key prediction)", fontsize=16)

# Tight layout
plt.tight_layout(rect=[0, 0, 1, 1])

# Save the plot
plt.savefig(f"{PLOT_OUTPUT_DIR_PATH}/embedding_comparison_metrics_v2.png")
