numberList = [1,2,3,6,7,8,9,11,12,13,15,17,28,30,34,37,42,47,50]

#Implementing Binary Search

def binarySearch(myList, myNum):
    low = 0
    high = len(myList) - 1

    while low <= high:
        mid = round((low + high)/2)
        mySearch = myList[mid]
        
        if mySearch == myNum:
            print("{0} is found at the index value of {1}".format(myNum,mid))
        if mySearch > myNum:
            high = mid - 1
        else:
            low = mid + 1
    return ("Binary Search Implemented")

print(binarySearch(numberList, 30))
print(binarySearch(numberList, 50))
print(binarySearch(numberList, 6)) 