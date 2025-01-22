class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        tmp = {}
        for i in range(len(magazine)):
            if magazine[i] not in tmp:
                tmp[magazine[i]] = 1
            else:
                tmp[magazine[i]] += 1

        miss = True
        for j in range(len(ransomNote)):
            if ransomNote[j] in tmp:
                if tmp[ransomNote[j]] == 1:
                    del tmp[ransomNote[j]]
                else:
                    tmp[ransomNote[j]] -= 1
            else:
                miss = False
        return miss

solution = Solution()
print(solution.canConstruct("aa", "aab"))
print(solution.canConstruct("aa", "ab"))
