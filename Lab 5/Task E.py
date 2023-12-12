def rotate_array(matrix):
    rotated_matrix = list(zip(*matrix[::-1]))
    return rotated_matrix

N, M = map(int, input().split())

array = [list(map(int, input().split())) for _ in range(N)]

rotated_array = rotate_array(array)
for row in rotated_array:
    print(" ".join(map(str, row)))
