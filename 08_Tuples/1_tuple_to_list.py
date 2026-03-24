# Convert tuple to list...

tuple_data = tuple(map(int, input("Enter numbers separated by space: ").split()))
print('Before converting your tuple is', tuple_data)

list_data = list(tuple_data)
print('after converting your tuple into list is', list_data)