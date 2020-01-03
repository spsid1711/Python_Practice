monthConversions = {
    "Jan": "January",
    "Feb": "February",
    "Mar": "March",
    "Apr": "April",
    "May": "May",
    "Jun": "June",
    "Jul": "July",
    "Aug": "August",
    "Sept": "September",
    "Oct": "October",
    "Nov": "November",
    "Dec": "December",
}

# Getting values based on the keys of the dictionary.
print(monthConversions["May"])

# Another way to get the values from the dictionary.
# Param: key.
print(monthConversions.get("Dec"))

# If the key-value pair that you are searching for using the get function
# is not in the dictionary, then you can pass in a DEFAULT value.
# Param: key, default_value
print(monthConversions.get("Luvv", "Invalid Key!"))

# The keys do not have to be a String. They can also be numbers or characters, based on the implementation.
