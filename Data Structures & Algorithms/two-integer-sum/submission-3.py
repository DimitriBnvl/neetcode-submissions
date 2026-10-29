class Solution:
    # def twoSum(self, nums: List[int], target: int) -> List[int]:
    #     for index1,i in enumerate(nums):
    #         for index2, j in enumerate(nums[1:]):
    #             sum = i + j
    #             if sum == target and index1 != (index2 + 1):
    #                 return [index1, index2+1]    

    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevMap = {}  # val -> index

        for i, n in enumerate(nums):
            diff = target - n
            if diff in prevMap:
                return [prevMap[diff], i]
            prevMap[n] = i