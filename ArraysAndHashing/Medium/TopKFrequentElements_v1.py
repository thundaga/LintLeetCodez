"""
Given an integer array nums and an integer k, return the k most frequent elements. return array elements in any order
"""
# overall Complexity | Time O(n * k) | Space O(n)
# base time complexity O(n * K + n)
# n = iterate through array of nums to build dictionary and second n to iterate over it
# k = iterate through k most elements
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # key(number) value (frequency)
        strKeyValues = {}
        output = []

        # we are going to input an identifier per each valid number and its occurence
        for num in nums:
            if strKeyValues.get(num) == None:
                strKeyValues[num] = 1
            else:
                strKeyValues[num] += 1

        # go through and manage the leaderboard of most frequent numbers
        for key in strKeyValues:
            minIndexFreq = 0
            smallestFreq = 0

            # input any key number if we haven't filled the array yet
            if (len(output) < k):
                output.append(key)
            # once its filled the subsequent numbers will start replacing the smallest occurences
            else:
                smallestFreq = strKeyValues[output[minIndexFreq]]
                for index in range(k):
                    # check if occurence is smaller than the smallest occurence
                    if strKeyValues[output[index]] < smallestFreq:
                        smallestFreq = strKeyValues[output[index]]
                        minIndexFreq = index

                # decide whether to replace if new key is bigger than the smallest one
                if strKeyValues[key] > strKeyValues[output[minIndexFreq]]:
                    output[minIndexFreq] = key

        return output

            
            



