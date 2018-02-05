# https://stackoverflow.com/questions/42519/how-do-you-rotate-a-two-dimensional-array
def rotate(matrix):
    size = len(matrix)
    layer_count = int(size / 2)

    for layer in range(0, layer_count):
        first = layer
        last = size - first - 1

        for element in range(first, last):
            offset = element - first

            top = matrix[first][element]
            right_side = matrix[element][last]
            bottom = matrix[last][last-offset]
            left_side = matrix[last-offset][first]

            matrix[first][element] = left_side
            matrix[element][last] = top
            matrix[last][last-offset] = right_side
            matrix[last-offset][first] = bottom


arr = [[1, 2, 3], [4 , 5, 6], [7, 8, 9]]

rotate(arr)
print(arr)
