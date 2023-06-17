#!/usr/bin/env python3
from brain_games.games.prime import welcome_user
from brain_games.games.prime import prime_games


def main():
    print('Welcome to the Brain Games!')
    welcome_user()
    prime_games()


if __name__ == "__main__":
    main()
