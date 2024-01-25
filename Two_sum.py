class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}  # Dictionary to store seen numbers and their indices
        for i, num in enumerate(nums):
            complement = target - num  # Calculate the complement
            if complement in seen:  # Check if complement has been seen before
                return [seen[complement], i]  # Return indices if found
            seen[num] = i  # Store the current number and its index
        return None