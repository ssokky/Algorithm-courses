def generate_array(n, m):
    array = [[0] * m for _ in range(n)]

    for j in range(m):
        array[0][j] = 1
    for i in range(n):
        array[i][0] = 1

    for i in range(1, n):
        for j in range(1, m):
            array[i][j] = array[i-1][j] + array[i][j-1]

    return array

n, m = map(int, input().split())

result_array = generate_array(n, m)
for row in result_array:
    print(" ".join(map(str, row)))
