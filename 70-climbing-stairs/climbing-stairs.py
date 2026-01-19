class Solution(object):
    def climbStairs(self, n):
        
        if n <= 2:
            return n

        prev, curr = 1, 2
        for _ in range(3, n + 1):
            prev, curr = curr, prev + curr

        return curr


        """
        def fib(num):
            if num == 0:
                return 0
            elif num == 1:
                return 1
            elif num == 2:
                return 2
            return fib(num-1) + fib(num-2)
        
        
        return fib(n)
        """
