def minCostClimbingStairs(cost: list[int]) -> int:
    n = len(cost)
    for i in range(2, n):
        cost[i] += min(cost[i - 1], cost[i - 2])
    print(cost[i])
    return min(cost[n - 1], cost[n - 2])


if __name__ == '__main__':
    minCostClimbingStairs([10, 15, 20])
    # [1,100,1,1,1,100,1,1,100,1]