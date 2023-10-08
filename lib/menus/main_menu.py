from menu_helpers.menu_utils import *  # clear_screen() , exit_program()
from ascii_titles import TITLE
import menus.language_menus.languages_main_menu  # languages_main_menu()
import menus.package_menus.packages_main_menu  # packages_main_menu()
import menus.dev_menu  # dev_menu()


def main_menu():
    clear_screen()
    print(f"[bold dark_turquoise]{TITLE}")
    while True:
        main_menu_options()
        choice = input("--> ")
        if ((choice.lower() == "exit") or (choice.lower() == "e")):
            exit_program()
        elif ((choice.lower() == "lang") or (choice.lower() == "l")):
            menus.language_menus.languages_main_menu.languages_main_menu()
        elif ((choice.lower() == "pack") or (choice.lower() == "p")):
            menus.package_menus.packages_main_menu.packages_main_menu()
        elif ((choice.lower() == "dev") or (choice.lower() == "d")):
            menus.dev_menu.dev_menu()
        else:
            clear_screen()
            print(f"[bold dark_turquoise]{TITLE}")
            print(":white_exclamation_mark:",
                  "[red blink][bold]Error:[/bold] Invalid option, try again.")


def main_menu_options():
    print("[dark_turquoise]*[/dark_turquoise][grey53]*[/grey53][dark_turquoise]*[/dark_turquoise][grey53]*[/grey53][dark_turquoise]*[/dark_turquoise][grey53]*[/grey53][dark_turquoise]*[/dark_turquoise][grey53]*[/grey53][dark_turquoise]*[/dark_turquoise][grey53]*[/grey53][dark_turquoise]*[/dark_turquoise][grey53]*[/grey53][dark_turquoise]*[/dark_turquoise][grey53]*[/grey53][dark_turquoise]*[/dark_turquoise][grey53]*[/grey53][dark_turquoise]*[/dark_turquoise][grey53]*[/grey53][dark_turquoise]*[/dark_turquoise][grey53]*[/grey53][dark_turquoise]*[/dark_turquoise][grey53]*[/grey53][dark_turquoise]*[/dark_turquoise][grey53]*[/grey53][dark_turquoise]*[/dark_turquoise][grey53]*[/grey53][dark_turquoise]*[/dark_turquoise][grey53]*[/grey53]")
    print("[grey53]*[/grey53]")
    print('[dark_turquoise]*[/dark_turquoise]  [bold][dark_turquoise]"exit" [magenta][italic]OR[/italic][/magenta] "e"[/bold][/dark_turquoise][grey53] to exit the program', ':stop_sign:')
    print('[grey53]*[/grey53]  [bold][dark_turquoise]"lang" [magenta][italic]OR[/italic][/magenta] "l"[/bold][/dark_turquoise][grey53] to view languages', ':robot:')
    print('[dark_turquoise]*[/dark_turquoise]  [bold][dark_turquoise]"pack" [magenta][italic]OR[/italic][/magenta] "p"[/bold][/dark_turquoise][grey53] to view packages', ':robot:')
    print('[grey53]*[/grey53]  [bold][dark_turquoise]"dev" [magenta][italic]OR[/italic][/magenta] "d"[/bold][/dark_turquoise][grey53] to use dev tools', ':robot:')
    print("[dark_turquoise]*[/dark_turquoise]")
    print("[grey53]*[/grey53][dark_turquoise]*[/dark_turquoise][grey53]*[/grey53][dark_turquoise]*[/dark_turquoise][grey53]*[/grey53][dark_turquoise]*[/dark_turquoise][grey53]*[/grey53][dark_turquoise]*[/dark_turquoise][grey53]*[/grey53][dark_turquoise]*[/dark_turquoise][grey53]*[/grey53][dark_turquoise]*[/dark_turquoise][grey53]*[/grey53][dark_turquoise]*[/dark_turquoise][grey53]*[/grey53][dark_turquoise]*[/dark_turquoise][grey53]*[/grey53][dark_turquoise]*[/dark_turquoise][grey53]*[/grey53][dark_turquoise]*[/dark_turquoise][grey53]*[/grey53][dark_turquoise]*[/dark_turquoise][grey53]*[/grey53][dark_turquoise]*[/dark_turquoise][grey53]*[/grey53][dark_turquoise]*[/dark_turquoise][grey53]*[/grey53][dark_turquoise]*[/dark_turquoise]")
