#!/usr/bin/python3
"""Writing a function for Pascal's Triangle"""


def pascal_triangle(n):
    # Edge case: Return an empty list for n <= 0
    if n <= 0:
        return []

    # Initialize the Pascal's triangle with the first row
    triangle = [[1]]

    # Build Pascal's triangle row by row
    for i in range(1, n):
        # Calculate the current row based on the previous row
        prev_row = triangle[-1]  # Get the previous row
        current_row = [1]  # Initialize the current row with the leftmost 1
        for j in range(1, i):
            # Calculate the elements between the leftmost and rightmost 1's
            current_row.append(prev_row[j - 1] + prev_row[j])
        current_row.append(1)  # Add the rightmost 1
        triangle.append(current_row)  # Add the current row to the triangle

    return triangle
