from re import L


arr = [1, 4, 5, 6, 7, 8, 9]
l = 0
u = len(arr) -1 
s = 4

def binarySearch(arr, l, u, s):
    while l <= u:      
        if l == u:
            return l if arr[l] == s else -1
        else:
            mid = l + (u-l)//2
            if arr[mid] == s:
                return mid
            elif arr[mid] < s:
                l = mid + 1
            else:
                u = mid - 1

print(binarySearch(arr, l, u, s))

# T.C = O(logn)
# S.C = O(1)