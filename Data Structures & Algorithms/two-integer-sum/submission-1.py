class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for index1,i in enumerate(nums):
            for index2, j in enumerate(nums[1:]):
                sum = i + j
                if sum == target and index1 != (index2 + 1):
                    return [index1, index2+1]    

    # for pos, i in nums:
    #   for pos, j in nums - i:
    #       sum =  i + j
    #       if sum = target then return [i,]