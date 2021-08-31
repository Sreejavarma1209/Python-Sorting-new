import time

# selection sort method
def selectionSort(sArray, length):  #sArray= name of the array
    for i in range(length):

        minIdx = i
        l=len(sArray)         #l=length of array

        for j in range(i + 1, l):
            if sArray[minIdx] > sArray[j]:
                minIdx = j

        # Swap
        sArray[i], sArray[minIdx] = sArray[minIdx], sArray[i]

    return sArray


# Inputarray = []
# k = 0
# size = int(input("Enter the size of the array: "))
#
# for k in range(size):
#     ans = int (input("Enter the  Element %d  : " % k))
#     Inputarray.append(ans)
#
# selectionstart = time.perf_counter()
# run = selectionSort(Inputarray, size)
# selectionend=time.perf_counter()
# runtime = selectionend - selectionstart
# print("Results after applying selection sort:", run)
# print("Run time of selection sort =", runtime)
