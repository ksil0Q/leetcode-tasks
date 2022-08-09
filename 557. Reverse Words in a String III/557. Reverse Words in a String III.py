def reverseWords(s: str) -> str:
    return ' '.join([temp[::-1] for temp in s.split()])
    


if __name__ == '__main__':
    reverseWords("Let's take LeetCode contest")