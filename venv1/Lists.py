lucky_nums = [4, 8, 15, 16, 23, 42]
friends = ["Siddharth", "Jemin", "Kishan", "Piyush", "Dilraj"]
print(friends[0])
print(friends[1:])

'Extends() function: appends one list at the end of another list'
friends.extend(lucky_nums)
print(friends)
print(lucky_nums)

'Append() function: appends a single element at the end of a list'
friends.append("Appu")
print(friends)

'Insert() function: Has two parameters {index, value}. as an element is passed into the list, ' \
'the rest of the elements are shifted to the right by one to make space.'
friends.insert(2, "Mari_vaahli")
print(friends)

# Remove() function: Helps remove the element from the list.
friends.remove(8)
print(friends)

# Clear() function: removes everything from the list
lucky_nums.clear()
print(lucky_nums)

# 'Index() function: returns the index of a value within the list'
print(friends.index("Siddharth"))

# 'Count() function: How many times a value shows up inside a list'
print(friends.count("Jemin"))

# 'Reverse() function: reverse the order of the list'
lucky_nums.reverse()
print(lucky_nums)

# 'Sort() function: Sorts the list out in ascending order'
lucky_nums.sort()
print(lucky_nums)

# 'Copy() function: copies a list to another list'
friends2 = friends.copy()
print(friends2)
