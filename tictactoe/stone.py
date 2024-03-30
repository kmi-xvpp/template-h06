from enum import Enum


class Stone(Enum):
    """Represents stones for TicTacToe game."""

    # more information about Enum avaliable here
    # https://docs.python.org/3/library/enum.html

    X = "X"
    O = "O"

    def __str__(self):
        return self.value
