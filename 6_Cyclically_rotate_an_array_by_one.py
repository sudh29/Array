def rotate( arr, n):
    m=len(arr)
    rem=n%(m+1)
    
    '''for i in range(rem-1):
        temp=arr.pop(0)
        arr.append(temp)'''
    for i in range(rem-1,0,-1):
        arr[i],arr[i-1]=arr[i-1],arr[i]
