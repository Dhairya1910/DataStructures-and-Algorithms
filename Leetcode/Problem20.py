def myfunc(divisor , dividend): 
    if divisor == dividend:
        return 0 
    quotient = 0
    neg = False
    if divisor < 0 :
        neg = True 
        divisor = abs(divisor)
    while dividend > divisor:
        dividend = dividend - divisor 
        quotient = quotient + 1 
    if neg:
        return -(quotient)
    return quotient


print(myfunc(-3,10))

class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        sign = -1 if (dividend >= 0 and divisor < 0) or (dividend < 0 and divisor >= 0) else 1
        dividend = abs(dividend)
        divisor = abs(divisor)
        result = len(range(0, dividend-divisor+1, divisor))
        if sign == -1:
            result = -result
        minus_limit = -(2**31)
        plus_limit = (2**31 - 1)
        result = min(max(result, minus_limit), plus_limit)
        return result