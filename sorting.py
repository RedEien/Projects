import random
import time
import sys
# set a new recursion limit
sys.setrecursionlimit(10000) # (default is 1000)
# create a list with random numbers
numList = []
numListLength = input('how many numbers do you want in your list? ')
for num in range(int(numListLength)):
    numList.append(random.randint(1,100)) # random numbers from 1 to 100
# the sorting algorithms in random order from https://www.geeksforgeeks.org/sorting-algorithms/#algo
# bubbleSort
def bubbleSort(bubbleSortList):
    n = len(bubbleSortList)

    for i in range(n):
        for j in range(0, n-i-1):
            if bubbleSortList[j] > bubbleSortList[j+1] :
                bubbleSortList[j], bubbleSortList[j+1] = bubbleSortList[j+1], bubbleSortList[j]
# recursive bubblesort
def reBubbleSort(reBubbleSortList):
    for i, num in enumerate(reBubbleSortList):
        try:
            if reBubbleSortList[i+1] < num:
                reBubbleSortList[i] = reBubbleSortList[i+1]
                reBubbleSortList[i+1] = num
                reBubbleSort(reBubbleSortList)
        except IndexError:
            pass
    return reBubbleSortList
# quicksort
def partition(quickSortList, low, high):
    i = ( low -1 )
    pivot = quickSortList[high]

    for j in range(low, high):
        if quickSortList[j] < pivot:
            i = i + 1
            quickSortList[i], quickSortList[j] = quickSortList[j], quickSortList[i]
    quickSortList[i+1], quickSortList[high] = quickSortList[high], quickSortList[i+1]
    return ( i+1 )
def quickSort(quickSortList, low, high):
    if low < high:
        pi = partition(quickSortList, low, high)
        quickSort(quickSortList, low, pi-1)
        quickSort(quickSortList, pi+1, high)
# shellsort
def shellSort(shellSortList):
    n = len(shellSortList)
    gap = n//2

    while gap > 0:
        for i in range(gap, n):
            temp = shellSortList[i]
            j = i
            while j >= gap and shellSortList[j-gap] > temp:
                shellSortList[j] = shellSortList[j-gap]
                j -= gap
            shellSortList[j] = temp
        gap //= 2
# mergesort
def mergeSort(mergeSortList):
    if len(mergeSortList) > 1:
        mid = len(mergeSortList)//2
        L = mergeSortList[:mid]
        R = mergeSortList[mid:]

        mergeSort(L)
        mergeSort(R)

        i = j = k = 0

        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                mergeSortList[k] = L[i]
                i+=1
            else:
                mergeSortList[k] = R[j]
                j+=1
            k+=1

        while i < len(L):
            mergeSortList[k] = L[i]
            i+=1
            k+=1

        while j < len(R):
            mergeSortList[k] = R[j]
            j+=1
            k+=1
# selectionsort
def selectionSort(selectionSortList):
    for i in range(len(selectionSortList)):
        min_idx = i
        for j in range(i+1, len(selectionSortList)):
            if selectionSortList[min_idx] > selectionSortList[j]:
                min_idx = j
        selectionSortList[i], selectionSortList[min_idx] = selectionSortList[min_idx], selectionSortList[i]
# the random list
print(numList)
# Bubble Sort
bubbleSortList = numList.copy()
bubbleSortStart = time.perf_counter()
bubbleSort(bubbleSortList)
bubbleSortEnd = time.perf_counter()
bubbleSortTimer = bubbleSortEnd - bubbleSortStart
# Recursive Bubble Sort
reBubbleSortList = numList.copy()
reBubbleSortStart = time.perf_counter()
reBubbleSort(reBubbleSortList)
reBubbleSortEnd = time.perf_counter()
reBubbleSortTimer = reBubbleSortEnd - reBubbleSortStart
# Quick Sort
quickSortList = numList.copy()
quickSortStart = time.perf_counter()
n = len(quickSortList)
quickSort(quickSortList, 0, n-1)
quickSortEnd = time.perf_counter()
quickSortTimer = quickSortEnd - quickSortStart
# Shell Sort
shellSortList = numList.copy()
shellSortStart = time.perf_counter()
shellSort(shellSortList)
shellSortEnd = time.perf_counter()
shellSortTimer = shellSortEnd - shellSortStart
# Merge Sort
mergeSortList = numList.copy()
mergeSortStart = time.perf_counter()
mergeSort(mergeSortList)
mergeSortEnd = time.perf_counter()
mergeSortTimer = mergeSortEnd - mergeSortStart
# Selection Sort
selectionSortList = numList.copy()
selectionSortStart = time.perf_counter()
selectionSort(selectionSortList)
selectionSortEnd = time.perf_counter()
selectionSortTimer = selectionSortEnd - selectionSortStart
# Output with clumsy timer
print('bubbleSortList', round(bubbleSortTimer, 6),'seconds')# : ', bubbleSortList)
print('reBubbleSortList: ', round(reBubbleSortTimer, 6),'seconds')# : ', reBubbleSortList)
print('quickSortList: ', round(quickSortTimer, 6),'seconds')# : ', quickSortList)
print('shellSortList: ', round(shellSortTimer, 6),'seconds')# : ', shellSortList)
print('mergeSortList: ', round(mergeSortTimer, 6),'seconds')# : ', mergeSortList)
print('selectionSortList: ', round(selectionSortTimer, 6),'seconds')# : ', selectionSortList)
#check for valid algorithms
if bubbleSortList == reBubbleSortList == quickSortList == shellSortList == mergeSortList == selectionSortList:
    print('alright, all lists are equal:')
    print(bubbleSortList)