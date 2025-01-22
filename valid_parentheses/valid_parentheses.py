class Solution:
    def isValid(self, s: str) -> bool:
        opening = ['(', '[', '{']
        closing = [')', ']', '}']
        stack = []
        
        for c in s:
            if c in opening:  # If it's an opening bracket, push it onto the stack
                stack.append(c)
            elif c in closing:  # If it's a closing bracket
                # Check if the stack is empty or the top of the stack doesn't match
                if not stack or stack[-1] != opening[closing.index(c)]:
                    return False
                stack.pop()  # Pop the matched opening bracket from the stack
        
        # If the stack is empty, all brackets were matched
        return len(stack) == 0

# Testing the solution
solution = Solution()
print(solution.isValid("([)]"))  # Output: False
print(solution.isValid("([])"))  # Output: True
print(solution.isValid("(]"))    # Output: False
print(solution.isValid("()[]{}"))  # Output: True
