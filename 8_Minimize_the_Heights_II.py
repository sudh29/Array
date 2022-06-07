class Solution:
    def getMinDiff(self, arr, n, k):
        # code here
        if(n==1):
           return 0
        arr.sort()
        diff = arr[n-1] - arr[0]
        for i in range(1,n):
            if(arr[i]-k < 0):
                continue
            max_val = max(arr[i-1]+k,arr[n-1]-k)
            min_val = min(arr[0]+k,arr[i]-k)
            diff = min(diff,max_val-min_val)
        return diff
