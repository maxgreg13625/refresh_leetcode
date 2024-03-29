class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        location_dict = {}
        temp_length, max_length, start_idx = 0, 0, 0

        for i in range(len(s)):
            if s[i] not in location_dict or location_dict[s[i]] < start_idx:
                location_dict[s[i]] = i
                temp_length += 1
            else:
                max_length = max(max_length, temp_length)
                temp_length = i - location_dict[s[i]]
                start_idx = location_dict[s[i]] + 1
                location_dict[s[i]] = i

        max_length = max(max_length, temp_length)
        return max_length

def main():
    test = Solution()
    assert test.lengthOfLongestSubstring('abcabcbb') == 3
    assert test.lengthOfLongestSubstring('bbbbb') == 1
    assert test.lengthOfLongestSubstring('pwwkew') == 3
    assert test.lengthOfLongestSubstring('dvdf') == 3

if __name__ == '__main__':
    main()