def rotate( arr, n):
    m=len(arr)
    rem=n%(m+1)
    #print(m,n,rem)
    for i in range(rem-1):
        temp=arr.pop(0)
        arr.append(temp)
