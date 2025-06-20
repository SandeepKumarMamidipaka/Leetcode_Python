class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        unique=[]
        for i in range(len(nums)):
            b=True
            for j in unique:
                if nums[i]==j:
                    b=False
            if(b):
                unique.append(nums[i])
        res=[]
        for i in unique:
            c=0
            for j in nums:
                if i==j:
                    c+=1
            if c==2:
                res.append(i)
        return res
        
