from typing import List

class Solution(object):
    def canJump(self, nums: List[int]) -> bool:
        # Variable to store the farthest index we can reach so far
        maxReach: int = 0
        
        # Iterate through each index and its jump value
        for i, jump in enumerate(nums):
            # If the current index is beyond our maximum reach,
            # it means we are stuck and cannot move further
            if i > maxReach:
                return False
            
            # Update the farthest index we can reach from the current position
            maxReach = max(maxReach, i + jump)
            
            # If at any point we can reach or go beyond the last index,
            # we can directly return True
            if maxReach >= len(nums) - 1:
                return True
        
        # If the loop finishes, it means we can reach the end
        return True