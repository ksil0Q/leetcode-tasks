def climbStairs(n: int) -> int:
    nums = [0, 1, 1]
    if n < 3:
        print(n)
        return n
    while len(nums[2:]) < n:
        nums.append(nums[-2] + nums[-1])
    print(nums[n+1])
    return 3


if __name__ == '__main__':
    climbStairs(2)

    # вставка элемента в списке n, а в словаре 1, собсно:

    # dic = {}
    # dic[0] = 0
    # dic[1] = 1
    # dic[2] = 2
    # if n == 1:
    #     return 1
    # if n == 2:
    #     return 2
    # for i in range(3, n + 1):
    #     dic[i] = dic[i - 1] + dic[i - 2]
    # return dic[n]

    # а это динпрог, что еще быстрее:

    # dp = {}  # n=>no of ways
    #
    # def dt(stair):
    #     if stair == n:
    #         return 1
    #     if stair > n:
    #         return 0
    #     if stair in dp:
    #         return dp[stair]
    #
    #     dp[stair] = dt(stair + 1) + dt(stair + 2)
    #
    #     return dp[stair]
    #
    # return dt(0)