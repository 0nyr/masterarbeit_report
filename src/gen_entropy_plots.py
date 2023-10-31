import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Define the path to the CSV file
CHUNK_ENTROPIES_CSV_FILE_PATH = "/home/onyr/code/phdtrack/predicting_ssh_key_masterarbeit_report/src/results/chunk_entropies/chunk_entropies.csv"
SAVE_PLOT_DIR_PATH = "/home/onyr/code/phdtrack/predicting_ssh_key_masterarbeit_report/src/results/plots"

# Load the CSV file using Pandas
df = pd.read_csv(CHUNK_ENTROPIES_CSV_FILE_PATH)

# Plotting using sns.stripplot
plt.figure(figsize=(14, 10))
sns.stripplot(x="chunk_is_key", y="chunk_entropy", data=df, jitter=0.45, alpha=0.5)

plt.title("Chunk Entropy by Key Status, for all chunks in the cleaned dataset.")
plt.xlabel("Is Key")
plt.ylabel("Entropy Value")

# save the plot
plt.savefig(f"{SAVE_PLOT_DIR_PATH}/chunk_entropy_by_key_status.png")