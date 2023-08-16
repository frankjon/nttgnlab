import re
# given string
string = "geeks2for3geeks"

# initialized value
total_digits = len(re.findall('[0-9]',string))
total_letters = len(re.findall('[A-z]', string))

# iterate through all characters
print("Total letters found :-", total_letters)
print("Total digits found :-", total_digits)
