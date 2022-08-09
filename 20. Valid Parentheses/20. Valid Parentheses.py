class Solution:
    def isValid(self, s: str) -> bool:
        dict = {
            ')': '(',
            '}': '{',
            ']': '['
        }
        stack = deque()

        for i in range(0, len(s)):
            if s[i] == '(' or s[i] == '{' or s[i] == '[':
                stack.append(s[i])
            elif stack:
                if stack[-1] == dict[s[i]]:
                    stack.pop()
                else:
                    break
            else:
                stack.append(s[i])
                break

        if stack.__len__() == 0:
            return True
        else:
            return False