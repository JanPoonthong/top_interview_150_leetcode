class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        for i in nums[::]:
            if i == val:
                nums.remove(i)
        return len(nums)

solution = Solution()
print(solution.removeElement(nums=[3,2,2,3], val = 3))