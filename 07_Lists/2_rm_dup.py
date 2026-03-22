# Remove duplicates...

#solve this que with using for loop..
number = list(map(int, input('Enter the numbers of list with the spaces: ').split()))
print('Before removing the duplicate numbers:',number)

remove_dup = []

for num in number:
    if num not in remove_dup:
        remove_dup.append(num)

print('After removing the duplicate numbers:',remove_dup)


# also using set for solving this fastest but order lose..

#elem = [10, 20, 20, 30, 30, 40, 50, 50]
#remove_dups = list(set(elem))

#print(remove_dups)




#now here we also use List Comprehension (Advanced) 
#this method is compact but less readable

#elem = [10, 20, 20, 30, 30, 40, 50, 50]
#unique = []

#[unique.append(i) for i in elem if i not in unique]

#print(unique)



#we are also using dictionary because it is best morden approach

#elem = [10, 20, 20, 30, 30, 40, 50, 50]
#unique = list(dict.fromkeys(elem))

#print(unique)
