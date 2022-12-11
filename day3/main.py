with open('./day3/input') as file:
    rucksacks = file.readlines()
print(len(rucksacks))
appears_in_both = []
for i in rucksacks:
    a,b=i[:len(i)//2], i[len(i)//2:]

    for r in a:
        if r in b:
            appears_in_both.append(r)
            break
print(appears_in_both)
print(len(appears_in_both))
priority_sum =[]    #ord(character) - 96

for char in appears_in_both:
    if char.islower():
        priority_sum.append(ord(char)-96)
    else:
        priority_sum.append(ord(char)-38)


print(sum(priority_sum))