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
        a , b = 1, 2
        for i in range(2,n):
            a , b = b, a + b
        return b
if __name__ == '__main__':
    unittest.main()
