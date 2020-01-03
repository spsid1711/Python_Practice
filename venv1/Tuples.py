# Tuples are non-changing lists. Tuples are formed with perentheses while list are formed using [].
coordinates = (4,5,6,7)
# coordinates[1] = 10

coords = [(4,5), (5,6), (6,7), (7,8)]
print(coords[1])
coords[1] = (10,11)
print(coords[1])