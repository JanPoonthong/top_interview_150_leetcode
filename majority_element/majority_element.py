class Solution:
    def my_max(self, tmp) -> int:
        current_max = 0
        a = 0
        for key, value in tmp.items():
            if value > current_max:
                current_max = value
                a = key
        return a

    def majorityElement(self, nums: list[int]) -> int:
        tmp = {}
       for num in nums:
            if num not in tmp:
                tmp[num] = 1
            else:
                tmp[num] += 1

        return self.my_max(tmp)

solution = Solution()
print(solution.majorityElement([2,2,1,1,1,2,2]))
print(solution.majorityElement([3,2,3]))
