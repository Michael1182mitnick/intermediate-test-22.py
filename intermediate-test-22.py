# Implement run-length encoding for a given binary image matrix.

def run_length_encoding(matrix):
    """
    Perform run-length encoding on a binary image matrix.

    :param matrix: List of lists representing a binary image (2D matrix of 0s and 1s).
    :return: List of tuples representing the run-length encoding of the matrix.
    """
    if not matrix or not matrix[0]:
        return []

    rows = len(matrix)
    cols = len(matrix[0])
    encoded = []

    for row in range(rows):
        current_val = matrix[row][0]
        count = 1

        for col in range(1, cols):
            if matrix[row][col] == current_val:
                count += 1
            else:
                encoded.append((current_val, count))
                current_val = matrix[row][col]
                count = 1

        # Append the last run in the row
        encoded.append((current_val, count))

    return encoded


# Example usage
binary_matrix = [
    [1, 1, 0, 0, 0],
    [1, 0, 0, 1, 1],
    [0, 0, 1, 1, 1]
]

encoded_result = run_length_encoding(binary_matrix)
print("Run-length encoding of the binary matrix:")
print(encoded_result)
