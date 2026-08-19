class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen_map = {}
        for index, value in enumerate(nums): 
            needed = target - value 
            if needed in seen_map: 
                return [seen_map[needed], index] 
            seen_map[value] = index