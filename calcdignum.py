alpha,string=0,"Geeks1234"
for i in string:
	if (i.isalpha()):
		alpha+=1
print("Number of Digit is", len(string)-alpha)
print("Number of Alphabets is", alpha)
