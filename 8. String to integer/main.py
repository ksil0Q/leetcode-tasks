def myAtoi(s: str) -> int:
    i = 0
    n = len(s)

    while i < n and s[i] == ' ':
        i += 1

    positive = 0
    negative = 0

    if i < n and s[i] == '+':
        positive += 1
        i += 1

    if i < n and s[i] == '-':
        negative += 1
        i += 1

    if positive > 0 and negative > 0:
        return 0
    
    ans = 0

    while i < n and '0' <= s[i] <= '9':
        ans = ans * 10 + (ord(s[i]) - ord('0'))
        i += 1

    if negative > 0:
        ans = -ans

    if ans > 2**31 - 1:
        return 2**31 - 1

    if ans < -2**31:
        return -2**31

    return int(ans)

print(myAtoi("-91283472332"))