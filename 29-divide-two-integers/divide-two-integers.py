class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        positive = (dividend < 0) is (divisor < 0) 
        dividend = abs(dividend)
        divisor =  abs(divisor) 
        res = 0 
        while dividend >= divisor: 
                curr_divisor, num_divisors = divisor, 1 
                while dividend >= curr_divisor: 
                    dividend -= curr_divisor 
                    res += num_divisors 
                    curr_divisor = curr_divisor << 1 
                    num_divisors = num_divisors << 1 
                    
        if not positive: 
            res = -res 
            
        return min(max(-2147483648, res), 2147483647) 
        