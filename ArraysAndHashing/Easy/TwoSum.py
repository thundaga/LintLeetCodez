"""
Given an array of integers nums and an integer target, 
return indices of the two numbers such that they add up to target.

Assume that each input would have exactly one solution, 
and not use the same element twice.

Answer can be returned in any order.
"""

# Overall complexity | time O(n) | space O(n)
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict_val = {}
        output_list = [] # number : number occurrence
        find_number = 0

        # Array value unto a dict and give it a value of how often it shows up
        # time O(n) | space O(n)
        for element in nums:
            if (dict_val.get(element) == None):
                dict_val.update({element : 1})
            else:
                dict_val[element] += 1

        # check difference of cur index num to dictionary excluding is own number
        # if we find a valid difference for the target num then hold it until we find its index and break out
        for indx, element in enumerate(nums):
            # check for a valid key that could be the targets difference
            if dict_val.get(target - element) != None and len(output_list) == 0:
                # make sure its not a duplicate
                if target - element != element:
                    output_list.append(indx)
                    find_number = target - element
                # if a duplicate make sure its count is greater than 1
                elif dict_val.get(target - element) > 1:
                    output_list.append(indx)
                    find_number = target - element
            # after finding the first element find the second number and add its index
            elif find_number == element and len(output_list) == 1:
                output_list.append(indx)
                break

        return output_list