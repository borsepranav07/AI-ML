# ==========================================================
# main.py
# Importing functions from math_utils.py
# ==========================================================

# Method 1 : Import the entire module
import math_utils

print("Using import math_utils")
print("Addition =", math_utils.add(10, 5))
print("Subtraction =", math_utils.subtract(10, 5))
print("Square =", math_utils.square(6))


print("\n-------------------------\n")


# Method 2 : Import only one function
from math_utils import square

print("Using from math_utils import square")
print("Square =", square(8))