arr = [20,40,68,80,90,120,240]
target = 210


#linear search O(n)
def linearsearch(arr, target):
    for i in range(len(arr)):
        num = target - arr[i]
        for j in range(i+1, len(arr)):
            if arr[j] == num:
                return (i,j)
    return -1

#binary search O(nlogn)
def binarySearch(arr, target):
    for i in range(len(arr)):
        num = target - arr[i]
        j = i + 1
        u = len(arr) - 1
        while j <= u:
            if arr[j] == num:
                return (i,j)
            else:
                mid = j + (u-j)//2
                if arr[mid] == num:
                    return i, mid
                elif arr[mid] < num:
                    j = mid + 1
                else:
                    u = mid - 1 
    return -1

#two pointers approach O(n)
def twoPointersApproach(arr, target):
    l = 0
    r = len(arr) - 1
    while l <= r:
        if arr[l] + arr[r] == target:
            return (l,r)
        elif arr[l] + arr[r] < target:
            l = l + 1
        else:
            r = r - 1

print(linearsearch(arr, target))
print(binarySearch(arr, target))
print(twoPointersApproach(arr, target))

