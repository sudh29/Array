class Solution:
    def segregateElements(self, arr, n):
        # Your code goes here
        temp1=[i for i in arr if i<0]
        temp2=[i for i in arr if i>=0]
        temp=(temp2+temp1)
        for i in range(n):
            arr[i]=temp[i]
        return arr
