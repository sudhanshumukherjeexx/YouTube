#Implementation of Selection Sort using Python

numList = [9,8,7,6,5,4,3,2,1]

def selectionSort(array):

    for i in range(len(array)):
        smallestIndex = i

        for j in range(i+1, len(array)):

            if array[j] < array[smallestIndex]:
                smallestIndex = j
        #swapping the elements
        (array[i],array[smallestIndex]) = (array[smallestIndex],array[i])
    return ("Selection Sort Implemented :",array)

print(selectionSort(numList))
