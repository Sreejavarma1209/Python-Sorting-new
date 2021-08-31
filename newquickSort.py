import time

#method to perform partition
def partition(inputArray, least, highest):             #l=low , h=high
    count = (least - 1)
    pi = inputArray[highest]

    for j in range(least, highest):

        if inputArray[j] <= pi:
            count += 1
            inputArray[count], inputArray[j] = inputArray[j], inputArray[count]

    inputArray[count + 1], inputArray[highest] = inputArray[highest], inputArray[count + 1]
    return count + 1


# Method to do Quick sort


def quickSort(array, lowest, highest):
    if len(array) == 1:
        return array
    if lowest < highest:
        pi = partition(array, lowest, highest)

        # Separately sort elements before
        # partition and after partition
        quickSort(array, lowest, pi - 1)
        quickSort(array, pi + 1, highest)
    return array

# inputArray = []
# i = 0
# size = int (input ("Enter the array size : "))
#
# for i in range (size):
#     ans = int (input ("Enter the  Element %d of List : " % i))
#     inputArray.append (ans)
# quick_start = time.perf_counter()
# run=quickSort(inputArray, 0, size-1)
# quick_time = time.perf_counter()- quick_start
# print("Results after performing Quick Sort:", run)
#
# print ("Quick sort Runtime=", quick_time)

