class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}

        for ind, val in enumerate(nums):
            dif = target - val
            if dif in seen:
                return seen[dif], ind
            seen[val] = ind

        return []