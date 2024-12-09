import pandas as pd
import sys

# Check if input and output files are provided
if len(sys.argv) < 3:
    sys.exit("Error: Please include an input and output file. Example: python script.py input.csv output.csv")

input_file = sys.argv[1]
output_file = sys.argv[2]

# Load the data into a pandas DataFrame
# Assuming the file contains raw data in a single column named "data"
try:
    df = pd.read_csv(input_file, header=None, names=["data"])
except Exception as e:
    sys.exit(f"Error reading the file: {e}")

# Split rows by newline
df["data"] = df["data"].astype(str)  # Ensure data is string
df = df["data"].str.split("\n", expand=True).stack().reset_index(drop=True).to_frame(name="data")

# Split data into columns by commas
df = df["data"].str.split(",", expand=True)

# Drop specific rows
rows_to_drop = [0, 12]  # Drop row 1 (index 0) and row 13 (index 12)
df = df.drop(rows_to_drop, axis=0).reset_index(drop=True)

# Drop additional rows where a specific column (e.g., split4) contains "Total"
# Assuming column 4 (zero-based index 3) corresponds to "split4"
if len(df.columns) > 3:  # Ensure column exists before filtering
    df = df[df[3] != "Total"]

# Save the cleaned data to a new CSV file
try:
    df.to_csv(output_file, index=False, header=False)
    print(f"Cleaned data successfully saved to {output_file}")
except Exception as e:
    sys.exit(f"Error saving the file: {e}")
