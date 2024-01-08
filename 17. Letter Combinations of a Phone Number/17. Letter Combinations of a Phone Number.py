from typing import List

all_letters = {
    '2': ('a', 'b', 'c'),
    '3': ('d', 'e', 'f'),
    '4': ('g', 'h', 'i'),
    '5': ('j', 'k', 'l'),
    '6': ('m', 'n', 'o'),
    '7': ('p', 'q', 'r', 's'),
    '8': ('t', 'u', 'v'),
    '9': ('w', 'x', 'y', 'z')
}


def letterCombinations(digits: str) -> List[str]:    
    digits_len = len(digits)

    res = []
    def create_combinations(index: int, sub: List[str]) -> None:
        if len(sub) == digits_len:
            res.append(sub[:])
            return
        
        letters = all_letters[digits[index]]

        for letter in letters:
            sub.append(letter)
            create_combinations(index + 1, sub)
            sub.pop()

    if len(digits) > 0:
        create_combinations(0, [])
    else:
        return []
    
    return list(map(lambda x: "".join(x), res))


########################################
if __name__ == '__main__':
    print(letterCombinations("234"))