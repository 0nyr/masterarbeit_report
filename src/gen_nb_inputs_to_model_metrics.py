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

# Filter out rows where precision_class_1 or recall_class_1 is 0
df_filtered = df[(df["precision_class_1"] != 0) & (df["recall_class_1"] != 0)]

# Filter metrics for Class 1
class1_metrics = df_filtered[["subpipeline_name", "nb_input_graphs", "precision_class_1", "recall_class_1", "f1_score_class_1", "AUC"]]

# Create a palette based on unique subpipeline names
unique_subpipelines = class1_metrics['subpipeline_name'].unique()
palette = sns.color_palette("husl", len(unique_subpipelines))
palette_dict = dict(zip(unique_subpipelines, palette)) # type: ignore

# Create subplots
fig, axes = plt.subplots(4, 1, figsize=(14, 16))

metrics = ["precision_class_1", "recall_class_1", "f1_score_class_1", "AUC"]
titles = ["Precision for Class 1", "Recall for Class 1", "F1 Score for Class 1", "AUC for Class 1"]

# Draw 4 subplots, one for each metric
# Each subplot contains 8 regplot (one for each model)
# x absciss is the number of input graphs ('nb_input_graphs')
# the color of the regplot is the subpipeline_name
for i, metric in enumerate(metrics):
    axes[i].set_title(titles[i])
    axes[i].set_xlabel("Number of Input Graphs")
    axes[i].set_ylabel(metric)

    # Loop through each subpipeline and plot a regplot on the subplot
    for subpipeline in unique_subpipelines:
        subset = class1_metrics[class1_metrics["subpipeline_name"] == subpipeline]
        sns.regplot(x="nb_input_graphs", y=metric, data=subset, ax=axes[i], color=palette_dict[subpipeline], label=subpipeline)

    axes[i].legend()

# Adjust layout and save the plots
plt.tight_layout()
plt.savefig(f"{PLOT_OUTPUT_DIR_PATH}/nb_input_to_model_metrics_plot_v2_no_zeros.png")