import unittest
from timeout_decorator import timeout
from Solution import Solution

class UnitTest(unittest.TestCase):
    def setUp(self):
        self.__testcases = {
            ([2,3,1,1,4], True), ([3,2,1,0,4], False)
        }
        self.__solution = Solution()
        return super().setUp()
    
    @timeout(0.5)
    def test_case_0(self):
        nums, expectedOutput = self.__testcases[0]
        actualOutput = self.__solution.canJump(nums = nums)
        self.assertEqual(actualOutput, expectedOutput)

    @timeout(0.5)
    def test_case_1(self):
        nums, expectedOutput = self.__testcases[1]
        actualOutput = self.__solution.canJump(nums = nums)
        self.assertEqual(actualOutput, expectedOutput)

if __name__ == '__main__': unittest.main()