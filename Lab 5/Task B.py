def is_symmetric(matrix):
    n = len(matrix)
    for i in range(n):
        for j in range(i + 1, n):
            if matrix[i][j] != matrix[j][i]:
                return "no"
    return "yes"

n = int(input())

matrix = [list(map(int, input().split())) for _ in range(n)]

result = is_symmetric(matrix)
print(result)
