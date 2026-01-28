# TITILE: Loops with conditions
# (1) Print numbers

num = int(input('enter any num: '))
while num < 10:
    print(num)
    num+=1

# (2) Powers of two
upper_limit = int(input("Please type in an upper limit: "))

number = 1

while number <= upper_limit:
    print(number)
    number = number * 2

# (3) Powers of base n
upper_limit = int(input("Please type in an upper limit: "))
base = int(input("Please type in the base: "))

number = 1

while number <= upper_limit:
    print(number)
    number = number * base

# (4)The sum of consecutive numbers, version 1
limit = int(input("Please type in a limit: "))
total = 0
number = 1

while total < limit:
    total += number
    number += 1

print(total)

# (5)The sum of consecutive numbers, version 2
limit = int(input("Please type in a limit: "))

total = 0
number = 1
calculation = ""

while total < limit:
    total += number
    calculation += str(number)
    if total < limit:
        calculation += " + "
    number += 1

print(f"The calculation performed was: {calculation} = {total}")

