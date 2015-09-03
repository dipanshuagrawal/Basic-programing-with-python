#Dictionary in Python
#Each key is separated from its value by a colon (:), the items are separated by commas.
#The whole thing is enclosed in curly braces. An empty dictionary without any items is written with just two curly braces.
#Keys are unique within a dictionary while values may not be. The values of a dictionary can be of any type.


#Creating an empty dictionary.
emailAddress = {}

#Adding data to empty dictionary.
emailAddress["febin"]="febin@gmail.com"
emailAddress["ajay"]="ajay@gmail.com"

#To print data of dictionary.
print(emailAddress)

#Creating another dictionary with data.
emailAddress2 = {"febin":"febin@gmail.com", "ajay":"ajay@gmail.com"}

#To print only keys.
emailAddress2.keys()

#To print only values.
emailAddress2.values()
