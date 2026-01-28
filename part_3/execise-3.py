# TITLE: More loops
# (1)Multiplication

num = int(input("Please enter a positive integer: "))

for i in range(1, num + 1):
    for j in range(1, num + 1):
        print(f"{i} x {j} = {i * j}")

# (2) Factorial

while True:
    number = int(input("Please type in an integer number: "))

    if number <= 0:
        break

    factorial = 1
    for i in range(1, number + 1):
        factorial *= i
    print(f"The factorial of the number {number} is {factorial}")

