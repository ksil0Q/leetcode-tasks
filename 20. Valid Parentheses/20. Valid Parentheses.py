from collections import deque


def isValid(s: str) -> bool:
    my_dict = {
        ')': '(',
        '}': '{',
        ']': '['
    }
    stack = deque()

    for i in range(0, len(s)):
        if s[i] == '(' or s[i] == '{' or s[i] == '[':
            stack.append(s[i])
        elif stack:
            if stack[-1] == my_dict[s[i]]:
                stack.pop()
            else:
                break
        else:
            stack.append(s[i])
            break

    if stack.__len__() == 0:
        print(True)
        return True
    else:
        print(False)
        return False


if __name__ == '__main__':
    # isValid('(){}[]')
    # isValid('(){}[')
    # isValid(')({}[')
    # isValid('(){[]')
    # isValid('(){}]')
    # isValid('({()}[)]')
    # isValid('({()})[]')
    isValid('(])')
