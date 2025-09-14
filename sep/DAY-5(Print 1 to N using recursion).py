def print_1_to_n(n):
    if n > 0:
        print_1_to_n(n - 1)
        print(n)


num = int(input("Enter a number: "))
print_1_to_n(num)
