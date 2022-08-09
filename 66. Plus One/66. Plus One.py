class Solution:
    def plusOne(digits: list[int]) -> list[int]:
        num = 1
        i = 0

        while i < len(digits):
            num += digits[i] * (10 ** i)
            i += 1

        digits.clear()
        while num > 0:
            digits.append(num % 10)
            num = num // 10

        digits.reverse()
        print(digits)
        print(bin(int('11', base=2) + int('1', base=2))[2:])

    if __name__ == '__main__':
        plusOne([1,2,3])


