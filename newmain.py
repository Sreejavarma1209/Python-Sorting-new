import time

from heapSort import heapSort
from newquickSort import quickSort
from quickUsingMedian import quickSort_median
from insertionSort import insertionSort
from bubbleSort import bubbleSort
from selectionSort import selectionSort
from newmerge import mergeSort
import numpy as np
import matplotlib.pyplot as plt


def main():
    # getting the input from the user
    globalArr = []
    size = int(input("Enter the size of the array : "))

    for i in range(size):
        value = int (input("Enter the  Element %d of array : " % i))
        globalArr.append(value)

    print(globalArr)
    arrayForSelectionSort = globalArr.copy()
    selection_start = time.perf_counter()
    r = selectionSort(arrayForSelectionSort, size)
    selection_time = time.perf_counter() - selection_start
    print("Results after performing Selection sort:", r)
    print("Run time of Selection Sort =", selection_time)

    arrayForbubbleSort = globalArr.copy()
    bubble_start = time.perf_counter()
    r = bubbleSort(arrayForbubbleSort, size)
    bubble_time = time.perf_counter() - bubble_start
    print("Results after performing Bubble sort:", r)
    print("Runtime of Bubble sort =", bubble_time)

    arrayForMergeSort = globalArr.copy()
    merge_start = time.perf_counter()
    r = mergeSort(arrayForMergeSort)
    merge_time = time.perf_counter() - merge_start
    print("Results after performing Merge sort:", r)
    print("Runtime of Merge sort=", merge_time)

    arrayForInsertionSort = globalArr.copy()
    insertion_start = time.perf_counter()
    r = insertionSort(arrayForInsertionSort, size)
    insertion_time = time.perf_counter() - insertion_start
    print("Results after performing Insertion sort:", r)
    print("Runtime of Insertion sort=", insertion_time)

    arrayForQuickSort = globalArr.copy()
    quick_start = time.perf_counter()
    r = quickSort(arrayForQuickSort, 0, len(arrayForQuickSort) - 1)
    quick_time = time.perf_counter() - quick_start
    print("Results after performing Quick sort:", r)
    print("Runtime of Quick sort=", quick_time)

    arrayForQuickSortMedian = globalArr.copy()
    quickstart_UsingMedain = time.perf_counter()
    r = quickSort_median(arrayForQuickSortMedian, 0, len(arrayForQuickSortMedian) - 1)
    quickMedian_time = time.perf_counter() - quickstart_UsingMedain
    print("Result after performing Quick sort using Median:", r)
    print("Runtime of Quick sort using Median=", quickMedian_time)

    arrayForheapSort = globalArr.copy()
    heap_start = time.perf_counter()
    r = heapSort(arrayForheapSort)
    heap_time = time.perf_counter() - heap_start
    print("Results after performing Heap sort:", r)
    print("Runtime of Heap sort=", heap_time)

    x = [bubble_time, insertion_time, selection_time, heap_time, merge_time, quick_time, quickMedian_time]
    plt.xticks(np.arange(7), (
    'bubblesort', 'insertionsort', 'selectionsort', 'heapsort', 'mergesort', 'quicksort', 'quickSortUsingMedian'))
    plt.plot(x, 'bo', x, 'r')
    plt.show()


main()