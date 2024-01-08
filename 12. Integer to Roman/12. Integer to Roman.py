int_roman = {
    1 : 'I',
    5 : 'V',
    10 : 'X',
    50 : 'L',
    100 : 'C',
    500 : 'D',
    1000 : 'M'
}

def intToRoman(num: int) -> str:
    denominator = 1000
    res = ''

    while num > 0:
        if denominator > num:
            denominator //= 10
            continue

        cur_num = num // denominator
        cur_let = ''
        
        if cur_num == 4:
            cur_let = "".join([int_roman[denominator], int_roman[5 * denominator]])
        elif cur_num == 9:
            cur_let = "".join([int_roman[denominator], int_roman[10 * denominator]])
        elif cur_num == 5 or cur_num == 1:
            cur_let = int_roman[cur_num * denominator]
        elif cur_num < 4:
            cur_let = int_roman[denominator] * cur_num
        elif cur_num > 5:
            cur_let = "".join([int_roman[5 * denominator], int_roman[denominator] * (cur_num - 5)])

        num = num % denominator
        denominator //= 10
        res = f"{res}{cur_let}"
    return res 


########################################

if __name__ == '__main__':
    print(intToRoman(40)) # XL
    print(intToRoman(90)) # XC
    print(intToRoman(3)), # III
    print(intToRoman(400)) # CD
    print(intToRoman(58)), # LVIII
    print(intToRoman(1994)), # MCMXCIV
##################################
    print(intToRoman(3999)), # MMMCMXCIX
    print(intToRoman(2165)), # MMCLXV
    print(intToRoman(715)) # DCCXV