import csv
import os


def catmull_rom_segment(p0, p1, p2, p3, t):
    """
    Calculate a point on a Catmull-Rom spline segment.
    p0, p1, p2, p3 are control points, t is parameter [0,1]

    Parameters:
        p0: Control point before the segment start as an array or list of [x, y].
        p1: Control point at the segment start as an array or list of [x, y].
        p2: Control point at the segment end as an array or list of [x, y].
        p3: Control point after the segment end as an array or list of [x, y].
        t: Parameter value in the range [0, 1].

    Returns:
        A point on the spline as an array [x, y].
    """
    t2 = t * t
    t3 = t2 * t

    return 0.5 * ((2 * p1) +
                  (-p0 + p2) * t +
                  (2*p0 - 5*p1 + 4*p2 - p3) * t2 +
                  (-p0 + 3*p1 - 3*p2 + p3) * t3)


def save_path(output_csv, x_fine, y_fine, boundary_left, boundary_right):
    """
    Save the generated spline points to a CSV file.

    Parameters:
        output_csv: Path to the output CSV file.
        x_fine: Array of x coordinates of the spline.
        y_fine: Array of y coordinates of the spline.
        boundary_left: Array of left boundary values.
        boundary_right: Array of right boundary values.
    """
    os.makedirs(os.path.dirname(output_csv), exist_ok=True)
    with open(output_csv, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['x', 'y', 'boundary_left', 'boundary_right'])
        for x, y, bl, br in zip(x_fine, y_fine, boundary_left, boundary_right):
            writer.writerow([x, y, bl, br])
