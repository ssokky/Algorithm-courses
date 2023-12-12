def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

# Вводим натуральное число
n = int(input())

# Проверяем, является ли число простым, и выводим результат
if is_prime(n):
    print("prime")
else:
    print("composite")
