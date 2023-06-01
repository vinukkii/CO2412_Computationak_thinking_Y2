# -*- coding: utf-8 -*-
"""
Created on Sun Sep 18 23:49:48 2022

@author: aiamini
"""

from contextlib import redirect_stdout
from heapq import merge


class masterClass:
 
 # code for QUICK SORT    #https://youtu.be/kFeXwkgnQ9U
  def quickSort(sequence):
    
    length = len(sequence)
    if length <= 1:
        return sequence
    else:
        pivot = sequence.pop()

    items_greater = []
    items_lower = []
    items_SortedQ = []

    for item in sequence:
        if item > pivot:
            items_greater.append(item)

        else:
            items_lower.append(item)
    items_SortedQ = masterClass.quickSort((items_lower)) + [pivot] + masterClass.quickSort((items_greater))     
    return items_SortedQ
  
   
   #-------------------------------------------------------------------------------------------------------------------------------------------
   # code for MERGE SORT  #https://youtu.be/rAqBlKhy_oI
    
  def mergeSort (sequence): 

      if len(sequence) <= 1:
          return sequence

      midpoint = int(len(sequence) / 2 )

      leftArray , rightArray = masterClass.mergeSort(sequence[ : midpoint ])  , masterClass.mergeSort(sequence[ midpoint :] )

      return masterClass.mergefunction ( leftArray , rightArray) # returning a new function named merge with the 2 arrays

  
  def mergefunction (leftArray , rightArray ) :

      resultedArray = []
      leftPointer =  rightPointer = 0

      while leftPointer < len(leftArray) and rightPointer < len(rightArray) :

          if leftArray[leftPointer] < rightArray[rightPointer]: 

              resultedArray.append(leftArray[leftPointer])

              leftPointer += 1


          else:

              resultedArray.append(rightArray[rightPointer])

              rightPointer += 1 


      resultedArray.extend(leftArray[leftPointer :])
      resultedArray.extend(rightArray[rightPointer :])
       
      
      return resultedArray

   #-------------------------------------------------------------------------------------------------------------------------------------------
   # code for SELECTION SORT  #https://youtu.be/4CykZVqBuCw
  def selectionSort(sequence):
    indexing_length = range(0, len(sequence)-1) # (-1) is added cuz when the unsorted list ends up becoming one element, it is automatically assigned as the last element in the sorted list

    for i in indexing_length:
        min_value = i

        for j in range(i+1, len(sequence)):
            if sequence[j] < sequence[min_value]:
                min_value = j

            if min_value != i:
                sequence[min_value], sequence[i] = sequence[i], sequence[min_value]

    return sequence
      




  
    
    
    

    

    
