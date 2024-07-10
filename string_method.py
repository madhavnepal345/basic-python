#write all string method

a="   hello Bro! How are you??   "
print(a.capitalize())#Capitalizes the first character of a string and makes all other characters lowercase.
print(a.lower())#Converts all uppercase characters in a string into lowercase characters. 
print(a.upper())#Converts all lowercase characters in a string into uppercase characters.
print(len(a))#Returns the number of characters in a string.
print(a.find("Bro"))#Finds the position where substring is found, if not present returns -1.
print(a[6])#Accessing an element by index. Index starts from 0 for the first character.
b=a+ "I am fine"
print(b)
c=a.replace("You","Me")
print(c)
d=a.split()
print(d)#Splits a string into a list where each word is a separate item in the list.
e=a.strip()#Removes leading and trailing whitespaces.
f=a.lstrip()#Removes only leading whitespaces.
g=a.rstrip()#Removes only trailing whitespaces.
print(e)
print(f)
print(g)
# print(a.count())#Returns the number of times a specified value occurs in a string
print(a.title())#Converts the first character of each word to UpperCase letter and make others LowerCase.
print(a.zfill(5))