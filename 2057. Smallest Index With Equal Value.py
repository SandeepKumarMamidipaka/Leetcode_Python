class Solution:
    def smallestEqual(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            n=i%10
            if n==nums[i]:
                return i
        return -1
