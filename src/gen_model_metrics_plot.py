import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

RESULT_CSV_PATH = "/home/onyr/code/phdtrack/predicting_ssh_key_masterarbeit_report/src/results/csv/concatenated_csv/concatenated_raw_result_v2.csv"
PLOT_OUTPUT_DIR_PATH = "/home/onyr/code/phdtrack/predicting_ssh_key_masterarbeit_report/src/results/plots"

# Load your concatenated csv file
df = pd.read_csv(RESULT_CSV_PATH)

# print the number of rows and columns
print("Number of rows:", df.shape[0])
print("Number of columns:", df.shape[1])

# remove the "-pipeline" suffix from the subpipeline_name column
df["subpipeline_name"] = df["subpipeline_name"].str.replace("-pipeline", "")

# Filter metrics for Class 1
class1_metrics = df[["subpipeline_name", "precision_class_1", "recall_class_1", "f1_score_class_1", "AUC"]]

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
    sns.stripplot(x="subpipeline_name", y=metric, data=class1_metrics, ax=ax, palette=palette_dict, jitter=0.2, dodge=False, hue="subpipeline_name")
    
    # Draw violinplot on top
    violin = sns.violinplot(x="subpipeline_name", y=metric, data=class1_metrics, ax=ax, palette=palette_dict, hue="subpipeline_name", inner="quart", width=0.9, dodge=False, facecolor=None, edgecolor="black", linewidth=1.5)
    violin.set_facecolor('none')

    # Number of unique subpipeline_names
    num_violins = len(class1_metrics['subpipeline_name'].unique())
    
    # Modify violinplot to only show the silhouette
    for violin in ax.collections[num_violins:]:  # Only select the violin collections
        violin.set_facecolor('none')
        violin.set_edgecolor('black')  # or any color you like
        violin.set_linewidth(1.5)
        
    ax.set_title(title)




# remove legend
for ax in axes:
    ax.legend_.remove()

# Add a title
fig.suptitle("Metrics for Class 1 (Key prediction), model comparisons.", fontsize=16)

plt.tight_layout(rect=[0, 0, 1, 0.96])
plt.savefig(f"{PLOT_OUTPUT_DIR_PATH}/models_comparison_metrics.png")
