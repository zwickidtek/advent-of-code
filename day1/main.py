with open('./day1/input') as file:
    lines = file.readlines()

max = 0
current_sum = 0
for line in lines:
    if len(line) < 2:
        if current_sum > max:
            max = current_sum
        current_sum = 0
        continue
    else:
        cleaned_str=line.replace(' ', '')
        cleaned_str=cleaned_str.replace('\n', '')
        current_sum+=int(cleaned_str)

print(max)