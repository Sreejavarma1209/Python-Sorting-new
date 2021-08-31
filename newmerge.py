import time

# left-leftarray
# right - rightArray
#method to perform merge
def merge(left, right):
    ans = []
    i, j = 0, 0

    while i < len(left) and j < len(right):

        if left[i] < right[j]:
            ans.append(left[i])
            i += 1
        else:
            ans.append(right[j])
            j += 1

    while i < len(left):
             ans.append(left[i])
             i += 1

    while j < len(right):
             ans.append(right[j])
             j += 1

    return ans
#method to perform Merge Sort
def mergeSort(mArray):
    length=len(mArray)
    if length == 1:
        return mArray

    mid = length // 2

    lP = mergeSort(mArray[0:mid])       #lP=left Partition, rP=right Partition
    rP = mergeSort(mArray[mid:])

    return merge(lP, rP)



# inputArray = []
# size = int (input("Enter the array size : "))
#
# for i in range(size):
#     ans = int (input("Enter the  Element %d : " % i))
#     inputArray.append(ans)
#
# merge_start = time.perf_counter()
# s = mergeSort(inputArray)
# runtime = time.perf_counter() - merge_start
# print("Results after applying Merge sort:", s)
# print("Runtime of Merge sort=", runtime)
