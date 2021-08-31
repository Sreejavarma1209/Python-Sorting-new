import time

#bubble Sort method
def bubbleSort(bArray, length):

    for i in range (length):
        for j in range (length-i-1):
            if bArray[j] > bArray[j + 1]:
                #swap
                bArray[j], bArray[j+1] = bArray[j+1], bArray[j]
    return bArray     #return array after sorting

# inputArray = []
# size = int (input ("Enter the size of the array: "))
#
# for k in range (size):
#     ans = int (input ("Enter the  Elements %d : " % k))
#     inputArray.append (ans)
#
# bubblestart = time.perf_counter()
# run=bubbleSort(inputArray,size)
# bubbleend = time.perf_counter()
# runtime = bubbleend-bubblestart
# print("Results after performing Bubble sort:" ,run)
# print ("Runtime of bubble sort=", runtime)