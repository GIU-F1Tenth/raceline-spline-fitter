import csv
import os
from argparse import ArgumentParser

import matplotlib.pyplot as plt
import numpy as np

from utils import catmull_rom_segment, save_path


def create_closed_catmull_rom_spline(points, num_points=1000):
    """
    Create a closed Catmull-Rom spline from a set of points.

    Parameters:
        points: List of control points, each point is a list or array of [x, y].
        num_points: Number of points to generate along the spline.

    Returns:
       (x_fine, y_fine): Arrays of x and y coordinates of the spline.
    """
    points = np.array(points)
    n = len(points)

    # For closed spline, extend points by wrapping around
    extended_points = np.vstack([points[-1:], points, points[:2]])

    num_segments = n
    points_per_segment = num_points // num_segments

    x_fine = []
    y_fine = []

    for i in range(num_segments):
        p0 = extended_points[i]
        p1 = extended_points[i + 1]
        p2 = extended_points[i + 2]
        p3 = extended_points[i + 3]

        # Generate points for this segment
        # Exclude last point to avoid duplication
        t_values = np.linspace(0, 1, points_per_segment + 1)[:-1]

        for t in t_values:
            point = catmull_rom_segment(p0, p1, p2, p3, t)
            x_fine.append(point[0])
            y_fine.append(point[1])

    x_fine.append(x_fine[0])
    y_fine.append(y_fine[0])

    return np.array(x_fine), np.array(y_fine)


if __name__ == "__main__":
    arg_parser = ArgumentParser(
        description="Create a closed Catmull-Rom spline from control points.")

    arg_parser.add_argument(
        '--num_points', type=int, default=1000,
        help='Number of points to generate along the spline.')
    arg_parser.add_argument(
        '--input_csv', type=str, required=True,
        help='Path to the input CSV file containing control points. Format: x,y per line.'
    )
    arg_parser.add_argument(
        '--output_csv', type=str, default=os.path.join("out", "spline_points.csv"),
        help='Path to save the generated spline points as a CSV file.'
    )

    args = arg_parser.parse_args()
    input_points = []

    # Check if the input CSV file exists
    if not os.path.exists(args.input_csv):
        print(f"Input CSV file '{args.input_csv}' does not exist.")
        exit(1)

    with open(args.input_csv, 'r') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            if len(row) == 2:
                try:
                    x, y = float(row[0]), float(row[1])
                    input_points.append([x, y])
                except ValueError:
                    print(f"Invalid point: {row}. Skipping.")

    if len(input_points) < 4:
        print("At least 4 control points are required to create a spline.")
        exit(1)

    # Create the closed Catmull-Rom spline
    x_fine, y_fine = create_closed_catmull_rom_spline(
        input_points, args.num_points)

    save_path(args.output_csv, x_fine, y_fine)

    # Plotting the spline and control points
    input_points = np.array(input_points)
    plt.figure(figsize=(8, 6))
    plt.plot(x_fine, y_fine, 'b-', label='Catmull-Rom Spline')
    plt.plot(input_points[:, 0], input_points[:, 1],
             'ro-', label='Control Points')
    plt.axis('equal')
    plt.legend()
    plt.title('Closed Catmull-Rom Spline Path')
    plt.grid(True)
    plt.show()


# Example usage:
# if __name__ == "__main__":
#     input_points = [
#         [0, 0],
#         [2, 1],
#         [4, 0],
#         [6, 2],
#         [8, 1],
#         [10, 3],
#         [9, 5],
#         [7, 6],
#         [5, 7],
#         [3, 6],
#         [1, 8],
#         [-1, 7],
#         [-3, 6],
#         [-4, 4],
#         [-5, 2],
#         [-4, 0],
#         [-3, -2],
#         [-1, -3],
#         [1, -2],
#         [2, -1]
#     ]

#     x_fine, y_fine = create_closed_catmull_rom_spline(input_points)

#     input_points = np.array(input_points)
#     plt.figure(figsize=(8, 6))
#     plt.plot(x_fine, y_fine, 'b-', label='Catmull-Rom Spline')
#     plt.plot(input_points[:, 0], input_points[:, 1],
#              'ro-', label='Control Points')
#     plt.axis('equal')
#     plt.legend()
#     plt.title('Closed Catmull-Rom Spline Path')
#     plt.grid(True)
#     plt.show()
