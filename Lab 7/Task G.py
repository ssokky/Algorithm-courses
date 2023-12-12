def count_substring_occurrences(main_string, substring):
    count = 0
    start = 0

    while start < len(main_string):
        index = main_string.find(substring, start)
        if index != -1:
            count += 1
            start = index + 1
        else:
            break

    return count

main_string = input().strip()
substring = input().strip()

result = count_substring_occurrences(main_string, substring)
print(result)
