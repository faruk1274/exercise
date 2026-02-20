def double_items_from_file(filename: str):
    numbers = []

    with open(filename) as file:
        for line in file:
            number = int(line.strip())
            numbers.append(number * 2)

    return numbers


if __name__ == "__main__":
    doubled_numbers = double_items_from_file("numbers.txt")
    print(doubled_numbers)