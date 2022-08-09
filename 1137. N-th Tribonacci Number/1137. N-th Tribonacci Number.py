def tribonacci(self, n: int) -> int:
    memo = {}
    memo[0] = 0
    memo[1] = 1
    memo[2] = 1
    def dp(n, memo):
        if n in memo: return memo[n]

        memo[n - 1] = dp(n - 1, memo)
        memo[n - 2] = dp(n - 2, memo)
        memo[n - 3] = dp(n - 3, memo)
        return memo[n - 1] + memo[n - 2] + memo[n - 3]

    return dp(n, memo)