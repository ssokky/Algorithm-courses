input_str = input()

digit_count = 0

for char in input_str:

    if char.isdigit():
        digit_count += 1

print(digit_count)
