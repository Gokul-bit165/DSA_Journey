def reverse_array(arr):
    if len(arr) == 0:
        return []
    return [arr[-1]] + reverse_array(arr[:-1])

array = list(map(int, input("Enter array elements separated by space: ").split()))
reversed_array = reverse_array(array)
print("Reversed array:", reversed_array)
