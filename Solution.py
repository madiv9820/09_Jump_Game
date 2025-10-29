from typing import List

class Solution(object):
    def canJump(self, nums: List) -> bool:
        """
        🏃‍♂️ Jump Game — Recursive (Brute Force) Solution
        Goal: Check if we can reach the last index starting from the first one.
        """

        def check(currentIndex: int = 0) -> bool:
            # 🏁 Base case: if we reach or cross the last index, return True
            if currentIndex >= len(nums) - 1:
                return True

            # 🚫 If not yet at the end, try all possible jumps from this position
            canJump: bool = False
            maxJumps: int = nums[currentIndex]  # 🔢 How far we can jump from here

            # 🔁 Try every jump length (1 to maxJumps)
            for i in range(1, maxJumps + 1):
                # Recursively check if jumping i steps gets us to the end
                canJump |= check(currentIndex + i)  # (Bitwise OR → True if any path works)

            # 🔙 Return whether any jump path succeeded
            return canJump

        # 🚀 Start checking from index 0
        return check()