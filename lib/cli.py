#!/usr/bin/env python3

from menu_helpers.menu_utils import clear_screen, exit_program
import menus.main_menu  # main_menu()
from utils.seed import seed_database
from utils.debug import reset_database
from rich import print
from ascii_titles import *

# global directory VARIABLE --> /Development/
#


def package_menu():
    clear_screen()
    print(f"[bold dark_turquoise]{PACKAGE}")
    while True:
        package_menu_options()
        choice = input("--> ")
        if (choice == "0"):
            main_menu()
        elif (choice == "1"):
            list_packages()
        elif (choice == "2"):
            find_package_by_name()
        elif (choice == "3"):
            find_package_by_id()
        elif (choice == "4"):
            create_package()
        elif (choice == "5"):
            update_package()
        elif (choice == "6"):
            delete_package()
        elif (choice == "7"):
            list_language_packages()
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
    menus.main_menu.main_menu()
