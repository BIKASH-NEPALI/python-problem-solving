# REVERSE A STRING USING A LOOP.
string=input("enter a string value:\n")
reverse=""
for ch in string:
    reverse=ch+reverse
print(reverse)