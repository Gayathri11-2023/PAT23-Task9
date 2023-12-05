'''
# Function to generate Fibonacci series
def fibonacci(n):
    fib_series = [0, 1]
    for i in range(2, n):
        fib_series.append(fib_series[-2] + fib_series[-1])
    return fib_series

# Generate Fibonacci series with 50 elements
fib_series = fibonacci(50)
print(fib_series)
'''
# Generate fibonacci series using lambda function
fibonacci = lambda n, a=0, b=1: [a] + (fibonacci(n-1, b, a+b) if n > 1 else [])

# Generate Fibonacci series with 50 elements
fib_series = fibonacci(50)

print(fib_series)

                           