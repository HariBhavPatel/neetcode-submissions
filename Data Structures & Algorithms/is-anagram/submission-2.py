class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #Solution that is O(1) 
        # check if len(s) != len(t) return false 
        # return and check if sorted(s) == sorted(t) 
        # There is no need to maintain order 
        if len(s) != len(t): 
            return False
        return sorted(s) == sorted(t)