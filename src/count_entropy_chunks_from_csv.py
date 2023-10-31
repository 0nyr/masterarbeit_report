import pandas as pd

# Define the path to the CSV file
CHUNK_ENTROPIES_CSV_FILE_PATH = "/home/onyr/code/phdtrack/predicting_ssh_key_masterarbeit_report/src/results/chunk_entropies/chunk_entropies.csv"

# Load the CSV file using Pandas
df = pd.read_csv(CHUNK_ENTROPIES_CSV_FILE_PATH)

# Calculate the minimum entropy of the chunks that are keys
min_entropy_of_key_chunks = df[df['chunk_is_key'] == True]['chunk_entropy'].min()

# Count the number of chunks whose entropy is less than this minimum
count_of_lower_entropy_chunks = len(df[df['chunk_entropy'] < min_entropy_of_key_chunks])

# Calculate the total number of chunks
total_chunks = len(df)

print(f"The number of chunks whose entropy is less than the minimum entropy of the chunks that are keys is: {count_of_lower_entropy_chunks}")
print(f"The total number of chunks is: {total_chunks}")

# print the percentage of reduction (number of chunks whose entropy is less than the minimum entropy of the chunks that are keys) / (total number of chunks)
print(f"The percentage of reduction is: {count_of_lower_entropy_chunks / total_chunks * 100}%")