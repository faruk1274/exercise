import math

def hypotenuse(leg1: float, leg2: float):
    return math.sqrt(leg1**2 + leg2**2)

if __name__ == "__main__":
    result = hypotenuse(3.0, 4.0)
    print("The length of the hypotenuse is:", result)