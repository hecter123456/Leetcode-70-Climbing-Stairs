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
    def __init__(self):
        self.dic = {0:1, 1:1}
    def climbStairs(self, n):
        if n not in self.dic:
            self.dic[n] = self.climbStairs(n-1) + self.climbStairs (n-2)
        return self.dic[n]
if __name__ == '__main__':
    unittest.main()
