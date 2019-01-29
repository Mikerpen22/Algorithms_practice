from random import randrange

def partition(arr):
    # Pick random index from 0~(len(arr)-1), the value will be our pivot's value by swapping
    # So we can still perform the for loop as usual
    rand_index = randrange(len(arr))
    arr[rand_index], arr[0] = arr[0], arr[rand_index]

    # The first value of the arr as pivot
    pivot = 0
    i = 1  # To distinguish >P, <P
    for j in range(1, len(arr)):  # Leave pivot alone and perform partitioning
        if arr[j] <= arr[0]:
            # swap i,j element to remain partition pattern(not i-1 since j will be swapping with the pivot then)
            arr[j], arr[i] = arr[i], arr[j]
            i += 1  # we have move a element to the left side of pivot

    arr[pivot], arr[i-1] = arr[i-1], arr[pivot]  # Swap the pivot back to its rightful position
    return arr, i-1


def r_select(array, i):
    if len(array) == 1:
        return array[0]
    else:
        array_partitioned, pivot_ind = partition(array)
        if (pivot_ind + 1) == i:  # We add 1 to pivot_ind since we are comparing the 'num' of elements not the index itself.
            return array_partitioned[pivot_ind]
        elif (pivot_ind + 1) > i:
            return r_select(array_partitioned[:pivot_ind], i)
        else:
            return r_select(array_partitioned[(pivot_ind+1):], i-(pivot_ind+1))


test = [43, 5, 99, 100, 72, 33, 77, 66, 3]
ans = r_select(test, 2)
print(ans)
