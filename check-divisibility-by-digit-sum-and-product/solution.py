class Solution:
    def checkDivisibility(self, n: int) -> bool:
        total_sum = 0
        total_product = 1
        temp = n
        while temp > 0:
            d = temp % 10
            total_sum += d
            total_product *= d
            temp //= 10
        return n % (total_sum + total_product) == 0
