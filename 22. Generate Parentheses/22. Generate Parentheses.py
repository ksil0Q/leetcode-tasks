from typing import List


def generateParenthesis(n: int) -> List[str]:    
    left = '('
    right = ')'


    res = []
    def create_combinations(sub: List[str],
                            left_count: int, right_count: int) -> None:
        
        if left_count == right_count == n:
            res.append(sub[:])
            return
    
        if left_count < n:
            sub.append(left)
            create_combinations(sub, left_count+1, right_count)
            sub.pop()

        if right_count < left_count:
            sub.append(right)
            create_combinations(sub, left_count, right_count+1)
            sub.pop()

            
    if n > 1:
        create_combinations([], 0, 0)
    else:

        return ['()']
    
    return list(map(lambda x: "".join(x), res))

################################################

if __name__ == '__main__':
    print(generateParenthesis(3)) # ["((()))","(()())","(())()","()(())","()()()"]