import pandas as pd


INPUT_RESULT_CSV_PATH = "/home/onyr/code/phdtrack/predicting_ssh_key_masterarbeit_report/src/results/csv/concatenated_csv/concatenated_raw_result_v2.csv"
OUTPUT_FILE_PATH = "/home/onyr/code/phdtrack/predicting_ssh_key_masterarbeit_report/src/results/embedding_and_training_duration_from_concat_res_v2.csv"

# Load your concatenated csv file
df = pd.read_csv(INPUT_RESULT_CSV_PATH)

# print the number of rows and columns
print("Number of rows:", df.shape[0])
print("Number of columns:", df.shape[1])

# count the average duration_embedding (in seconds) for each model
# EX: duration_embedding =  94.191921 total sec (00h 01m 34s)
# first, remove the " sec (00h 01m 34s)" part, and convert the string to float
df["duration_embedding"] = df['duration_embedding'].str.extract(r'(\d+\.\d+)').astype(float)
df['duration_train_test'] = df['duration_train_test'].str.extract(r'(\d+\.\d+)').astype(float)

# Compute totals and ratio
total_embedding_time = df['duration_embedding'].sum()
total_training_time = df['duration_train_test'].sum()
ratio = total_embedding_time / total_training_time if total_training_time != 0 else float('inf')

# save results to .txt file
with open(OUTPUT_FILE_PATH, 'w') as f:
    f.write(f'Total embedding time: {total_embedding_time} seconds\n')
    f.write(f'Total training time: {total_training_time} seconds\n')
    f.write(f'Ratio: {ratio}\n')

# also print results to console
def format_time(seconds):
    days = seconds // (24 * 3600)
    seconds %= (24 * 3600)
    hours = seconds // 3600
    seconds %= 3600
    minutes = seconds // 60
    seconds %= 60
    return f'{int(days)} days, {int(hours)} hours, {int(minutes)} minutes, {seconds} seconds'

print(f'Total embedding time: {format_time(total_embedding_time)}')
print(f'Total training time: {format_time(total_training_time)}')

print(f'Ratio: {ratio}')