def convert(s: str, numRows: int) -> str:
    if numRows == 1:
        return s
    
    res = ''
    cycle_len = 2 * (numRows - 1)
    
    for j in range(0, numRows):
        temp_str = ''
        temp_cycle_len = cycle_len - j * 2 == 0 and cycle_len or cycle_len - j * 2
        i = j
        while i < len(s):
            temp_str += s[i]

            i += temp_cycle_len
            temp_cycle_len = cycle_len - temp_cycle_len if cycle_len - temp_cycle_len != 0 else cycle_len 

        res += temp_str
        
    return res