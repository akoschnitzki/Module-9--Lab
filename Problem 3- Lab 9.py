# Name - Alexander Koschnitzki
# Date - 11-30-21
# CSS - 225

# Problem 3

# In this problem, it is able to show a loop that can ask the user
# to input numbers until it adds to one hundred or until it is greater than
# it. Then it prints all the numbers that you input.

sum = 0
list = []

while sum <= 100:
    number = int(input("Enter your Number"))
    list.append(number)
    sum = sum + number
print(list)
