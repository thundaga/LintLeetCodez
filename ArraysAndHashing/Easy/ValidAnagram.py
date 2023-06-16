"""
    Given two strings s and t, return true if t is an anagram of s, and false otherwise.

    An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, 
    typically using all the original letters exactly once.
"""
# Overall complexity | time O(s + t) | Space O(n)
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        dict_values = {}
        output = True
        # add the base string to a dictionary and the number of times its value shows up
        for char in s:
            if dict_values.get(char) == None:
                dict_values[char] = 1
            else:
                dict_values[char] += 1
        
        # check if t is anagram of s
        for char in t:
            if dict_values.get(char) == None or dict_values.get(char) == 0:
                output = False
                break
            else:
                dict_values[char] -= 1

        return output