from models.language import Language
from models.package import Package
from ascii_titles import PACKAGE_CREATE
from rich import print
from menu_helpers.menu_utils import clear_screen
from utils.custom_progresses import new_progress
import menus.package_menus.packages_main_menu
import time


def packages_name_create_menu():
    new_package_name = ""
    new_package_command = ""
    new_package_language_name = ""
    clear_screen()
    print(f"[bold][dark_turquoise]{PACKAGE_CREATE}")
    while True:
        packages_name_create_menu_options(
            new_package_name, new_package_command, new_package_language_name)
        choice = input("NAME :> ")
        if ((choice.lower() == "b") or (choice.lower() == "back")):
            menus.package_menus.packages_main_menu.packages_main_menu()
        elif (not choice.isnumeric()):
            if (len(choice) <= 20):
                new_package_name = choice
                pass
            else:
                print(f"[bold dark_turquoise]{PACKAGE_CREATE}")
                print(":white_exclamation_mark:",
                      "[red blink][bold]Error:[/bold] Invalid name, try again.")
        else:
            print(f"[bold dark_turquoise]{PACKAGE_CREATE}")
            print(":white_exclamation_mark:",
                  "[red blink][bold]Error:[/bold] Invalid command, try again.")


def packages_name_create_menu_options(new_package_name, new_package_command, new_package_language_name):
    print("[dark_turquoise]*[/dark_turquoise][grey53]*[/grey53][dark_turquoise]*[/dark_turquoise][grey53]*[/grey53][dark_turquoise]*[/dark_turquoise][grey53]*[/grey53][dark_turquoise]*[/dark_turquoise][grey53]*[/grey53][dark_turquoise]*[/dark_turquoise][grey53]*[/grey53][dark_turquoise]*[/dark_turquoise][grey53]*[/grey53][dark_turquoise]*[/dark_turquoise][grey53]*[/grey53][dark_turquoise]*[/dark_turquoise][grey53]*[/grey53][dark_turquoise]*[/dark_turquoise][grey53]*[/grey53][dark_turquoise]*[/dark_turquoise][grey53]*[/grey53][dark_turquoise]*[/dark_turquoise][grey53]*[/grey53][dark_turquoise]*[/dark_turquoise][grey53]*[/grey53][dark_turquoise]*[/dark_turquoise][grey53]*[/grey53][dark_turquoise]*[/dark_turquoise][grey53]*[/grey53]")
    print(
        f"[magenta]*[/magenta]  [grey53]Name: [/grey53][dark_turquoise]{new_package_name if new_package_name != '' else 'None'}")
    print(
        f"[magenta]*[/magenta]  [grey53]Command: [/grey53][dark_turquoise]{new_package_command if new_package_command != '' else 'None'}")
    print(
        f"[magenta]*[/magenta]  [grey53]Language: [/grey53][dark_turquoise]{new_package_language_name if new_package_language_name != '' else 'None'}")
    print("[dark_turquoise]*[/dark_turquoise][grey53]*[/grey53][dark_turquoise]*[/dark_turquoise][grey53]*[/grey53][dark_turquoise]*[/dark_turquoise][grey53]*[/grey53][dark_turquoise]*[/dark_turquoise][grey53]*[/grey53][dark_turquoise]*[/dark_turquoise][grey53]*[/grey53][dark_turquoise]*[/dark_turquoise][grey53]*[/grey53][dark_turquoise]*[/dark_turquoise][grey53]*[/grey53][dark_turquoise]*[/dark_turquoise][grey53]*[/grey53][dark_turquoise]*[/dark_turquoise][grey53]*[/grey53][dark_turquoise]*[/dark_turquoise][grey53]*[/grey53][dark_turquoise]*[/dark_turquoise][grey53]*[/grey53][dark_turquoise]*[/dark_turquoise][grey53]*[/grey53][dark_turquoise]*[/dark_turquoise][grey53]*[/grey53][dark_turquoise]*[/dark_turquoise][grey53]*[/grey53]")
    print("[grey53]*[/grey53]")
    print('[dark_turquoise]*[/dark_turquoise]  [bold][dark_turquoise]"back" [magenta][italic]OR[/italic][/magenta] "b"[/bold][/dark_turquoise][grey53] to return to the previous menu',
          ':right_arrow_curving_left:')
    print(
        '[grey53]*[/grey53]  [bold][dark_turquoise]INPUT[/bold][/dark_turquoise][grey53] to change the package name [italic]*max 20 chars / min 1 char*[/italic]', ':robot:')
    print("[dark_turquoise]*[/dark_turquoise]")
    print("[grey53]*[/grey53][dark_turquoise]*[/dark_turquoise][grey53]*[/grey53][dark_turquoise]*[/dark_turquoise][grey53]*[/grey53][dark_turquoise]*[/dark_turquoise][grey53]*[/grey53][dark_turquoise]*[/dark_turquoise][grey53]*[/grey53][dark_turquoise]*[/dark_turquoise][grey53]*[/grey53][dark_turquoise]*[/dark_turquoise][grey53]*[/grey53][dark_turquoise]*[/dark_turquoise][grey53]*[/grey53][dark_turquoise]*[/dark_turquoise][grey53]*[/grey53][dark_turquoise]*[/dark_turquoise][grey53]*[/grey53][dark_turquoise]*[/dark_turquoise][grey53]*[/grey53][dark_turquoise]*[/dark_turquoise][grey53]*[/grey53][dark_turquoise]*[/dark_turquoise][grey53]*[/grey53][dark_turquoise]*[/dark_turquoise][grey53]*[/grey53][dark_turquoise]*[/dark_turquoise]")
