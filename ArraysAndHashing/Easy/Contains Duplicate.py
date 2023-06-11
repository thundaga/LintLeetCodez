"""
    Given an integer array nums, return true if any value appears at least twice in the array, 
    and return false if every element is distinct.
"""

class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        dict_value = {}
        output = False
        for value in nums:
            # if not in dict add it else if already in dict break and return true
            if dict_value.get(str(value)) == None:
                dict_value[str(value)] = value
            else:
                output = True
                break
        
        # overall Complexity | Time O(n) | Space O(n)
        return output