# Lecture Notes: Python Lists

### Materials for reference:
- [Dylan's Lecture Notes](https://docs.google.com/document/d/1PwZ6Zdf4iHPYCmGeHMQlBo1EVnMXkitE4VamNf8wRl4/edit)

## Intro to Lists
- **What are they**?
    - Lists are a data type that can store multiple different items (strings, ints, lists, etc)
- Create an empty list, and a list with items in it

### Indexing 
- The key to accessing, modifying, and removing items from list. 
- Indexes are the positions of each item in a list, counting from 0
    - Example of indexing into a list:
        - Index into first item using `0`
        - Index into the LAST ITEM `-1`

```python
# Indexing into a list
fruits = ["apple", "banana", "cherry"]
print(fruits[0])  # Output: apple
print(fruits[2])  # Output: cherry
```

### Indexing Errors
- Indexing to a position that *does not exist* in your list will cause an `index out of bounds` error

### Flexibility:
- Lists can hold diverse items

```python
eclectic_list = [42, "unicorn", 3.14, ["apple", "banana", "cherry"]]
print(eclectic_list)
```


### Dynamic Size 
- We can add to lists using `.append(<item>)`
- We can remove from lists `.remove(<item>)` (removes the first instance of an item)
    - Show remove with duplicates
- Max size = `536,870,912`

### List Methods:
- `.append( item )`
- `.insert( index, item)`
- `.remove(item)`
- `.pop()` takes out last item (returns item removed)
    - `.pop(index)` removes item from specified index
- `.index(item)` tells you the position of an item in a list
- Modifying lists at particular indices 
    - `list[index] = new_item`
- `.count(item)` counts how many times an item occurs in a list
- `.reverse()` reverses your list
- `.sort()` sorts items alphabetically or by ascending value
- `len()` returns the length of a list (how many items are in it)
- `.clear()` removes everything from a list (in place)

### Membership Check:
- `in`: 
    - checks to see if an item is in a list

- `Not in`: 
    - checks to see if item not in a list

### ==Merging Lists==:
- `list_1 + list_2 = list_3`
    - definitely give this example, maybe use `all_students = class1 + class2` 
- `list_1.extends(list_2)`
    - maybe not so necessary, don't need to show

### ==Copying Lists==:
- `.copy()` returns a copy of a list
- `[:]` Full slice
- Why we can’t do `copy = my_list`

### Identity Operators:
- Check it two items are the exact same object
- `is`: 
    - checks to see two variables refer to the same place in memory
```python
# Example 1: Using `is`
list1 = [1, 2, 3]
list2 = list1
list3 = [1, 2, 3]

# Checking if list1 and list2 reference the same object
print(list1 is list2)  # Output: True

# Checking if list1 and list3 reference the same object
print(list1 is list3)  # Output: False

```

- `is not`: 
    - checks if to variable don’t refer to the same place in memory

```python
guest_list = ["Alice", "Bob", "Charlie"]
print("Alice" in guest_list)    # Outputs: True
print("Dana" in guest_list)    # Outputs: False
```

### Slicing:
- `[start:stop]`
- Defaults are `0` index to very end

### Joining Strings
- `" ".join( list )` returns all string in list joined into a single string with a `“ “` between the words

