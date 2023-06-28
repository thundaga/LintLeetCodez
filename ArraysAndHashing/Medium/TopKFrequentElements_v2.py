"""
Given an integer array nums and an integer k, return the k most frequent elements. return array elements in any order
"""
# overall Complexity | Time O(n) | Space O(n)
# base time complexity O(n + k + n + n)
# n = iterate through array of nums then dictionary O(n) worst case then iterate through final array
# k = iterate through k most elements, this will occur once in total as we go through final array backwards
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
       output = []
       # key(number) values(number frequency)
       strKeyValues = {}

       # Array index = occurence count | Array innerlist = list of numbers with count
       # Max length is original list length since its also the max occurence count
       countValues = [[] for i in range(len(nums) + 1) ]

       for num in nums:
           # fill up the dictionary if empty start at 0 and add 1
           strKeyValues[num] = 1 + strKeyValues.get(num, 0)

       # iterate dict and fill up the countvalue array with the number occurences
       for keyNum, valueFreq in strKeyValues.items():
            countValues[valueFreq].append(keyNum)

       # iterate backwards on 2d array and stop at k most elements
       for index in range(len(countValues) - 1, 0, -1):
            for num in countValues[index]:
                if (len(output) == k):
                    return output
                else:
                    output.append(num)
                    
       return output
            
            



