arr = [2, 0, 4, 0, 12, 34, 66, 21, 0, 1]


def pushZeroesToEnd(arr):

    count = 0
    l = len(arr)
    try:
        for i in range(l):
            if arr[i] == 0:
                arr.pop(i)
                count += 1
                l -= 1
    except:
        pass

    for _ in range(count):
        arr.append(0)

    return arr


print(pushZeroesToEnd(arr))
