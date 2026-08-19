class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # return false if len(s) != len(t)
        # Have a map of letters and count the frequency of the characters seen 
        # map(s)
        # Have a map of letters and count the frequency of characters seen 
        # map(t)
        # return if map(s) == map(t)
        sample_dict = {}
        target_dict = {} 
        if len(s) != len(t): 
            return False
        # Here is my dictionary implementation. 
        for char in s: 
	        sample_dict[char] = sample_dict.get(char,0) + 1 
        for char2 in t: 
            target_dict[char2] = target_dict.get(char2,0) + 1
        return sample_dict == target_dict
