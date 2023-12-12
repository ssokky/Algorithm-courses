def generate_array(n, m):
    array = [[0] * m for _ in range(n)]

    num = 0
    for i in range(n + m - 1):
        for j in range(max(0, i - m + 1), min(i, n - 1) + 1):
            array[j][i - j] = num
            num += 1

    return array

n, m = map(int, input().split())

result_array = generate_array(n, m)
for row in result_array:
    print(" ".join(map(str, row)))
