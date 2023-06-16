"""
    Given an array of strings strs, group the anagrams together. You can return the answer in any order.

    An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, 
    typically using all the original letters exactly once.
"""
# overall Complexity  | Time O(n * k) 
# base complexity O(n * K * 26(2) + n)
# n = the array holding the strings
# k = average length of each string length
# 26(2) | 0(1) = the two loops for building the charCounts and tempStr a-z(26 letters)
# additional complexity to iterate and build final list, worst case O(n)
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        strKeyValues = {} # key = strCharcounts: value = List[strings]
        outputList = []
        
        for string in strs:
            # initialize char to 26 indices with a count of zero
            charCounts = [0 for i in range(26)]
            strCharCounts = [0 for i in range(26)]
            tempStr = ""

            for char in string:
                charCounts[ord(char) - ord("a")] += 1
                strCharCounts[ord(char) - ord("a")] = char

            # build a string with the char ascii index and its how often it occurs in alphabetical order
            # have a string char array to prevent duplicate string number keys
            for index, valueCount in enumerate(charCounts):
                if valueCount != 0:
                    tempStr += strCharCounts[index] + str(index) + str(valueCount)

            # add that string as a key value in our dictionary
            # if key is not there set the key value as a list and append the current string
            # if key is valid simply append to the list already created
            if strKeyValues.get(tempStr) == None:
                strKeyValues[tempStr] = []
                strKeyValues[tempStr].append(string)
            else:
                strKeyValues[tempStr].append(string)
        
        # after our dictionary is complete simply go through it in our output list
        for key in strKeyValues:
            outputList.append(strKeyValues[key])
        
        return outputList