# Using recursive functions, write a program in C++/Java/python to print the first 10 Fibonacci Series

def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)
    
    
range_of_series = 10

for i in range(range_of_series):
    print(fibonacci(i), end=" ")    
    
    
    