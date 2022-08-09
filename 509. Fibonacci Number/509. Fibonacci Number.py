def fib(n: int) -> int:
    def recurse(n):
        if n == 0:
            return 0
        elif n == 1:
            return 1
        if n in d:
            return d[n]
        d[n] = recurse(n - 1) + recurse(n - 2)
        return d[n]

    d = {}
    return recurse(n)



if __name__ == '__main__':
    fib(4)


    # def dp(n, memo):
    #     if n in memo: return memo[n]
    #     if n <= 1:
    #         memo[n] = n
    #         return memo[n]
    #     memo[n - 1] = dp(n - 1, memo)
    #     memo[n - 2] = dp(n - 2, memo)
    #     return memo[n - 1] + memo[n - 2]
    #
    # return dp(n, memo={})
