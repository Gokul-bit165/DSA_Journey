def sum_of_first_n(n):
    if n == 0:
        return 0
    return n + sum_of_first_n(n - 1)

num = int(input("Enter a number: "))
result = sum_of_first_n(num)
print(f"The sum of the first {num} natural numbers is: {result}")
