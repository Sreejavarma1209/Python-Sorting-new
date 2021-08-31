import time
#Method to perform Quick Sort
def quickSort_median(arr, lowest, highest):
    if lowest < highest:
        p = partition(arr, lowest, highest)
        quickSort_median(arr, lowest, p - 1)
        quickSort_median(arr, p + 1, highest)
    return arr

#A=Array name
#Method to get pivot value
def pivot(A, lowest, highest):
    mid = (lowest + highest) // 2
    if A[lowest] <= A[mid] <= A[highest]:
        return mid
    if A[highest] <= A[mid] <= A[lowest]:
        return mid
    if A[lowest] <= A[highest] <= A[mid]:
        return highest
    if A[mid] <= A[highest] <= A[lowest]:
        return highest
    return lowest

#method to divide the array values according to pivot
def partition(A, lowest, highest):
    pivotIdx = pivot(A, lowest, highest)
    pivotValue = A[pivotIdx]
    A[pivotIdx], A[lowest] = A[lowest], A[pivotIdx]
    pointer = lowest

    for i in range(lowest, highest + 1):
        if A[i] < pivotValue:
            pointer += 1
            A[i], A[pointer] = A[pointer], A[i]
    A[lowest], A[pointer] = A[pointer], A[lowest]

    return pointer


# inputArray = []
# i = 0
# size = int (input ("Enter the array size : "))
#
# for i in range (size):
#     ans = int (input ("Enter the  Element %d of List : " % i))
#     inputArray.append (ans)
# quickMstart = time.perf_counter()
# run = quickSort_median(inputArray, 0, len(inputArray) - 1)
# quickMedian_time = time.perf_counter() - quickMstart
# print("Results after applying quick sort using Median:", run)
# print("Runtime=", quickMedian_time)

