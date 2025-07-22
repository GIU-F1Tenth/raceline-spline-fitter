# Raceline Spline Fitter

-   Creates closed Catmull-Rom splines from CSV input data
-   Configurable number of output points for smooth trajectory generation
-   Visualization support with matplotlib
-   Command-line interface for easy integration
-   CSV converter utility to adapt midline generator output for spline fitting Spline Fitter

A Python tool for creating smooth closed Catmull-Rom splines from control points, designed for generating racing lines and trajectory paths.

## Installation

### Prerequisites

-   Python 3.7 or higher

### Setting up a Virtual Environment

1. **Create a virtual environment:**

    ```bash
    python -m venv raceline-env
    ```

2. **Activate the virtual environment:**

    **On Windows (PowerShell/Command Prompt):**

    ```bash
    raceline-env\Scripts\activate
    ```

    **On macOS/Linux:**

    ```bash
    source raceline-env/bin/activate
    ```

3. **Install required packages:**
    ```bash
    pip install -r requirements.txt
    ```

## Usage

### CSV Converter (Data Adapter)

If you have output from a midline generator that needs to be cleaned and formatted for use with this spline fitter, use the CSV converter script first:

```bash
python csv_converter.py --csv_file input_file.csv --cleaned_csv_file cleaned_output.csv
```

### Parameters

-   `--csv_file` (required): Path to the input CSV file to be cleaned
-   `--cleaned_csv_file` (optional): The output path for the new cleaned csv
    (default: `out/cleaned.csv`)

This utility:

-   Extracts only x,y coordinates from the input CSV
-   Filters out any non-numeric data
-   Adds proper headers to the output file
-   Acts as an adapter between midline generator output and spline fitting input

**Note:** The converter expects input files to be in a `data/` directory and will save cleaned output there as well.

### Command Line Interface

Run the script with a CSV file containing control points:

```bash
python main.py --input_csv path/to/your/points.csv --num_points 1000
```

### Parameters

-   `--input_csv` (required): Path to the input CSV file containing control points
-   `--num_points` (optional): Number of points to generate along the spline
    (default: 1000)
-   `--output_csv` (optional): The output path for the new spline csv
    (default: `out/spline_output.csv`)

### CSV Input Format

The input CSV file should contain x,y coordinate pairs, one per line:

```csv
0,0
2,1
4,0
6,2
8,1
```

### Example Usage

```bash
# First, convert raw midline generator output to clean format
python csv_converter.py --csv_file raw_midline_data.csv --cleaned_csv_file cleaned_points.csv

# Then generate a spline with 1000 points from the cleaned control points
python main.py --input_csv data/cleaned_points.csv --num_points 1000

# Generate a spline with 500 points
python main.py --input_csv data/cleaned_points.csv --num_points 500
```

## Output

The script generates a smooth closed spline that passes through the vicinity of the provided control points, creating a continuous racing line suitable for autonomous vehicle path planning.

## Deactivating the Virtual Environment

When you're done working with the project, you can deactivate the virtual environment:

```bash
deactivate
```
