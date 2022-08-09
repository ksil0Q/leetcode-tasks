def matrixReshape(mat: list[list[int]], r: int, c: int) -> list[
    list[int]]:
    m = len(mat)
    n = len(mat[0])

    if m == r and n == c:
        return mat

    if not (m * n) == (r * c):
        return mat

    new_matrix = []
    list_ = []

    for i in range(0, m):
        for j in range(0, n):
            list_.append(mat[i][j])

    for i in range(0, r):
        temp = []
        for j in range(0, c):
            element = list_.pop(0)
            temp.append(element)
        new_matrix.append(temp)

    return new_matrix


if __name__ == '__main__':
    matrixReshape([[1,2],[3,4]], 1, 4)