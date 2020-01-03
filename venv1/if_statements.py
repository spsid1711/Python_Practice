#If-Else Statements with Boolean Variables

is_male = False  # type: bool
is_tall = False  # type: bool

# if is_male is True and is_tall is True:
#    print("You are a tall male")
# elif is_male is True and is_tall is False:
#    print("You are a short male")
# elif is_male is False and is_tall is True:
#    print("You are a tall female")
# else:
#    print("You are a short female")

if is_male and is_tall:
    print("You are a tall male")
elif is_male and not(is_tall):
    print("You are a short male")
elif not is_male and is_tall:
    print("You are a tall female")
else:
    print("You are a short female")

def max_num(num1, num2, num3):
    if num1 >= num2 and num1 >= num3:
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    else:
        return num3

print(max_num(3,1,2))
