import os, sys
from enum import Enum


class Score(Enum):
    LOSS = 0
    DRAW = 3
    WIN = 6


class Rochambeau(Enum):
    ROCK = 1
    PAPER = 2
    SCISSOR = 3

    @staticmethod
    def get_winning_hand(hand):
        if hand == Rochambeau.ROCK:
            return Rochambeau.PAPER
        elif hand == Rochambeau.PAPER:
            return Rochambeau.SCISSOR
        else:
            return Rochambeau.ROCK

    @staticmethod
    def get_draw_hand(elf_hand):
        return elf_hand

    @staticmethod
    def get_losing_hand(elf_hand):
        if elf_hand == Rochambeau.ROCK:
            return Rochambeau.SCISSOR
        elif elf_hand == Rochambeau.PAPER:
            return Rochambeau.ROCK
        else:
            return Rochambeau.PAPER

    @staticmethod
    def get_hand_by_strategy(strat, elf_hand):
        if strat == 'X':
            return Rochambeau.get_losing_hand(elf_hand)
        elif strat == 'Y':
            return Rochambeau.get_draw_hand(elf_hand)
        else:
            return Rochambeau.get_winning_hand(elf_hand)


MAP_ELF = {Rochambeau.ROCK: 'A', Rochambeau.PAPER: 'B', Rochambeau.SCISSOR: 'C'}
MAP_STR = {Score.LOSS: 'X', Score.DRAW: 'Y', Score.WIN: 'Z'}
REV_MAP_ELF = {v: k for k, v in MAP_ELF.items()}
REV_MAP_STR = {v: k for k, v in MAP_STR.items()}


if __name__ == "__main__":
    total = 0

    # read file
    with open("input2.txt", 'r') as f:
        lines = f.readlines()
        
        for line in lines:
            line = line.strip()
            elf, win_lose = line.split()

            total += REV_MAP_STR[win_lose].value
            total += Rochambeau.get_hand_by_strategy(win_lose, REV_MAP_ELF[elf]).value

    print( total )

