# In python, there already exists a function for exponential functions.
print(2**3)
# Lets try and create our own exponential function.
def raise_to_pow(base, power):
    result = 1
    for i in range(power):
        result *= base
    return result

print(raise_to_pow(2,3))