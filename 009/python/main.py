class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        elif x < 10:
            return True

        ## solution 1: transform into str, then do the comparsion during the iteration to middle
        #x_str = str(x)
        #x_len, x_half_len = len(x_str), len(x_str) // 2
        #for i in range(x_half_len):
        #    if x_str[i] != x_str[x_len - i - 1]:
        #        return False
        #return True

        # solution 2: compared with reverse str directly
        return str(x) == str(x)[::-1]

def main():
    test = Solution()
    assert test.isPalindrome(121) == True
    assert test.isPalindrome(-121) == False
    assert test.isPalindrome(10) == False
    assert test.isPalindrome(1001) == True

if __name__ == '__main__':
    main()