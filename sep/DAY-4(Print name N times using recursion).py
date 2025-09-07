def print_name_n_times(name, n):
    if n > 0:
        print(name)
        print_name_n_times(name, n - 1)

name = input("Enter your name: ")
num = int(input("Enter a number: "))
print_name_n_times(name, num)
