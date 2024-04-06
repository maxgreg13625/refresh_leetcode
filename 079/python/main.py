from typing import List

class Solution:
    def check_element(self, i: int, j: int, w_idx: int) -> bool:
        # over boundary
        if i < 0 or j < 0 or i >= self.height or j >= self.width:
            return False
        # if char not match, then back to prev
        if self.board[i][j] != self.word[w_idx]:
            return False
        # if char match, then continue comparsion
        w_idx += 1
        if w_idx == len(self.word):
            return True
        # replace original char to avoid back to current path
        temp, self.board[i][j] = self.board[i][j], ''
        # check board top, down, left, and right
        if self.check_element(i-1, j, w_idx) or\
                self.check_element(i+1, j, w_idx) or\
                self.check_element(i, j-1, w_idx) or\
                self.check_element(i, j+1, w_idx):
            return True
        else:
            self.board[i][j] = temp
            return False

    def exist(self, board: List[List[str]], word: str) -> bool:
        self.board, self.word = board, word
        self.height, self.width, self.length = len(board), len(board[0]), len(word)

        # if the word length large than board size, return False directly
        if self.height * self.width < self.length:
            return False
 
        for i in range(self.height):
            for j in range(self.width):
                if self.check_element(i, j, 0):
                    return True
        return False

def main():
    test = Solution()
    # case 1
    board = [["A", "B", "C", "E"],
             ["S", "F", "C", "S"],
             ["A", "D", "E", "E"]]
    assert test.exist(board, "ABCCED") == True
    # case 2
    board = [["A", "B", "C", "E"],
             ["S", "F", "C", "S"],
             ["A", "D", "E", "E"]]
    assert test.exist(board, "SEE") == True
    # case 3
    board = [["A", "B", "C", "E"],
             ["S", "F", "C", "S"],
             ["A", "D", "E", "E"]]
    assert test.exist(board, "ABCB") == False
    # case 4
    board = [["a", "a", "a", "a"],
             ["a", "a", "a", "a"],
             ["a", "a", "a", "a"]]
    assert test.exist(board, "aaaaaaaaaaaaa") == False
    # case 5
    board = [["A", "A"],
             ["A", "a"],
             ["A", "a"],
             ["a", "a"],
             ["a", "A"]]
    assert test.exist(board, "AaaaaAaAA") == False
if __name__ == '__main__':
    main()