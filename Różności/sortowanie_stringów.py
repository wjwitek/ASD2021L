"""
Mamy daną tablicę stringów, gdzie suma długości wszystkich stringów daje n. Napisz algorytm, który
posortuje tę tablicę w czasie O(n).
Można założyć, że stringi składają się wyłącznie z małych liter alfabetu łacińskiego.
"""


def countingSort(arr,k,idx,start):
    print(arr, start)
    count = [0]*k
    n = len(arr)
    for i in range(start,n):
        count[ord(arr[i][idx])-ord("a")] += 1
    for i in range(1,k):
        count[i] += count[i-1]
    new = [None]*n
    for i in range(n-1,start-1,-1):
        count[ord(arr[i][idx])-ord("a")] -= 1
        new[start+count[ord(arr[i][idx])-ord("a")]] = arr[i]
    for i in range(start,n):
        arr[i] = new[i]
    return arr


def sortString(A):
    n = len(A)
    norm = len(A[0])
    for i in range(1,n):
        if len(A[i]) > norm:
            norm = len(A[i])
    count = [0]*(norm+1)
    sizes = [0]*(norm+1)
    for i in range(n):
        count[len(A[i])] += 1
        sizes[len(A[i])] += 1
    for i in range(1,norm+1):
        count[i] += count[i-1]
    new = [None]*n
    for i in range(n-1,-1,-1):
        count[len(A[i])] -= 1
        new[count[len(A[i])]] = A[i]
    pivot = n
    print(new)
    for i in range(norm,0,-1):
        pivot -= sizes[i]
        new = countingSort(new,ord("z") - ord("a") + 1,i-1,pivot)
    return new

arr = ["abc","aaaaz","efgh","i","jk"]
sortString(arr)
print(arr)