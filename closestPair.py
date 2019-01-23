import math


def combine_xy(x_arr, y_arr):
    # combine x_arr and y_arr to combined list of (x,y) tuples
    return list(zip(x_arr, y_arr))


def x_sort(xy_arr):
    # sort array according to x value
    return sorted(xy_arr, key=lambda x: x[0])


def y_sort(xy_arr):
    # sort array according to y value
    return sorted(xy_arr, key=lambda x: x[1])


def euclidean(a, b):
    # returns distance between two (x,y) pairs
    return ((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2) ** 0.5


def brute(xy_arr):
    dmin = math.inf
    for i, pnt_i in enumerate(xy_arr[:-1]):  # [:-1] to avoid last point of the array since the next line will cover it
        # No need to create a list to store distance, directly find the min by updating
        dis_storage_min = min(euclidean(pnt_i, pnt_j) for pnt_j in xy_arr[i+1:])
        if dis_storage_min < dmin:
            dmin = dis_storage_min

    return dmin


def closest_split_pair(p_x, p_y, delta, best_pair):
    len_x = len(p_x)
    x_bar = p_x[len_x // 2][0]
    Sy = [x for x in p_y if (x_bar-delta) <= x[0] <= (x_bar+delta)]  # Sy being points from p_y limited by delta
    best = delta
    for i in range(len(Sy)-1):
        # From i search for at most 7 points will have d(p, q) < delta
        # min(i+7, len(Sy)-i) since the arr might approach the end and have less than 7 elements left
        for j in range(1, min(i+7, len(Sy)-i)):
            p, q = Sy[i], Sy[i+j]
            dist = euclidean(p, q)
            if dist < best:
                best = dist
                best_pair = (p, q)
    return best_pair


def closestPair(Px, Py):
    if len(Px) <= 3:
        return brute(Px)

    mid = len(Px) / 2

    # Divide into left and right
    Q, R = Px[:mid], Px[mid:]

    # For Q and R, sort with x-coord and y-coord respectively(這兩行看不懂)
    Qx, Qy = [sorted(Q, key=lambda x:x[0]), sorted(Q, key=lambda x:x[1])]
    Rx, Ry = [sorted(R, key=lambda x:x[0]), sorted(R, key=lambda x:x[1])]

    # Recursively call closestPair till it have less or equal to three points
    (p1, q1) = closestPair(Qx, Qy)
    (p2, q2) = closestPair(Rx, Ry)

    d = min(euclidean(p1, q1), euclidean(p2, q2))  # get the minimum dist
    mn = min((p1, q1), (p2, q2), key=lambda x: euclidean(x[0], x[1]))  # get the minimum pair
    (p3, q3) = closest_split_pair(Px, Py, d, mn)

    return min(mn, (p3, q3), key=lambda x: euclidean(x[0], x[1]))

