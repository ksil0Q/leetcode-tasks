def maximalSquare(matrix: list[list[str]]) -> int:
    if not matrix:
        return 0
    m = len(matrix)
    n = len(matrix[0])
    rec = [0] * n
    maximum = 0
    prev = 0
    for i in range(m):
        for j in range(n):
            temp = rec[j]
            if matrix[i][j] == "1":
                if j > 0:
                    rec[j] = min(rec[j - 1], rec[j], prev) + 1
                else:
                    rec[j] = 1
            else:
                rec[j] = 0
            prev = temp
            maximum = max(maximum, rec[j])

    print(maximum ** 2)
    return maximum * maximum
#сука динпрог, хз че происходит в (if j > 0:)

if __name__ == '__main__':
    maximalSquare([['0', '1', '1', '1'],
                   ['1', '1', '0', '1'],
                   ['1', '0', '1', '0'],
                   ['1', '1', '1', '1']])