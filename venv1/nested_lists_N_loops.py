# You can create a multi-dimensional array in Python and access is using the idea of rows and columns.
number_grid = [
    [1,2,3],
    [4,5,6],
    [7,8,9],
    [0]
]

print(number_grid[0][0])
print("---x---x---x---")

# You can also use nested loops to print all the elements from the list
for row in number_grid:
    for col in row:
        print(col)