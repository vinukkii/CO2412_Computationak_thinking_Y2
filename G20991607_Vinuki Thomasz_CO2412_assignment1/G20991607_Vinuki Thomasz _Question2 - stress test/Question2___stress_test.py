import random 

from MasterClass import masterClass
from timeit import default_timer as time

# Randomly generated list 1 
randomList1 = []
randomList2 = []
randomList3 = []

# reference : https://pythonexamples.org/python-generate-random-number-of-specific-length/#:~:text=To%20generate%20a%20random%20number%20of%20given%20length%2C%20all%20we,(10%2C%20N)%2D1.
for _ in range(10000):          
     min = pow(10, 7-1) # to maintain the 7 digits of every randomly created number
     max = pow(10, 7 ) - 7
     randomList1.append(random.randint(min , max))
#print(randomList1)

for _ in range(100000):
     min = pow(10, 7-1)
     max = pow(10, 7 ) - 7
     randomList2.append(random.randint(min , max))
#print(randomList2)

for _ in range(1000000):
     min = pow(10, 7-1)
     max = pow(10, 7 ) - 7
     randomList3.append(random.randint(min , max))
##print(randomList3)

#--------------------------------------------------------------------------------------------

#  sorting for array1 :

print("ARRAY 1:\n")
#quick sort 
QS1Start = time()
randomList1Q = masterClass.quickSort(randomList1)
#print(randomList1Q)
QS1End = time()
print("Quick Sort time taken:\n", QS1End - QS1Start)

#merge sort
MS1Start = time()
randomList1M = masterClass.mergeSort(randomList1)
#print(randomList1M)
MS1End = time()
print("Merge Sort time taken:\n", MS1End - MS1Start)

#slection sort
SS1Start = time()
randomList1S = masterClass.selectionSort(randomList1)
#print(randomList1S)
SS1End = time()
print("Selection Sort time taken:\n", SS1End - SS1Start)

#--------------------------------------------------------------------------------------------
 # sorting for array2  : 
print("\n")
print("ARRAY 2:\n")
#quick sort 
QS2Start = time()
randomList2Q = masterClass.quickSort(randomList2)
#print(randomList2Q)
QS2End = time()
print("Quick Sort time taken:\n", QS2End - QS2Start)

#merge sort 
MS2Start = time()
randomList2M = masterClass.mergeSort(randomList2)
#print(randomList2M)
MS2End = time()
print("Merge Sort time taken:\n", MS2End - MS2Start)

#slection sort 
SS2Start = time()
randomList2S = masterClass.selectionSort(randomList2)
#print(randomList2S)
SS2End = time()
print("Selection Sort time taken:\n", SS2End - SS2Start)

#--------------------------------------------------------------------------------------------
# sorting for array3  : 9
print("\n")
#quick sort
print("ARRAY 3:\n")
QS3Start = time()
randomList3Q = masterClass.quickSort(randomList3)
#print(randomList3Q)
QS3End = time()
print("Quick Sort time taken:\n", QS3End - QS3Start)

#merge sort 
MS3Start = time()
randomList3M = masterClass.mergeSort(randomList3)
#print(randomList3M)
MS3End = time()
print("Merge Sort time taken:\n", MS3End - MS3Start)

#selection sort 
SS3Start = time()
randomList3S = masterClass.selectionSort(randomList3)
#print(randomList3S)
SS3End = time()
print("Selection Sort time taken:\n", SS3End - SS3Start)

#--------------------------------------------------------------------------------------------
# writting the sorted arrays to the file
# since all the arrays are sorted to obtain the same output, the quick sort of the 3 unsorted arrays are printed to the file

# to write to the file
list1QConverted = str(randomList1Q) # to convert the int list to string to take the iteration in a loop
list2QConverted = str(randomList2Q)
list3QConverted = str(randomList3Q)

print("\n")

with open ("SortedLists.txt" , "w") as sortFile:
    sortFile.write("THE 1ST ARRAY SORTED USING QUICK SORT OUTPUT :")
    sortFile.write("\n")
    for item in list1QConverted:
        sortFile.write(item)
    print("Sorted list1 is written to the file successfully!")
    sortFile.write("----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
    sortFile.write("\n")
    sortFile.write("\n")
    sortFile.write("\n")
    sortFile.write("\n")
    sortFile.write("\n")
    sortFile.write("\n")

    sortFile.write("THE 2ND ARRAY SORTED USING QUICK SORT OUTPUT :")
    sortFile.write("\n")
    for item in list2QConverted:
        sortFile.write(item)
    print("Sorted list2 is written to the file successfully!")
    sortFile.write("----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
    sortFile.write("\n")
    sortFile.write("\n")
    sortFile.write("\n")
    sortFile.write("\n")
    sortFile.write("\n")
    sortFile.write("\n")

    sortFile.write("THE 3RD ARRAY SORTED USING QUICK SORT OUTPUT :")
    sortFile.write("\n")
    for item in list3QConverted:
        sortFile.write(item)
    print("Sorted list3 is written to the file successfully!")






