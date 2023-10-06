#!/usr/bin/env python3

from menu.menu_helpers import clear_screen, exit_program
from utils.seed import seed_database
from utils.debug import reset_database
from rich import print
from ascii_titles import *


def main_menu():
    clear_screen()
    print(f"[bold dark_turquoise]{TITLE}")
    while True:
        main_menu_options()
        choice = input("--> ")
        if (choice == "0"):
            exit_program()
        elif (choice == "1"):
            language_menu()
        elif (choice == "2"):
            package_menu()
        elif (choice == "3"):
            developer_menu()
        else:
            print(f"[bold dark_turquoise]{TITLE}")
            print(":white_exclamation_mark:",
                  "[red blink][bold]Error:[/bold] Invalid option, try again.")


def language_menu():
    clear_screen()
    print(f"[bold dark_turquoise]{LANGUAGE}")
    while True:
        language_menu_options()
        choice = input("--> ")
        if (choice == "0"):
            main_menu()
        elif (choice == "1"):
            pass
        elif (choice == "2"):
            pass
        elif (choice == "3"):
            pass
        else:
            print(f"[bold dark_turquoise]{LANGUAGE}")
            print(":white_exclamation_mark:",
                  "[red blink][bold]Error:[/bold] Invalid option, try again.")


def package_menu():
    clear_screen()
    print(f"[bold dark_turquoise]{PACKAGE}")
    while True:
        package_menu_options()
        choice = input("--> ")
        if (choice == "0"):
            main_menu()
        elif (choice == "1"):
            pass
        elif (choice == "2"):
            pass
        elif (choice == "3"):
            pass
        else:
            print(f"[bold dark_turquoise]{PACKAGE}")
            print(":white_exclamation_mark:",
                  "[red blink][bold]Error:[/bold] Invalid option, try again.")


def developer_menu():
    clear_screen()
    print(f"[bold dark_turquoise]{DEVELOPER}")
    while True:
        developer_menu_options()
        choice = input("--> ")
        if (choice == "0"):
            main_menu()
        elif (choice == "1"):
            seed_database()
        elif (choice == "2"):
            reset_database()
        else:
            print(f"[bold dark_turquoise]{DEVELOPER}")
            print(":white_exclamation_mark:",
                  "[red blink][bold]Error:[/bold] Invalid option, try again.")


def main_menu_options():
    print('[bold][grey53]0:[/bold][/grey53][dark_turquoise]Exit the program', ':stop_sign:')
    print('[bold][grey53]1:[/bold][/grey53][dark_turquoise]Access Languages DB', ':robot:')
    print('[bold][grey53]2:[/bold][/grey53][dark_turquoise]Access Packages DB', ':robot:')
    print('[bold][grey53]3:[/bold][/grey53][dark_turquoise]Developer Tools', ':robot:')


def language_menu_options():
    print('[bold][grey53]0:[/bold][/grey53][dark_turquoise]Back to main menu',
          ':right_arrow_curving_left:')
    print('[bold][grey53]1:[/bold][/grey53][dark_turquoise]List all Languages', ':robot:')
    print('[bold][grey53]2:[/bold][/grey53][dark_turquoise]Find Language by name', ':robot:')
    print('[bold][grey53]3:[/bold][/grey53][dark_turquoise]Find Language by ID', ':robot:')
    print('[bold][grey53]4:[/bold][/grey53][dark_turquoise]Create Language', ':robot:')
    print('[bold][grey53]5:[/bold][/grey53][dark_turquoise]Update Language', ':robot:')
    print('[bold][grey53]6:[/bold][/grey53][dark_turquoise]Delete Language', ':robot:')


def package_menu_options():
    print('[bold][grey53]0:[/bold][/grey53][dark_turquoise]Back to main menu',
          ':right_arrow_curving_left:')
    print('[bold][grey53]1:[/bold][/grey53][dark_turquoise]List all Packages', ':robot:')
    print('[bold][grey53]2:[/bold][/grey53][dark_turquoise]Find Package by name', ':robot:')
    print('[bold][grey53]3:[/bold][/grey53][dark_turquoise]Find Package by ID', ':robot:')
    print('[bold][grey53]4:[/bold][/grey53][dark_turquoise]Create Package', ':robot:')
    print('[bold][grey53]5:[/bold][/grey53][dark_turquoise]Update Package', ':robot:')
    print('[bold][grey53]6:[/bold][/grey53][dark_turquoise]Delete Package', ':robot:')
    print('[bold][grey53]7:[/bold][/grey53][dark_turquoise]List all Packages in a Language', ':robot:')


def developer_menu_options():
    print('[bold][grey53]0:[/bold][/grey53][dark_turquoise]Back to main menu',
          ':right_arrow_curving_left:')
    print('[bold][grey53]1:[/bold][/grey53][dark_turquoise]Seed the DB', ':robot:')
    print('[bold][grey53]2:[/bold][/grey53][dark_turquoise]Reset and Debug the DB', ':robot:')


if __name__ == "__main__":
    main_menu()
