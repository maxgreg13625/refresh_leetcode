import re

class Solution:
    def myAtoi(self, s: str) -> int:
        # below 2 cases return 0, both violate rule 4
        #  1. start with no digit chars
        #  2. start with both positive and negative sign 
        pattern = r"^\s*([\-\+]{0,1}\d+)[^\d]*"
        result_list = re.findall(pattern, s)
        result = int(result_list[0]) if len(result_list) > 0 else 0

        if result < 0 and result < -2147483648:
            return -2147483648
        elif result > 0 and result > 2147483647:
            return 2147483647
        else:
            return result

def main():
    test = Solution()
    assert test.myAtoi('42') == 42
    assert test.myAtoi('   -42') == -42
    assert test.myAtoi('4193 with words') == 4193
    assert test.myAtoi('words and 987') == 0
    assert test.myAtoi('+1') == 1
    assert test.myAtoi('+-12') == 0

if __name__ == '__main__':
    main()