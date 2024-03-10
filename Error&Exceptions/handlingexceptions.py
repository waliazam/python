try:
    # Try to execute this block of code
    result = 10 / 0
except ZeroDivisionError:
    # Handle division by zero error
    print("You can't divide by zero!")
else:
    # Execute if no exceptions
    print("Division successful!")
finally:
    # Execute regardless of what happens
    print("Execution completed.")
