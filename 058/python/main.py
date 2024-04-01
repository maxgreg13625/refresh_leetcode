class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        str_list = s.split()
        return len(str_list[-1])

def main():
    test = Solution()
    assert test.lengthOfLastWord('Hello World') == 5
    assert test.lengthOfLastWord('   fly me   to   the moon  ') == 4
    assert test.lengthOfLastWord('luffy is still joyboy') == 6

if __name__ == '__main__':
    main()