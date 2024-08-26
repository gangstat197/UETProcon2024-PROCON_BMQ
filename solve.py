def compare(a, b):
    difference_count = 0

    # Compare the matrices element-wise and count differences
    for i in range(a.m):
        for j in range(a.n):
            if a.matrix[i][j] != b.matrix[i][j]:
                difference_count += 1

    return difference_count
