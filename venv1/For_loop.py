# We can loop through a list or an array.
friends = ["Siddharth", "Aparna", "Jemin", "Dilraj"]
for i in friends:
    print(i)
print("---x---x---x---x---")
# We can also loop through a series of numbers.
for index in range(10):
    print(index) # This will loop through a series of numbers from 0-9 not including 10.
print("---x---x---x---x---")
# You can also specify a range of numbers such as range from 3-10.
for index in range(3, 10):
    print(index) # This will print out numbers from 3-10, not including 10.
print("---x---x---x---x---x---")
# Lets try and pass in the length of an array as the range within the for-loop.
for length in range(len(friends)):

    print(length)