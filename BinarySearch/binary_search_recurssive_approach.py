def binarySearch(arr, l, u, s):
    if l == u:
        return l if arr[l] == s else -1
    else:
        mid = l + (u - l) // 2
        if arr[mid] == s:
            return mid
        elif arr[mid] < s:
            return binarySearch(arr, mid+1, u, s)
        else:
            return binarySearch(arr, l, mid-1, s)

arr = [5,8,1,4,6,9,7]
arr.sort()
print(arr)
l = 0
u = len(arr) - 1
s = 5
print(binarySearch(arr, l, u, s))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            