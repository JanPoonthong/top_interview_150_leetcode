class Solution:
    def romanToInt(self, s: str) -> int:
        roman_dict = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }

        output = 0
        for i in range(len(s) - 1):
            if roman_dict[s[i]] < roman_dict[s[i + 1]]:
                output += (-roman_dict[s[i]])
            else:
                output += (roman_dict[s[i]])
        return output + roman_dict[s[-1]]


solution = Solution()
# print(solution.romanToInt("III"))
print(solution.romanToInt("CMXCVIII"))
print(solution.romanToInt("MCMXCIV"))
