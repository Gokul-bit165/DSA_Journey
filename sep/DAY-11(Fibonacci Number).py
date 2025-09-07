def fibonacci_iterative(n):
    sequence = []
    a, b = 0, 1
    for _ in range(n):
        sequence.append(a)
        a, b = b, a + b
    return sequence

num = int(input("Enter the number of Fibonacci numbers to generate: "))
print(fibonacci_iterative(num))
