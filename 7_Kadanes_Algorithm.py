
class Solution:
    ##Complete this function
    #Function to find the sum of contiguous subarray with maximum sum.
    def maxSubArraySum(self,arr,N):
        ##Your code here
        max_so_far=-100000000
        max_end_her=0
        for i in arr:
            max_end_her=max(i,max_end_her+i)
            max_so_far=max(max_so_far,max_end_her)
        return max_so_far
