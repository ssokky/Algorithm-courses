path = input()

path_parts = path.split("\\")

for part in path_parts[:-1]:  
    print(part)
