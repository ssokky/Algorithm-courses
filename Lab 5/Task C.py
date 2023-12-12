def print_multiplication_table(n, m):
    for i in range(n * m):
        print(f"{(i // m) * (i % m):3}", end=" ")
        if (i + 1) % m == 0:
            print()

n, m = map(int, input().split())

print_multiplication_table(n, m)
