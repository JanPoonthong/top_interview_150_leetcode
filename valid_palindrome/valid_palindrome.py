class Solution:
    def isPalindrome(self, s: str) -> bool:
        boo = False
        i = 0
        s = s.lower()
        s = ''.join(e for e in s if e.isalnum())
        j = len(s) - 1
        if len(s) == 0:return True
        while i <= j:
            if s[i] == s[j]:
                boo = True
            else:
                boo = False
                break
            i += 1
            j -= 1
        return boo


solution = Solution()
print(solution.isPalindrome("A man, a plan, a canal: Panama"))
print(solution.isPalindrome(" "))
