def fibonacci(n):
    # Base case: Fibonacci of 0 is 0, Fibonacci of 1 is 1
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    # Recursive case: Fibonacci of n is the sum of the previous two Fibonacci numbers
    else:
        return fibonacci(n-1) + fibonacci(n-2)

# Taking user input for the Fibonacci number
n = int(input("Enter a number to find the Fibonacci value: "))

# Calling the fibonacci function and printing the result
result = fibonacci(n)
print(f"Fibonacci of {n} is: {result}")
