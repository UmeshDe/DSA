from re import L


arr = [9,8,7,6,5,3,2,1]
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
                u = mid - 1
            else:
                l = mid + 1

print(binarySearch(arr, l, u, s))

# T.C = O(logn)
# S.C = O(1)