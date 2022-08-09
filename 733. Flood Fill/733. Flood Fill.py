def floodFill(image: list[list[int]], sr: int, sc: int, newColor: int) -> list[list[int]]:
    image[sr][sc] = newColor


    return image

if __name__ == '__main__':
    floodFill([[0,0,0],[0,0,0]], 0, 0, 2)