class Solution:
    def rearrange(self,arr, n):
        # code here
        arr1=[i for i in arr if i<0]
        arr2=[j for j in arr if j>=0]
        i=0
        while arr1 and arr2:
            arr[i]=arr2.pop(0)
            i+=1
            arr[i]=arr1.pop(0)
            i+=1
        while arr1:
            arr[i]=arr1.pop(0)
            i+=1  
        
        while arr2:
            arr[i]=arr2.pop(0)
            i+=1 
