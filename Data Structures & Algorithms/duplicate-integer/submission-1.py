class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool: 
        seen = set()  # create an empty set
        for n in nums:
            if n in seen:   # if we've seen the number before → duplicate found
                return True
            seen.add(n)     # otherwise, add it to the set
        return False 