# Name - Alexander Koschnitzki
# Date - 11-30-21
# CSS - 225

# Problem 2

# In this problem, it is able to count each number until it hits eleven and it
# is able to add them to a list. Once it adds it to a list and it hits 10, it prints
# the list to see them all.

numbers = []
count = 0
while count <= 10:
    numbers.append(count)
    count +=1

print(numbers)