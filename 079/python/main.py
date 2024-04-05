from typing import List

class Solution:
    def check_element(self, i: int, j: int, w_idx: int) -> bool:
        if i < 0 or j < 0 or i >= self.height or j >= self.width:
            return False

        if self.board[i][j] != self.word[w_idx]:
            return False
        elif self.board[i][j] == self.word[w_idx] and w_idx == self.length:
            return True
        else:
            w_idx += 1
            
            # check top, down, left, and right 
            return self.check_element(i-1, j, w_idx) or\
                self.check_element(i+1, j, w_idx) or\
                self.check_element(i, j-1, w_idx) or\
                self.check_element(i, j+1, w_idx)

    def exist(self, board: List[List[str]], word: str) -> bool:
        self.board, self.word = board, word
        self.height, self.width, self.length = len(board), len(board[0]), len(word)

        word_idx = 0
        for i in range(self.height):
            for j in range(self.width):
                if self.check_element(i, j, word_idx):
                    return True
        return False

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