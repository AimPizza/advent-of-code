import re

# put first element in one list
# second element in another list
# sort both lists
# add on each iteration onto whole sum

# read all numbers into two separate lists

first_numbers = []
second_numbers = []

with open("input.txt", "r") as input_numbers:
    for line in input_numbers:
        both_numbers = re.findall('\d+', line)
        first_numbers.append(int(both_numbers[0]))
        second_numbers.append(int(both_numbers[1]))


# sort lists and add them up into one big sum

final_sum = 0

first_numbers.sort()
second_numbers.sort()

for i in range(0, len(first_numbers)):
    final_sum += abs(first_numbers[i] - second_numbers[i])

print(final_sum)