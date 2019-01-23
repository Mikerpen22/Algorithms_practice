def mergeSortInversions(arr):
    if len(arr) == 1:
        return arr, 0
    else:
        a = arr[:len(arr)//2]
        b = arr[len(arr)//2:]

        print('a and b before: ', a, b)
        a, ai = mergeSortInversions(a)
        b, bi = mergeSortInversions(b)
        c = []
        print('a and b after:', a, b)

        i, j = 0, 0
        inversions = ai + bi  # Sum up both sides inversion count
        print('inversions accumulated:', ai, '+', bi, '=', inversions)

        while i < len(a) and j < len(b):
            if a[i] < b[j]:
                c.append(a[i])
                i += 1
            else:
                c.append(b[j])
                j += 1
                # Choosing from b means elements in a after a[i] is out of order with current b element
                inversions += (len(a) - i)

        c += a[i:]
        c += b[j:]
        print('result:', c, ', how many inversions:', inversions)

    return c, inversions

inp = [9, 2, 5, 6, 4, 1, 12, 55]
print(mergeSortInversions(inp))