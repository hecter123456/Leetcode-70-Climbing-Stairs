import unittest

class unitest(unittest.TestCase):
    def testNone(self):
        Input = 0
        Output = 1
        self.assertEqual(Solution().climbStairs(Input),Output)

class Solution():
    def climbStairs(self, n):
        if n == 0:
            return 1

if __name__ == '__main__':
    unittest.main()