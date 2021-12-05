# Name - Alexander Koschnitzki
# Date - 11-30-21
# CSS - 225

# Problem 4

# In this problem, it is able to show a loop that uses a counter to count from zero to
# fifty. Each time a number is divisible by ten, it is able to put that number in a list. Once
# the counter hits fifty, it then prints the list to display all the number in the list that
# were divisible by ten.

factors = []
num = 0

while num <= 50:
    if num % 10 == 0:
        factors.append(num)
    num += 1

print(factors)