def isPalindrome(s: str) -> bool:
    s = s.replace(' ', '')
    s = s.lower()

    for sign in s:
        if not sign.isalnum():
            s = s.replace(sign, '')

    if len(s) == 0:
        print(True)
        return True

    first = s[:len(s) // 2]
    if len(s) % 2 == 1:
        second = s[len(s) // 2 + 1:]
    else:
        second = s[len(s) // 2:]

    if first == second[::-1]:
        print(True)
        return True
    else:
        print(False)
        return  False



if __name__ == '__main__':
    isPalindrome('abbba')

    # s = re.sub("[^0-9a-zA-Z]+", '', s)
    # s = s.lower()
    # return s == s[::-1]