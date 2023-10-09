from ascii_titles import PACKAGE_CREATE
from rich import print
from menu_helpers.menu_utils import clear_screen
from menu_helpers.packages_menu_helpers import create_new_package
import menus.package_menus.packages_language_create_menu
import menus.package_menus.packages_main_menu


def packages_confirm_create_menu(new_package_name, new_package_command, new_package_language_name, new_package_language_id):
    clear_screen()
    print(f"[bold][dark_turquoise]{PACKAGE_CREATE}")
    while True:
        packages_confirm_create_menu_options(
            new_package_name, new_package_command, new_package_language_name)
        choice = input("Y/N :> ")
        if (choice.lower() == "n"):
            menus.package_menus.packages_language_create_menu.packages_language_create_menu(
                new_package_name, new_package_command)
        elif (choice.lower() == 'y'):
            create_new_package(
                new_package_name, new_package_command, new_package_language_id)
        else:
            clear_screen()
            print(f"[bold dark_turquoise]{PACKAGE_CREATE}")
            print(":white_exclamation_mark:",
                  "[red blink][bold]Error:[/bold] Invalid option, try again.")


def packages_confirm_create_menu_options(new_package_name, new_package_command, new_package_language_name):
    print("[dark_turquoise]*[/dark_turquoise][grey53]*[/grey53][dark_turquoise]*[/dark_turquoise][grey53]*[/grey53][dark_turquoise]*[/dark_turquoise][grey53]*[/grey53][dark_turquoise]*[/dark_turquoise][grey53]*[/grey53][dark_turquoise]*[/dark_turquoise][grey53]*[/grey53][dark_turquoise]*[/dark_turquoise][grey53]*[/grey53][dark_turquoise]*[/dark_turquoise][grey53]*[/grey53][dark_turquoise]*[/dark_turquoise][grey53]*[/grey53][dark_turquoise]*[/dark_turquoise][grey53]*[/grey53][dark_turquoise]*[/dark_turquoise][grey53]*[/grey53][dark_turquoise]*[/dark_turquoise][grey53]*[/grey53][dark_turquoise]*[/dark_turquoise][grey53]*[/grey53][dark_turquoise]*[/dark_turquoise][grey53]*[/grey53][dark_turquoise]*[/dark_turquoise][grey53]*[/grey53]")
    print(
        f"[magenta]*[/magenta]  [dark_turquoise]Name: [/dark_turquoise][grey53]{new_package_name if new_package_name != '' else 'None'}")
    print(
        f"[magenta]*[/magenta]  [dark_turquoise]Command: [/dark_turquoise][grey53]{new_package_command if new_package_command != '' else 'None'}")
    print(
        f"[magenta]*[/magenta]  [dark_turquoise]Language: [/dark_turquoise][grey53]{new_package_language_name if new_package_language_name != '' else 'None'}")
    print("[dark_turquoise]*[/dark_turquoise][grey53]*[/grey53][dark_turquoise]*[/dark_turquoise][grey53]*[/grey53][dark_turquoise]*[/dark_turquoise][grey53]*[/grey53][dark_turquoise]*[/dark_turquoise][grey53]*[/grey53][dark_turquoise]*[/dark_turquoise][grey53]*[/grey53][dark_turquoise]*[/dark_turquoise][grey53]*[/grey53][dark_turquoise]*[/dark_turquoise][grey53]*[/grey53][dark_turquoise]*[/dark_turquoise][grey53]*[/grey53][dark_turquoise]*[/dark_turquoise][grey53]*[/grey53][dark_turquoise]*[/dark_turquoise][grey53]*[/grey53][dark_turquoise]*[/dark_turquoise][grey53]*[/grey53][dark_turquoise]*[/dark_turquoise][grey53]*[/grey53][dark_turquoise]*[/dark_turquoise][grey53]*[/grey53][dark_turquoise]*[/dark_turquoise][grey53]*[/grey53]")
    print("[grey53]*[/grey53]")
    print(
        '[dark_turquoise]*[/dark_turquoise]  [bold][dark_turquoise]Y/N[/bold][/dark_turquoise][grey53] is this correct?', ':floppy_disk:')
    print("[grey53]*[/grey53]")
    print("[dark_turquoise]*[/dark_turquoise][grey53]*[/grey53][dark_turquoise]*[/dark_turquoise][grey53]*[/grey53][dark_turquoise]*[/dark_turquoise][grey53]*[/grey53][dark_turquoise]*[/dark_turquoise][grey53]*[/grey53][dark_turquoise]*[/dark_turquoise][grey53]*[/grey53][dark_turquoise]*[/dark_turquoise][grey53]*[/grey53][dark_turquoise]*[/dark_turquoise][grey53]*[/grey53][dark_turquoise]*[/dark_turquoise][grey53]*[/grey53][dark_turquoise]*[/dark_turquoise][grey53]*[/grey53][dark_turquoise]*[/dark_turquoise][grey53]*[/grey53][dark_turquoise]*[/dark_turquoise][grey53]*[/grey53][dark_turquoise]*[/dark_turquoise][grey53]*[/grey53][dark_turquoise]*[/dark_turquoise][grey53]*[/grey53][dark_turquoise]*[/dark_turquoise][grey53]*[/grey53]")
