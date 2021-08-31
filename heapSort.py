import time

#method to heapify
def heapify(array, n, i):
    greatest= i
    left = 2 * i + 1
    right = 2 * i + 2


    if left < n and array[greatest] < array[left]:
        greatest = left


    if right < n and array[greatest] < array[right]:
        greatest = right


    if greatest != i:
        #swap
        array[i], array[greatest] = array[greatest], array[i]

        # Heapify the root.
        heapify(array, n, greatest)


# method to perform heap Sort


def heapSort(heaparr):
    length = len(heaparr)

    # Build a maxheap.
    for i in range(length // 2 - 1, -1, -1):
        heapify(heaparr, length, i)
    for i in range(length - 1, 0, -1):
        #swap
        heaparr[i], heaparr[0] = heaparr[0], heaparr[i]
        heapify(heaparr, i, 0)
    return heaparr



# inputArray = []
# i = 0
# size = int (input ("Enter the size of the array : "))
#
# for i in range (size):
#    ans= int (input ("Enter the  Element %d  : " % i))
#    inputArray.append (ans)
#
# heap_start = time.perf_counter()
# run = heapSort(inputArray)
# runtime = time.perf_counter() - heap_start
# print("Results after applying heap Sort:", run)
#
# print ("Runtime=", runtime)
