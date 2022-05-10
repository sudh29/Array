class Solution:
    def commonElements (self,A, B, C, n1, n2, n3):
        # your code here
        temp={}
        A=list(set(A))
        B=list(set(B))
        C=list(set(C))
        for i in A:
            if i in temp:
                temp[i]+=1
            else:
                temp[i]=1
        for i in B:
            if i in temp:
                temp[i]+=1
            else:
                temp[i]=1
        for i in C:
            if i in temp:
                temp[i]+=1
            else:
                temp[i]=1
        res=[]
        temp1=temp
        val=sorted(temp)
        #print(val)
        #print(temp1)
        for i in val:
            if temp1[i]==3:
                res.append(i)
        return res
