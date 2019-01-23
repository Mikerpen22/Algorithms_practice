def mergeSort(arr):
    if len(arr) == 1:
        return arr
    else:
        a = arr[:len(arr)//2]
        b = arr[len(arr)//2:]

        print('a and b before: ', a, b)
        a = mergeSort(a)
        b = mergeSort(b)
        c = []
        print('a and b after:', a, b)

        i = 0
        j = 0
        while i < len(a) and j < len(b):
            if a[i] < b[j]:
                c.append(a[i])
                i = i + 1
            else:
                c.append(b[j])
                j = j + 1

        c += a[i:]
        c += b[j:]
        print('result', c)
    return c

inp = [9, 2, 5, 6, 4, 1, 12, 55]
print(mergeSort(inp))