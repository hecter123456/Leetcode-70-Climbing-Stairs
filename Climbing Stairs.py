import unittest

class unitest(unittest.TestCase):
    def testNone(self):
        Input = 0
        Output = 1
        self.assertEqual(Solution().climbStairs(Input),Output)
    def testSample(self):
        Input = 3
        Output = 3
        self.assertEqual(Solution().climbStairs(Input),Output)

class Solution():
    def climbStairs(self, n):
        if n == 0 or n == 1:
            return 1
        return self.climbStairs(n-1) + self.climbStairs (n-2)

if __name__ == '__main__':
    unittest.main()
