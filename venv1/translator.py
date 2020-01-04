# Note that this is not an actual translator. It is a hard-coded program meant to learn
# strings and nested loops.

# The first loop reads each character from the string of words. Using the string in the if-else statement,
# it checks if the letter exists within that string verifying if it is a vowel or not.
# If the argument is true then each vowel in the string will be replaced by g.
def translate(string):
    translation = ""  # type: str
    for letter in string:
        if letter in "AEIOUaeiou":
            translation = translation + "g"
        else:
            translation = translation + letter
    return translation

print(translate(raw_input("Enter a phrase: ")))