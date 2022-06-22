# Given an array nums. We define a running sum of an array as runningSum[i] = sum(nums[0]…nums[i]).

# Return the running sum of nums.

# Example 1:

# Input: nums = [1,2,3,4]
# Output: [1,3,6,10]
# Explanation: Running sum is obtained as follows: [1, 1+2, 1+2+3, 1+2+3+4].
# Example 2:

# Input: nums = [1,1,1,1,1]
# Output: [1,2,3,4,5]
# Explanation: Running sum is obtained as follows: [1, 1+1, 1+1+1, 1+1+1+1, 1+1+1+1+1].
# Example 3:

# Input: nums = [3,1,2,10,1]
# Output: [3,4,6,16,17]
 

# Constraints:

# 1 <= nums.length <= 1000
# -10^6 <= nums[i] <= 10^6

class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        counter = 0
        empty_arr = []
        for i in nums:
            counter += i
            empty_arr.append(counter)
                    
        return empty_arr

nums = [1,2,3,4]

# Complexity Analysis

# Time complexity: O(n)O(n) where nn is the length of the input array. This is because we use a single loop that iterates over the entire array to calculate the running sum.

# Space complexity: O(1)O(1) since we don't use any additional space to find the running sum. Note that we do not take into consideration the space occupied by the output array.

