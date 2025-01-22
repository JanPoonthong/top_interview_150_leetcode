class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        i = 0
        n = len(nums) - 1

        while i <= n:
            if nums[i] == val:
                nums[i] = nums[n]
                n -= 1
            else:
                i += 1

        return n

solution = Solution()
print(solution.removeElement(nums=[0,1,2,2,3,0,4,2], val = 2))