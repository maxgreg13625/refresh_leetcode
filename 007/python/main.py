class Solution:
    def reverse(self, x: int) -> int:
        if x < 10 and x > -10:
            return x

        temp_x, is_negative = 0, False
        if x < 0:
            x, is_negative = x * -1, True

        # solution 1: reverse by iterating each digit
        while x != 0:
            temp_x = temp_x * 10 + x % 10
            x = x // 10
        ## solution 2: reverse by str
        #temp_x = int(str(x)[::-1])
        #temp_x = temp_x * -1 if is_negative else temp_x
        # return 0 when outside the signed 32-bit integer range 
        return 0 if temp_x < -2147483648 or temp_x > 2147483647 else temp_x

def main():
    test = Solution()
    assert test.reverse(0) == 0
    assert test.reverse(321) == 123
    assert test.reverse(-123) == -321
    assert test.reverse(120) == 21
    assert test.reverse(1534236469) == 0

if __name__ == '__main__':
    main()