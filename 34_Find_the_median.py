class Solution:
	def find_median(self, v):
		# Code here
		v.sort()
		#print(v)
		n=len(v)
		if n%2==0:
		    return (v[n//2]+v[(n//2)-1])//2
	    else:
	        return v[n//2]
