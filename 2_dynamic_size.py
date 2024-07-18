# Dynamic means our lists can grow and shrink by adding and removing items

bec_class = ['David', 'James', 'Adam', 'Tyler']
print(bec_class)

# ADDING TO LISTS

#--- list.append(item) : list method that adds an item to the END of a list

bec_class.append('Vincent')
print(bec_class)

bec_class.append(str(2))
print(bec_class)

bec_class.append('2')
print(bec_class)

some_stuff = [12, True, 'blue', 1345.6789]
bec_class.append(some_stuff)
print(bec_class)

# REMOVING ITEMS FROM LISTS

#--- list.remove(item) : list method that allows us to remove an item by name

bec_class.remove(some_stuff)
print(bec_class)

bec_class.remove('2')
print(bec_class)

bec_class.remove('2')
print(bec_class)

bec_class.remove('James')
print(bec_class)


# bec_class.append('2', '2', '2') # this will not work