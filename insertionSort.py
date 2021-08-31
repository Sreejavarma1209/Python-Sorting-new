import time

#insertion sort method
def insertionSort(iarr, n):

    for i in range(n):
        data = iarr[i]
        j = i-1
        while j >= 0 and data < iarr[j]:
            iarr[j+1] = iarr[j]
            j -= 1
        iarr[j+1] = data
    return iarr


# inputArray = []
# size = int (input ("Enter the array size : "))
#
# for k in range(size):
#     ans=int (input("Enter the elements %d: " %k))
#     inputArray.append(ans)
# insertionstart=time.perf_counter()
# run=insertionSort(inputArray,size)
# runtime = time.perf_counter()-insertionstart
#
#
# print ("Results after applying insertion sort:", run)
# print (" Runtime of insertion sort:", runtime)
