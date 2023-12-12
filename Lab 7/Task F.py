def replace_substring(main_string, pattern, replacement):
   
    result_string = main_string.replace(pattern, replacement)
    return result_string

main_string = input()
pattern = input()
replacement = input()

result_string = replace_substring(main_string, pattern, replacement)
print(result_string)
