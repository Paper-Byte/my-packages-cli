#!/usr/bin/env python3

from menu.menu_helpers import *
from rich import print
import pyfiglet

TITLE = pyfiglet.figlet_format('My Pack', font='block')


def main():
    while True:
        main_menu()
        choice = input(">")


def main_menu():
    print(f"[bold dark_turquoise]{TITLE}")
    print('[bold][grey53]0:[/bold][/grey53][dark_turquoise]Exit the program', ':stop_sign:')
    print('[bold][grey53]1:[/bold][/grey53][dark_turquoise]Access Languages DB', ':robot:')
    print('[bold][grey53]2:[/bold][/grey53][dark_turquoise]Access Packages DB', ':robot:')


if __name__ == "__main__":
    main()
