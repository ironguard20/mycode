#!/usr/bin/env python3
"""
Author: Robert Spring

This program randomly selects two pokemon from the pokemon API 
and allows a player to do battle with the infamous Gary.
"""

from pokefunc import pokebattler, input_filter, poke_picker


def main():
    PokeA = poke_picker()
    PokeB = poke_picker()
    name = input_filter("Trainer, state your name: ")
    pokebattler(name, PokeA, PokeB)


if __name__ == "__main__":
    main()

