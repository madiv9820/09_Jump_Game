from typing import List

class Solution(object):
    def canJump(self, nums: List[int]) -> bool:
        """
        🧠 Jump Game — Top-Down DP (Memoized Recursive Approach with Pruning)
        Objective: Determine if we can reach the last index starting from the first.
        """

        n: int = len(nums)
        cache: List[bool] = [None] * n   # 🗂️ Cache stores whether index i can reach the end

        def check(currentIndex: int = 0) -> bool:
            """
            Recursively checks if we can reach the last index from currentIndex.
            Uses memoization to avoid recomputation.
            """

            # 🏁 Base case: If we reach or cross the last index → success!
            if currentIndex >= n - 1: return True

            # 🔍 If not computed before, calculate it now
            if cache[currentIndex] is None:
                maxJump: int = nums[currentIndex]    # Maximum steps we can jump from here
                canJump: bool = False                # Assume we can't reach yet

                # 🔁 Explore all jump possibilities (1 → maxJump)
                for i in range(1, maxJump + 1):
                    # Recursively check next position
                    canJump |= check(currentIndex + i)
                    # ⚡ Optimization: Stop early if we already found a valid path
                    if canJump: break

                # 💾 Save result in cache
                cache[currentIndex] = canJump

            # 📦 Return cached result (True/False)
            return cache[currentIndex]

        # 🚀 Start checking from index 0
        return check()