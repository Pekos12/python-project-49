#!/usr/bin/env python3
from brain_games.games.calc import welcome_user
from brain_games.games.calc import calc_games


def main():
    print('Welcome to the Brain Games!')
    welcome_user()
    calc_games()


if __name__ == "__main__":
    main()
