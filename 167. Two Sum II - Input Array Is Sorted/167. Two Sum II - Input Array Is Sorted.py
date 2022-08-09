def twoSum(numbers: list[int], target: int) -> list[int]:
    for i, first in enumerate(numbers):
        try:
            second = target - first
            t = numbers.index(second, i + 1)
            print([i + 1, t + 1])
            return [i + 1, t + 1]
        except ValueError:
            continue



if __name__ == '__main__':
    twoSum([2,7,11,15], 17)

        #     res = []
        # if len(numbers)==0 or numbers[0]*2>target or target>numbers[-1]*2:
        #     return res
        # low, high = 0, len(numbers)-1
        # while low<high:
        #     sum = numbers[low]+numbers[high]
        #     if sum<target or  (low>0 and numbers[low]==numbers[low-1]):
        #         low+=1
        #     elif sum>target or  (high<0 and numbers[high]==numbers[high+1]):
        #         high-=1
        #     else:
        #         res.append(low+1)
        #         res.append(high+1)
        #         return res
        # return res и все таки бин поиск быстрее