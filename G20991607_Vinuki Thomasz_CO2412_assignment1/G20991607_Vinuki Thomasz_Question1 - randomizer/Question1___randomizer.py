import random
import sys
sys.setrecursionlimit(6000)

#opening first name and last name files 
file1 = open("firstName.txt" , "r")
file2 = open("lastName.txt" , "r")

#  assigning the data of files to variables 
file1Data = file1.read() # reads file1 data to the variable
file2Data = file2.read() # reads file2 data to the variable


# to convert the variables to lists:
file1List = file1Data.split("\n") # splits the data in the variable to a list 
file2List = file2Data.split("\n") 

# to obtain counts 
# BEFORE TRIIMING :
# First name file:
print("Number of lines of data Before trimming the files :")
counter1 = 0; 
for i in file1List: # counts the number of lines in the file
    if i:
        counter1 = counter1 + 1
print("First Name : " , counter1)

# Last Name file : 
counter2 = 0;       # counts the number of lines in the file
for j in file2List:
    if j:
        counter2 = counter2 + 1
print("Last Name: " , counter2)

print("\n")
#making of lists to store the shuffled file content 
File1Random = []
File2Random = []

File1Random = random.choices(file1List , k = 4000)  # saves the 4000 first names
File2Random = random.choices(file2List , k = 4000)  # saves the 4000 last names 

#------------------------------------------------------------------------------------------
# to obtain counts 
# AFTER TRIMMING:

print("Number of lines of data After trimming the files :")

firstNameCount = len(File1Random) # takes the length of the file random list
lastNameCount = len(File2Random)
print("First name :" , firstNameCount)
print("Last name :" , lastNameCount)

#------------------------------------------------------------------------------------------

file3Data = open("fullName.txt" , "w")

for i in range (len(File1Random)) : # giving the range for the for loop as 4000
    file3Data.write(  File1Random[i] + " " + File2Random[i] + "\n" ) # string concatanation to form full names (first name + " " + last name)
    #str(i +1 ) + "." + # to add the number in front of the full name ( 1. abc def )
#-------------------------------------------------------------------------------------------
file4Data = open("fullName.txt" , "r")
fullnameVariable = file4Data.read()
print(fullnameVariable)
fullnameArray = fullnameVariable.split("\n") # converts the variable to a list

# Using iteration and recursion  : https://www.geeksforgeeks.org/python-program-to-return-the-length-of-the-longest-word-from-the-list-of-words/

# using iteration : 
sortingArray = [] # used to save the list which is later being sorted using a inbuilt function "sort"

def wordFinderIteration(nameArray , sortArray): # here the the full names are sorted using the sort function . the longest word is sorted to be the last element in the tuple 
    for item in nameArray:
        sortArray.append((len(item) , item ))   # here the appended data is written to a new array named sortArray
    return nameArray

wordFinderIteration(fullnameArray , sortingArray)

sortingArray.sort()
print("\n")

print( "USING ITERATION : ")
print("The longest word : " , sortingArray[-1][1]  )  # this is a tuple

print("The element number in the full name file :" , fullnameArray.index(sortingArray[-1][1]) +1 ) # because index starts from zero and to take the element no. we need to add a (+1)

print("Number of characters in the longest word: " , len(sortingArray[-1][1] ) -1 ) # (-1) is added to remove the space which is counted as a character 

print("\n")
# Using recursion : 
print("USING RECURSION:")
#

def wordFinderRecursion(nameArray):
    if len(nameArray) == 1:
        return nameArray[0]
     
    comparedTo = nameArray[0]
    longest = wordFinderRecursion( nameArray[1 :])

    if len(comparedTo) < len(longest):
        return longest

    else:
        return comparedTo


lonegstwordRecursion = wordFinderRecursion(fullnameArray )
print("The longest word is:" , lonegstwordRecursion)

letterCounter = 0
for i in lonegstwordRecursion:
    if i:
        letterCounter = letterCounter + 1 
print("No. of characters in the longest word using recursion :" , (letterCounter - 1) )  # (-1) is to remove the space between the first and last name

print ("\n")
print("---Note that the no of characters is counted without the space between the first name and the last name---")

#longestword = str(lonegstwordRecursion )
#lengthofWord = len((lonegstwordRecursion) - 1 )
#print("Number of characters in the longest word using recursion:" , lengthofWord )



