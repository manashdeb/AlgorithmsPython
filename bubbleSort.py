#!/usr/bin/env python
# coding: utf-8

# Approach1: Using while loop

def bubbleSort(intList):
    print(f"initial list: {intList}")
	# used to track number of operations used by the algorithm
    ops=0
	# used to track number of passes made by the while loop below
    passCount=0
	# boolean to check if list is already sorted
    sorted=False
    while(sorted==False):
        sorted=True
        passCount+=1
        for i in range(len(intList)-passCount):
            ops+=1
            if intList[i]>intList[i+1]:
			    # swap adjacent values in the list
                temp=intList[i]
                intList[i]=intList[i+1]
                intList[i+1]=temp
                sorted=False
    print(f"final list:   {intList}, total ops {ops}")    
bubbleSort([4,1,1,3,9,5,2,5,8,4])


# Approach2: Using two for loops


def bubbleSort(intList):
    print(f"initial list: {intList}")
    ops=0
    for i in range(len(intList)-1):
        swapped=False
        for j in range(len(intList)-1-i):
            ops+=1
            if intList[j]>intList[j+1]:
                temp=intList[j]
                intList[j]=intList[j+1]
                intList[j+1]=temp
                swapped=True
        if not swapped:
            break
#         print(f"list values:  {intList}, total ops {ops}")        
    print(f"final list:   {intList}, total ops {ops}")    
bubbleSort([4,1,1,3,9,5,2,5,8,4])

