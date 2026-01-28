# Objects and methods
def smallest_average(person1: dict, person2: dict, person3: dict):
    def average(person):
        return (person["result1"] + person["result2"] + person["result3"]) / 3

    avg1 = average(person1)
    avg2 = average(person2)
    avg3 = average(person3)

    if avg1 <= avg2 and avg1 <= avg3:
        return person1
    elif avg2 <= avg1 and avg2 <= avg3:
        return person2
    else:
        return person3



p1 = {"name": "Aisha", "result1": 5, "result2": 6, "result3": 7}
p2 = {"name": "Musa", "result1": 3, "result2": 4, "result3": 5}
p3 = {"name": "Zainab", "result1": 6, "result2": 6, "result3": 6}

# person1 = {"name": "Mary", "result1": 2, "result2": 3, "result3": 3}
# person2 = {"name": "Gary", "result1": 5, "result2": 1, "result3": 8}
# person3 = {"name": "Larry", "result1": 3, "result2": 1, "result3": 1}

# print(smallest_average(person1, person2, person3))

result = smallest_average(p1, p2, p3)
print(result["name"])  

# example 2

def row_sums(my_matrix: list):
    for row in my_matrix:
        row.append(sum(row))

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

row_sums(matrix)
print(matrix)
