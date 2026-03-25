# Create dictionary from two lists......

num1 = list(input("Enter 1st list values separated by space: ").split())    #name age branch
num2 = list(input("Enter 2nd list values separated by space: ").split())    #shreya 20 Datascience

print('Your 1st list is', num1)         #Your 1st list is ['name', 'age', 'branch']
print('Your 2nd list is', num2)         #Your 2nd list is ['shreya', '20', 'Datascience']

dictionary = dict(zip(num1, num2))      #{'name': 'shreya', 'age': '20', 'branch': 'Datascience'}
print(dictionary)