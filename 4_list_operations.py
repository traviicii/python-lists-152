# Some other cool we can do with lists

# Memberships checks with 'in' to check if an item is IN a list, returns a boolean value

guest_list = ['Adam', "Bob", 'Charlie', 'James', "Dylan", 'Ethan']

print('Albert' in guest_list)
print('Dylan' in guest_list)

# name = input("What's your name? ")
# guest_list.append(name)

# # using if statements with the 'in' keyword
# if (name in guest_list):
#     print("Welcome to the party: ", name + '!!!')
# else:
#     print("Scraaaam fool!!!")

# # Secondary example of the above scenario with a second condition to check for
# if (name in guest_list):
#     print("Welcome to the party: ", name + '!!!')
# elif name not in guest_list:
#     print("Scraaaam fool!!!")


# Merging lists together with '+'

list1 = [1,2,3,4]
list2 = [5,6,7,8]
list3 = list1 + list2
print(list3)

list1 = [1,2,3,4]
list2 = ["this thing", 'that thing', 'another thing']
list3 = list1 + list2
print(list3)

# Copying a list with the .copy() method
# Changes made to a true copy do not affect the original list

fruit = ['apples', 'bananas', 'oranges']
copy_fruit = fruit.copy() # this creates a true copy that is not connected to the original list
print(copy_fruit)
copy_fruit.pop()
print("copy_fruit: ", copy_fruit)
print("fruit: ", fruit)

print('='*50)
print("THIS IS THE FULL SLICE")
# copying a list with a full slice --> list[:]
copy_fruit = fruit[:] # this is also a true copy
print(copy_fruit)
copy_fruit.pop()
print("copy_fruit: ", copy_fruit)
print("fruit: ", fruit)

print('='*50)

copy_fruit = fruit # not a true copy, would not recommend because it's still pointing to the same place in memory as the original fruit list. This is the same piece of data, but with two names now
print(copy_fruit)
copy_fruit.pop()
print("copy_fruit: ", copy_fruit)
print("fruit: ", fruit)

print('='*50)
# List slicing --> list[start:stop] : return a sublist from the start index to the stop index
# the default start and stop are the beginning and the end of the list (Full slice)
# the stop index is non-inclusive, meaning the item at the stop index will not be included in the slice

#indecies           0        1          2         3
key_lime_pie = ['slice1', 'slice2', 'slice3', 'slice4']
#neg indecies      -4       -3         -2        -1

my_slice = key_lime_pie[0:1]
print(my_slice)

big_slice = key_lime_pie[1:3]
print(big_slice)

last_slice = key_lime_pie[3:]
print(last_slice)

another_slice = key_lime_pie[2:-1]
print(another_slice)

another_slice2 = key_lime_pie[-1:]
print(another_slice2)

another_slice3 = key_lime_pie[-2:]
print(another_slice3)

another_slice4 = key_lime_pie[-1:-3:-1] # specifying a step parameter to tell python how to move onto the next item in the list. list[start:stop:step]
print(another_slice4)


# ' '.join(list) : Joins a list of strings together to form a single string

words = ['Hello', "I'm", 'getting', 'joined!']

sentence = ' '.join(words)
print(sentence)

new_sentence = '!!!!'.join(words)
print(new_sentence)