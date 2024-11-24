def fibonacci_series(n):
    a, b = 0, 1
    fibo = []
    for i in range(n):
        fibo.append(a)
        a, b = b, a + b
    return fibo

n = int(input("Enter the number of terms for the Fibonacci series: "))

if n <= 0:
    print("Please enter a positive integer.")
else:
    print("Fibonacci_series up to", n, "terms:", fibonacci_series(n))
