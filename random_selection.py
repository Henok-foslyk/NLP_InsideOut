import sys
import pandas as pd
import random

def process_csv(input_file):
    # Load the CSV file
    try:
        data = pd.read_csv(input_file)
    except Exception as e:
        print(f"Error reading file: {e}")
        sys.exit(1)

    # Ensure the file has at least two columns
    if data.shape[1] < 2:
        print("The input file must have at least two columns.")
        sys.exit(1)

    # Randomly select 30 rows
    sampled_data = data.sample(n=min(30, len(data)), random_state=random.randint(0, 10000))

    # Keep only the first two columns
    sampled_data = sampled_data.iloc[:, :2]

    # Save the resulting data to a new file
    output_file = "random_rows.csv"
    sampled_data.to_csv(output_file, index=False)

    print(f"Processed file saved as: {output_file}")

if __name__ == "__main__":
    # Ensure the script is run with the correct arguments
    if len(sys.argv) != 2:
        print("Usage: python script.py file.csv")
        sys.exit(1)

    input_file = sys.argv[1]
    process_csv(input_file)