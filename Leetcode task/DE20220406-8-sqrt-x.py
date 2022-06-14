class Solution:
    def mySqrt(self, x: int) -> int:

        if x <= 1:
            return x

        # left, right = 0, x//2
        #
        # while left <= right:
        #     mid = (left + right) // 2
        #     tmpVal = mid*mid
        #
        #     if tmpVal == x:
        #         return mid
        #     elif tmpVal < x:
        #         left = mid + 1
        #     else:
        #         right = mid - 1
        #
        # return right

        left, right = 1, x

        while left <= right:
            mid = (left + right) // 2

            if mid * mid <= x < (mid + 1) * (mid + 1):
                return mid
            elif x > mid * mid:
                left = mid
            else:
                right = mid
