class Solution:
    def countPrimes(self, n: int) -> int:
        if n <= 2:
            return 0
        
        prime_number = [True] * n
        
        prime_number[0] = prime_number[1] = False
        
        for i in range(2, int(n**0.5)+1):
            if prime_number[i]:
                for j in range(i*i, n, i):
                    prime_number[j] = False
        
        return sum(prime_number)