import re

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        match_result = re.search(needle, haystack)
        return match_result.start() if match_result else -1 

def main():
    test = Solution()
    assert test.strStr('sadbutsad', 'sad') == 0
    assert test.strStr('leetcode', 'leeto') == -1

if __name__ == '__main__':
    main()