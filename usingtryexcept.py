# given string
string = "geeks2for3geeks"

# initialized value
total_digits = 0
total_letters = 0

# iterate through all characters
for s in string:

	# try to convert the character to int
	# if it's not possible, increment the letter count
	try:
		int(s)
		total_digits += 1
	except:
		total_letters += 1

print("Total letters found :-", total_letters)
print("Total digits found :-", total_digits)
