from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}
        for num, item in enumerate(nums):
                m = target - item
                if m in d:
                    return [d[m], num]
                else:
                    d[item] = num
        return list(d)

def main():
    """Проверка алгоритма"""
    ex_s = Solution()
    nums = [2,7,11,15]
    target = 9
    print(ex_s.twoSum(nums,target))
    nums2 = [3,2,4] 
    target2 = 6
    print(ex_s.twoSum(nums2,target2))
    nums3 = [3,3]
    target3 = 6
    print(ex_s.twoSum(nums3,target3))
    nums4 = [3,2,3]
    target4 = 6
    print(ex_s.twoSum(nums4,target4))

if __name__ == "__main__":
    main()