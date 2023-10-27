import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

RESULT_CSV_PATH = "/home/onyr/code/phdtrack/predicting_ssh_key_masterarbeit_report/src/results/csv/concatenated_csv/concatenated_raw_result.csv"
GRAPH_OUTPUT_DIR_PATH = "/home/onyr/code/phdtrack/predicting_ssh_key_masterarbeit_report/src/results/plots"

# Load your concatenated csv file
df = pd.read_csv(RESULT_CSV_PATH)

# Filter metrics for Class 1
class1_metrics = df[["subpipeline_name", "precision_class_1", "recall_class_1", "f1_score_class_1", "AUC"]]

# Create subplots
fig, axes = plt.subplots(4, 1, figsize=(14, 16))
axes = axes.flatten()
metrics = ["precision_class_1", "recall_class_1", "f1_score_class_1", "AUC"]
titles = ["Precision for Class 1", "Recall for Class 1", "F1 Score for Class 1", "AUC for Class 1"]

for i, (ax, metric, title) in enumerate(zip(axes, metrics, titles)):
    sns.boxplot(x="subpipeline_name", y=metric, data=class1_metrics, ax=ax)
    ax.set_title(title)

# Add a unique legend
handles, labels = axes[-1].get_legend_handles_labels()
fig.legend(handles, labels, loc='upper center')

plt.tight_layout(rect=[0, 0, 1, 0.96])
plt.savefig(f"{GRAPH_OUTPUT_DIR_PATH}/models_comparison_metrics.png")

