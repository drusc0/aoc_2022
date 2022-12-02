import os, sys
from enum import Enum

class Score(Enum):
    LOSSS = 0
    DRAW = 3
    WIN = 6


class Rochambeau(Enum):
    ROCK = 1
    PAPER = 2
    SCISSOR = 3

    @staticmethod
    def what_beats(hand):
        if hand == Rochambeau.ROCK:
            return Rochambeau.PAPER
        elif hand == Rochambeau.PAPER:
            return Rochambeau.SCISSOR
        else:
            return Rochambeau.ROCK


MAP_ELF = {Rochambeau.ROCK: 'A', Rochambeau.PAPER: 'B', Rochambeau.SCISSOR: 'C'}
MAP_STR = {Rochambeau.ROCK: 'X', Rochambeau.PAPER: 'Y', Rochambeau.SCISSOR: 'Z'}
REV_MAP_ELF = {v: k for k, v in MAP_ELF.items()}
REV_MAP_STR = {v: k for k, v in MAP_STR.items()}

if __name__ == "__main__":
    total = 0

    # read file
    with open("input2.txt", 'r') as f:
        lines = f.readlines()
        
        for line in lines:
            line = line.strip()
            elf, mine = line.split()

            # draw possibily if both come up to the same play
            if REV_MAP_ELF[elf] == REV_MAP_STR[mine]:
                total += Score.DRAW.value
                total += REV_MAP_ELF[elf].value
            # win for my hand
            elif REV_MAP_STR[mine] == Rochambeau.what_beats(REV_MAP_ELF[elf]):
                total += Score.WIN.value
                total += REV_MAP_STR[mine].value
            else:
                total += REV_MAP_STR[mine].value

    print( total )

