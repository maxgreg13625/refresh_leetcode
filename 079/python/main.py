from typing import List

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        pass

def main():
    board = [["A", "B", "C", "E"],
             ["S", "F", "C", "S"],
             ["A", "D", "E", "E"]]
    test = Solution()
    assert test.exist(board, "ABCCED") == True
    assert test.exist(board, "SEE") == True
    assert test.exist(board, "ABCB") == False

if __name__ == '__main__':
    main()