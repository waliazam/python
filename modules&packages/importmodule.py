
''''
You can then import mymodule in another Python script and use its myfunction:

'''


import mymodule   
# Import the calculator module
import calculator

mymodule.myfunction()

# Perform some calculations
result_add = calculator.add(10, 5)
result_subtract = calculator.subtract(10, 5)
result_multiply = calculator.multiply(10, 5)
result_divide = calculator.divide(10, 5)

# Print the results
print(f"Addition: {result_add}")
print(f"Subtraction: {result_subtract}")
print(f"Multiplication: {result_multiply}")
print(f"Division: {result_divide}")
