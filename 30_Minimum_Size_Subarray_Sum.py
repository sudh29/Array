import sys
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n=len(nums)
        res=sys.maxsize
        i=0
        j=1
        temp=nums[i]
        if temp>=target: return 1
        if j<n: temp+=nums[j]
        while(i<n and j<n): 
            if temp>=target:
                res=min(res,j-i+1)
                temp-=nums[i]
                i+=1
            else:
                j+=1
                if j<n:
                    temp+=nums[j]
        return res if res<sys.maxsize else 0
        
