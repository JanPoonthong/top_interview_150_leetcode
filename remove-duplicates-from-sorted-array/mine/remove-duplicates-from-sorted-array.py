class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        swap = 0
        tmp = {}
        for k in nums:
            if k not in tmp:
                tmp[k] = 1
            else:
                tmp[k] += 1

        for i in range(len(nums)-1):
            for j in range(i+1, len(nums)):
                if nums[j] > nums[i]:
                    nums[j], nums[i+1] = nums[i+1], nums[j]
                    swap += 1
                    break
        return len(tmp)


solution = Solution()
print(solution.removeDuplicates([1,1,2]))
print(solution.removeDuplicates([0,0,1,1,1,2,2,3,3,4]))
