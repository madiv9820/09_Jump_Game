from typing import List

class Solution(object):
    def canJump(self, nums: List[int]) -> bool:
        """
        🧠 Jump Game — Bottom-Up Dynamic Programming (Tabulation)
        Goal: Check if we can reach the last index starting from the first.
        """
        
        n: int = len(nums)
        cache: List[bool] = [False] * n   # 🗂️ cache[i] → can we reach the end from index i?
        cache[-1] = True                  # 🏁 Last index can always reach itself

        # 🔁 Iterate from second-last index down to 0
        for currentIndex in range(n - 2, -1, -1):
            # 📏 Calculate farthest index we can jump to (bounded by last index)
            maxJump: int = min(currentIndex + nums[currentIndex], n - 1)

            # 🔍 Check if any next reachable index can lead to the end
            for i in range(currentIndex + 1, maxJump + 1):
                if cache[i]:                    # ✅ If we can reach end from i
                    cache[currentIndex] = True  # then we can also reach from currentIndex
                    break                       # ⚡ Stop early once True found

        # 🚀 Final answer: can we reach the end from index 0?
        return cache[0]