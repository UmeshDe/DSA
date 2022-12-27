#find position of 1st index of inf value
import math
arr = [-23, 40, 50,2,27,-89, float('inf'), float('inf'), float('inf')]
l = 0
n = 9
u = n-1

#linear approach
def linearSearch(arr, n):
    for i in range(n):
        if arr[i] == float('inf'):
            return i

def binarySearch(arr, l, u):
    while l <= u:
        mid = l + (u-l)//2
        if type(arr[mid]) == int:
            l = mid + 1
        elif math.isinf((arr[mid]))  and type(arr[mid-1]) == int:
            return mid
        else:
            u = mid - 1



print(linearSearch(arr, n))
print(binarySearch(arr, l, u, n))