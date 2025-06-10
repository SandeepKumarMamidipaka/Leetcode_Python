class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        res=[]
        sum1=0      
        for i in nums:
            sum1+=i
            res.append(sum1)
        return res
