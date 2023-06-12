#!/usr/bin/env python3
from brain_games.games.progression import welcome_user
from brain_games.games.progression import progression_games


def main():
    print('Welcome to the Brain Games!')
    welcome_user()
    progression_games()


if __name__ == "__main__":
    main()
