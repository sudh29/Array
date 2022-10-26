class Solution:
        def segregateElements(self, arr, n):
        # Your code goes here
        # temp1=[i for i in arr if i<0]
        # temp2=[i for i in arr if i>=0]
        # temp=(temp2+temp1)
        # for i in range(n):
        #     arr[i]=temp[i]
        # return arr
        
        for i in range(n):
            if arr[i]>=0:
                pos=i
                break
        for i in range(n):
            if arr[i]<0:
                neg=i
                break
        while(pos<n and neg<n):
            if pos<neg:
                pos+=1
            else:
                arr[pos],arr[neg]=arr[neg],arr[pos]
                pos+=1
                neg+=1
        
        print(arr)
