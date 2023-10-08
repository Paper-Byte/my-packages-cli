from ascii_titles import PACKAGE_CREATE
from rich import print
from menu_helpers.menu_utils import clear_screen
import menus.package_menus.packages_name_create_menu
import menus.package_menus.packages_language_create_menu


def packages_command_create_menu(new_package_name):
    new_package_command = ""
    new_package_language_name = ""
    clear_screen()
    print(f"[bold][dark_turquoise]{PACKAGE_CREATE}")
    while True:
        packages_command_create_menu_options(
            new_package_name, new_package_command, new_package_language_name)
        choice = input("npm install :> ")
        if ((choice.lower() == "b") or (choice.lower() == "back")):
            menus.package_menus.packages_name_create_menu.packages_name_create_menu()
        elif (not choice.isnumeric()):
            if (len(choice) <= 50):
                choice = 'npm install ' + choice
                new_package_command = choice
                menus.package_menus.packages_language_create_menu.packages_language_create_menu(
                    new_package_name, new_package_command)
            else:
                clear_screen()
                print(f"[bold dark_turquoise]{PACKAGE_CREATE}")
                print(":white_exclamation_mark:",
                      "[red blink][bold]Error:[/bold] Invalid command, try again.")
        else:
            clear_screen()
            print(f"[bold dark_turquoise]{PACKAGE_CREATE}")
            print(":white_exclamation_mark:",
                  "[red blink][bold]Error:[/bold] Invalid command, try again.")


def packages_command_create_menu_options(new_package_name, new_package_command, new_package_language_name):
    print("[dark_turquoise]*[/dark_turquoise][grey53]*[/grey53][dark_turquoise]*[/dark_turquoise][grey53]*[/grey53][dark_turquoise]*[/dark_turquoise][grey53]*[/grey53][dark_turquoise]*[/dark_turquoise][grey53]*[/grey53][dark_turquoise]*[/dark_turquoise][grey53]*[/grey53][dark_turquoise]*[/dark_turquoise][grey53]*[/grey53][dark_turquoise]*[/dark_turquoise][grey53]*[/grey53][dark_turquoise]*[/dark_turquoise][grey53]*[/grey53][dark_turquoise]*[/dark_turquoise][grey53]*[/grey53][dark_turquoise]*[/dark_turquoise][grey53]*[/grey53][dark_turquoise]*[/dark_turquoise][grey53]*[/grey53][dark_turquoise]*[/dark_turquoise][grey53]*[/grey53][dark_turquoise]*[/dark_turquoise][grey53]*[/grey53][dark_turquoise]*[/dark_turquoise][grey53]*[/grey53]")
    print(
        f"[magenta]*[/magenta]  [dark_turquoise]Name: [/dark_turquoise][grey53]{new_package_name if new_package_name != '' else 'None'}")
    print(
        f"[magenta]*[/magenta]  [dark_turquoise]Command: [/dark_turquoise][grey53]{new_package_command if new_package_command != '' else 'None'}")
    print(
        f"[magenta]*[/magenta]  [dark_turquoise]Language: [/dark_turquoise][grey53]{new_package_language_name if new_package_language_name != '' else 'None'}")
    print("[dark_turquoise]*[/dark_turquoise][grey53]*[/grey53][dark_turquoise]*[/dark_turquoise][grey53]*[/grey53][dark_turquoise]*[/dark_turquoise][grey53]*[/grey53][dark_turquoise]*[/dark_turquoise][grey53]*[/grey53][dark_turquoise]*[/dark_turquoise][grey53]*[/grey53][dark_turquoise]*[/dark_turquoise][grey53]*[/grey53][dark_turquoise]*[/dark_turquoise][grey53]*[/grey53][dark_turquoise]*[/dark_turquoise][grey53]*[/grey53][dark_turquoise]*[/dark_turquoise][grey53]*[/grey53][dark_turquoise]*[/dark_turquoise][grey53]*[/grey53][dark_turquoise]*[/dark_turquoise][grey53]*[/grey53][dark_turquoise]*[/dark_turquoise][grey53]*[/grey53][dark_turquoise]*[/dark_turquoise][grey53]*[/grey53][dark_turquoise]*[/dark_turquoise][grey53]*[/grey53]")
    print("[grey53]*[/grey53]")
    print('[dark_turquoise]*[/dark_turquoise]  [bold][dark_turquoise]"back" [magenta][italic]OR[/italic][/magenta] "b"[/bold][/dark_turquoise][grey53] to return to the previous menu',
          ':right_arrow_curving_left:')
    print(
        '[grey53]*[/grey53]  [bold][dark_turquoise]INPUT[/bold][/dark_turquoise][grey53] to set the package command [italic]*max 20 chars / min 1 char*[/italic]', ':robot:')
    print("[dark_turquoise]*[/dark_turquoise]")
    print("[grey53]*[/grey53][dark_turquoise]*[/dark_turquoise][grey53]*[/grey53][dark_turquoise]*[/dark_turquoise][grey53]*[/grey53][dark_turquoise]*[/dark_turquoise][grey53]*[/grey53][dark_turquoise]*[/dark_turquoise][grey53]*[/grey53][dark_turquoise]*[/dark_turquoise][grey53]*[/grey53][dark_turquoise]*[/dark_turquoise][grey53]*[/grey53][dark_turquoise]*[/dark_turquoise][grey53]*[/grey53][dark_turquoise]*[/dark_turquoise][grey53]*[/grey53][dark_turquoise]*[/dark_turquoise][grey53]*[/grey53][dark_turquoise]*[/dark_turquoise][grey53]*[/grey53][dark_turquoise]*[/dark_turquoise][grey53]*[/grey53][dark_turquoise]*[/dark_turquoise][grey53]*[/grey53][dark_turquoise]*[/dark_turquoise][grey53]*[/grey53][dark_turquoise]*[/dark_turquoise]")
