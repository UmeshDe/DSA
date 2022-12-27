#An array is given but its order is not mentioned ascending descending

# arr = [1, 4, 5, 6, 7, 8, 9]
arr = [9,8,7,6,5,3,2,1]
l = 0
u = len(arr) -1 
s = 8

def binarySearch(arr, l, u, s):
    while l <= u:
        if l == u:
            return l if arr[l] == s else -1
        else:
            order = "ASC" if arr[l] < arr[l+1] else "DESC"
            mid = l + (u - l) // 2
            if order == "ASC":
                if arr[mid] == s:
                    return mid
                elif arr[mid] < s:
                    l = mid + 1
                else:
                    u = mid - 1
            else:
                if arr[mid] == s:
                    return mid
                elif arr[mid] < s:
                    u = mid - 1
                else:
                    l = mid + 1
    return -1

print(binarySearch(arr, l, u, s))