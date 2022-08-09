class Solution:
    def romanToInt(self, s: str) -> int:
        num = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000,
            'O': 0}
        s += '!' if len(s) % 2 == 1 else '!!'
        i = 0
        result = 0
        while s[i+1] != '!':
            result += makenumber(s[i], s[i+1], num)
            i += 1
        else:
            result += makenumber(s[i], 'O', num)
        return result


def makenumber(first: str, second: str, num: dict) -> int:
    result = 0

    if first == second:
        result += num[first]
    elif num[first] < num[second]:
        result = result - num[first]
    else:
        result += num[first]
    return result