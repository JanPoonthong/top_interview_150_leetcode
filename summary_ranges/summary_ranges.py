class Solution:
    def summaryRanges(self, nums: list[int]) -> list[str]:
        tmp = []
        i = 0

        while i < len(nums):
            start = nums[i]

            while i < len(nums) - 1 and nums[i] + 1 == nums[i+1]:
                i += 1
            
            if start != nums[i]:
                tmp.append(str(start) + '->' + str(nums[i]))
            else:
                tmp.append(str(nums[i]))
        i += 1

        return tm





solution = Solution()
print(solution.summaryRanges([0,1,2,4,5,7]))
print(solution.summaryRanges([0,2,3,4,6,8,9]))
