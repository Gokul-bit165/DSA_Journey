def print_divisors(n):
    print(f"Divisors of {n} are:")
    for i in range(1, n + 1):
        if n % i == 0:
            print(i)

num = int(input("Enter a number to find its divisors: "))
print_divisors(num)