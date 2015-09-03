# List and tuple are hybrid data type means it can be used to handle multiple data type data

myFirstList = [3, 4, 5.6, "cow", "goat"]
myFirstList
print(myFirstList)

#To print first element of list.
myFirstList[0]
print(myFirstList[0])

#To print all character after first character.
print(myFirstList[1:])

#To repeat content of list multiple times.
myFirstList*3

#To add two list.
mySecondList= [44, 55, "Hi"]
myFirstList + mySecondList

#To update list.
myFirstList[2]="New York"

#Tuple works same as list but only we cannot update tuple

myFirstTuple = (3, 4, 5.6, "cow", "goat")

