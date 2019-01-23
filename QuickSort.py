## Quick sorting without in place partitioning
# def quickSort(arr):
#     less = []
#     equal = []
#     greater = []
#
#     if len(arr) > 1:
#         # Select the first element as pivot
#         pivot = arr[0]
#         for i in arr:
#             if i > pivot:
#                 greater.append(i)
#             elif i == pivot:
#                 equal.append(pivot)
#             else:
#                 less.append(pivot)
#
#         return quickSort(less) + equal + quickSort(greater)
#
#     else:
#         return arr


## QuickSort with in place partitioning
def partition(arr, low, high):
    # Take the first of the sub arr as pivot
    pivot = low
    i = low + 1
    for j in range(low+1, high+1):  # Leave pivot alone and perform partitioning
        if arr[j] <= arr[low]:
            arr[j], arr[i] = arr[i], arr[j]  # swap i,j element to remain partition pattern
            i += 1  # we have move a element to the left side of pivot

    arr[pivot], arr[i-1] = arr[i-1], arr[pivot]
    print(arr)
    return i-1

def inplaceQuickSort(arr, begin=0, end=None):
    if end is None:
        end = len(arr) - 1

    def quickSort(array, begin, end):
        if begin >= end:  # We have exactly one element in the array
            return

        # Find pivot and by partition, put it in the right place
        pivot = partition(array, begin, end)
        quickSort(array, begin, pivot-1)
        quickSort(array, pivot+1, end)
    return quickSort(arr, begin, end)


array = [97, 200, 100, 101, 211, 101]
inplaceQuickSort(array)
print(array)
