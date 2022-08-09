class Solution:
    def maxPower(self, s: str) -> int:
        substring = s[0]
        maxsub = s[0]
        s += '!'
        for i, letter in enumerate(s[:-1]):
            maxsub = substring if len(maxsub) < len(substring) else maxsub
            substring += letter
            if s[i] != s[i+1]:
                substring = ''
                substring += s[i+1]
        maxsub += s[-1] if s[-1] == maxsub[0] else ''
        return len(maxsub)