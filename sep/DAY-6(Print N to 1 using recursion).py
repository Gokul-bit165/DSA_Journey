def print_n_to_1(n):
    if n > 0:
        print(n)
        print_n_to_1(n - 1)

num = int(input("Enter a number: "))
print_n_to_1(num)
