def partition(arr, low, high):
    i = (low - 1)  # index of smaller element
    pivot = arr[high]  # pivot

    for j in range(low, high):

        # If current element is smaller than or
        # equal to pivot
        if arr[j] <= pivot:
            # increment index of smaller element
            i = i + 1
            arr[i], arr[j] = arr[j], arr[i]
    i += 1
    # 最后交换一下pivot
    arr[i], arr[high] = arr[high], arr[i]
    return i


# The main function that implements QuickSort
# arr[] --> Array to be sorted,
# low  --> Starting index,
# high  --> Ending index

# Function to do Quick sort
def quickSort(arr, low, high):
    if low < high:
        # pi is partitioning index, arr[p] is now
        # at right place
        pi = partition(arr, low, high)

        # Separately sort elements before
        # partition and after partition
        quickSort(arr, low, pi - 1)
        quickSort(arr, pi + 1, high)

# arr[] = {10, 80, 30, 90, 40, 50, 70}
# Indexes:  0   1   2   3   4   5   6
#
# low = 0, high =  6, pivot = arr[h] = 70
# Initialize index of smaller element, i = -1
# i的下一位一定是比pivot大的数，因为只要比pivot小，i，j就会同步走