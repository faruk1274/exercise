from fractions import Fraction

def fractionate(amount: int):
    part = Fraction(1, amount)
    return [part for _ in range(amount)]

if __name__ == "__main__":
    result = fractionate(5)
    print(result)