def print_n_times(n):
    if n > 0:
        print("Hello")
        print_n_times(n - 1)

num = int(input("Enter a number: "))
print_n_times(num)