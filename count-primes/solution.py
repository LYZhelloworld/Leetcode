class Solution:
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 2:
            return 0

        primes = [True for i in range(n)]
        primes[0] = False
        primes[1] = False

        for i in range(2, n):
            if primes[i] == True:
                for m in range(2, (n - 1) // i + 1):
                    primes[i * m] = False

        return primes.count(True)
