import os
import csv
from argparse import ArgumentParser


def convert_csv(csv_file, cleaned_csv_file):
    """
    Convert a CSV file to a cleaned format with only x and y coordinates.
    Parameters:
        csv_file: Path to the input CSV file.
        cleaned_csv_file: Path to save the cleaned CSV file.
    """

    csv_data = []

    with open(os.path.join("data", csv_file), 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            try:
                x = float(row[0])
                y = float(row[1])
                csv_data.append([x, y])
            except ValueError:
                continue  # Skip rows with non-numeric values

    with open(os.path.join("data", cleaned_csv_file), 'w') as file:
        writer = csv.writer(file)
        writer.writerow(['x', 'y'])  # Write header
        writer.writerows(csv_data)


if __name__ == "__main__":
    parser = ArgumentParser(description="Convert a CSV file.")
    parser.add_argument("csv_file", help="The input CSV file to convert.")
    parser.add_argument("cleaned_csv_file",
                        help="The output cleaned CSV file.")
    args = parser.parse_args()

    # Sanity checks
    if not os.path.exists(args.csv_file):
        raise FileNotFoundError(
            f"The file {args.csv_file} does not exist. Please ensure it is in the current directory.")

    if os.path.exists(args.cleaned_csv_file):
        print(
            f"Warning: The file {args.cleaned_csv_file} already exists and will be overwritten.")
        input("Press Enter to continue or Ctrl+C to cancel...")

    convert_csv(args.csv_file, args.cleaned_csv_file)
