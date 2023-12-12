def generate_sequences(N, K, sequence=[]):
    if len(sequence) == N:
        print(" ".join(map(str, sequence)))
        return
    for i in range(1, K + 1):
        generate_sequences(N, K, sequence + [i])

N, K = map(int, input().split())

generate_sequences(N, K)
