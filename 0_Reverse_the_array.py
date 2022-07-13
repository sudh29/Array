t=int(input())
#print(t)
for i in range(t):
    n=int(input())
    arr=input().split()
    # print(arr)
    for i in range(len(arr)//2):
        arr[i],arr[n-1-i]=arr[n-1-i],arr[i]
    print(" ".join(arr))    
    # print(" ".join(arr[::-1]))
