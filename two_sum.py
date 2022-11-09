class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        objects = {}
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in objects:
                return [i, objects[complement]]
            objects[nums[i]] = i