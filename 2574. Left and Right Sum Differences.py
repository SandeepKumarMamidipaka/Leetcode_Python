class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        leftSum=[]
        rightSum=[]
        leftSum.append(0)
        l_sum=0
        for i in range(len(nums)-1):
            l_sum+=nums[i]
            leftSum.append(l_sum)
        rightSum.append(0)
        r_sum=0
        for i in range(len(nums)-1,0,-1):
            r_sum+=nums[i]
            rightSum.append(r_sum)
        rightSum.reverse()
        # print(leftSum)
        res=[]
        for i in range(len(leftSum)):
            n=abs(leftSum[i]-rightSum[i])
            res.append(n)
        return res
