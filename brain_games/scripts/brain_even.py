#!/usr/bin/env python3
from brain_games.games.cli import welcome_user
from brain_games.games.even import even_games


def main():
    print('Welcome to the Brain Games!')
    name = welcome_user()
    even_games(name)


if __name__ == "__main__":
    main()
