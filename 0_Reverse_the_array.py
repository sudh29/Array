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

    
    
# Two pointer approach

def reverse_array(arr):
    start = 0
    end = len(arr) - 1
    while start < end:
        arr[start], arr[end] = arr[end], arr[start]
        start += 1
        end -= 1
