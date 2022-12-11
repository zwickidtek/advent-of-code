with open('day1/input') as file:
    lines = file.readlines()

current_sum = 0
sum_array = []
for line in lines:
    if len(line) < 2:
        sum_array.append(current_sum)
        current_sum = 0
        continue
    else:
        cleaned_str=line.replace(' ', '')
        cleaned_str=cleaned_str.replace('\n', '')
        current_sum+=int(cleaned_str)


sum_array.sort()
print(sum(sum_array[-3:]))