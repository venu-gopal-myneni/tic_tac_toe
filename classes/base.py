import warnings
from pprint import pprint as print


class Board:
    player_0 = 0
    player_1 = 1

    def __init__(self) -> None:
        self.state = [[None, None, None], [None, None, None], [None, None, None]]
        self._marks = 0

    @property
    def marks(self):
        return self._marks

    @marks.setter
    def marks(self, value):
        self._marks = value

    def mark(self, player_id, x, y):
        if x > 2 or y > 2:
            warnings.warn(f"X i.e. {x} and Y i.e {y} should be <= 2")
            return False
        if self.state[x][y] is None:
            self.state[x][y] = player_id
            self.marks = self.marks + 1
            return True
        else:
            warnings.warn(f"X i.e. {x} and Y i.e. {y} is already occupied")
            return False

    def has_ended(self):
        for row in range(0, 3):
            if (self.state[row][0] == self.state[row][1] == self.state[row][2]) and (
                self.state[row][0] is not None
            ):
                return (True, self.state[row][0])

        for col in range(0, 3):
            if (self.state[0][col] == self.state[1][col] == self.state[2][col]) and (
                self.state[0][col] is not None
            ):
                return (True, self.state[0][col])

        if (
            self.state[0][0] == self.state[1][1] == self.state[2][2]
            and self.state[0][0] is not None
        ):
            return (True, self.state[0][0])

        if (
            self.state[0][2] == self.state[1][1] == self.state[2][2]
            and self.state[2][0] is not None
        ):
            return (True, self.state[1][1])

        if self.marks == 9:
            return (True, None)

        return (False, None)

    def print(self) -> str:
        print("***********")
        for row in self.state:
            c = ["_" if ele is None else f"{ele}" for ele in row]
            c = ",".join(c)
            print(c)


class Player:
    pass


if __name__ == "__main__":
    board = Board()
    board.mark(0, 1, 3)
    board.mark(1, 1, 1)
    board.mark(1, 1, 1)
    print(board.has_ended())
