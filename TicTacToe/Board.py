class Board:
    def __init__(self, size):
        self.reset(size)

    # Resets board to initial state
    def reset(self, size):
        self.board = [["" for _ in range(size)] for _ in range(size)]
        self.row_counts = [{"X": 0, "O": 0} for _ in range(size)]
        self.col_counts = [{"X": 0, "O": 0} for _ in range(size)]
        self.diag_counts = [{"X": 0, "O": 0} for _ in range(2)]
        self.size = size

    # Places a marker from a given player at a location on board
    # returns True if this was a winning move else False
    def place(self, player, r, c):
        marker = player.marker
        if self.board[r][c] != '':
            raise ValueError

        else:
            self.board[r][c] = marker

            self.row_counts[r][marker] += 1
            if self.row_counts[r][marker] == self.size:
                return True

            self.col_counts[c][marker] += 1
            if self.col_counts[c][marker] == self.size:
                return True

            if r == c:
                self.diag_counts[0][marker] += 1
                if self.diag_counts[0][marker] == self.size:
                    return True

            if r + c == self.size - 1:
                self.diag_counts[1][marker] += 1
                if self.diag_counts[1][marker] == self.size:
                    return True

            return False

