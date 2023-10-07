from models.package import Package
from models.language import Language
from rich import print
from menu_helpers.menu_utils import clear_screen
import menus.package_menus.packages_main_menu  # packages_main_menu()
import pyfiglet


def packages_sub_menu(package):

    PACKAGE_TITLE = pyfiglet.figlet_format((f'{package.name}'), font='mini')
    PACKAGE_OWNER = Language.find_by_id(package.language_id)

    clear_screen()
    print(f"[bold dark_turquoise]{PACKAGE_TITLE}")
    while True:
        packages_crud_menu_options(package, PACKAGE_OWNER)
        choice = input("--> ")
        if ((choice.lower() == "b") or (choice.lower() == "back")):
            menus.package_menus.packages_main_menu.packages_main_menu()
        elif ((choice.lower() == "n") or (choice.lower() == "name")):
            pass
        elif ((choice.lower() == "c") or (choice.lower() == "com")):
            pass
        elif ((choice.lower() == "l") or (choice.lower() == "lan")):
            pass
        elif ((choice.lower() == "d") or (choice.lower() == "del")):
            print(":white_exclamation_mark:", "[red blink] Are you sure? Y/N")
            if (choice.lower() == 'y'):
                pass
            elif (choice.lower() == 'n'):
                packages_sub_menu(package)
            else:
                print(":white_exclamation_mark:",
                      "[red blink][bold]Error:[/bold] Invalid option, try again.")
        else:
            print(f"[bold dark_turquoise]{PACKAGE_TITLE}")
            print(":white_exclamation_mark:",
                  "[red blink][bold]Error:[/bold] Invalid option, try again.")


def packages_crud_menu_options(package, PACKAGE_OWNER):
    print("[dark_turquoise]*[/dark_turquoise][grey53]*[/grey53][dark_turquoise]*[/dark_turquoise][grey53]*[/grey53][dark_turquoise]*[/dark_turquoise][grey53]*[/grey53][dark_turquoise]*[/dark_turquoise][grey53]*[/grey53][dark_turquoise]*[/dark_turquoise][grey53]*[/grey53][dark_turquoise]*[/dark_turquoise][grey53]*[/grey53][dark_turquoise]*[/dark_turquoise][grey53]*[/grey53][dark_turquoise]*[/dark_turquoise][grey53]*[/grey53][dark_turquoise]*[/dark_turquoise][grey53]*[/grey53][dark_turquoise]*[/dark_turquoise][grey53]*[/grey53][dark_turquoise]*[/dark_turquoise][grey53]*[/grey53][dark_turquoise]*[/dark_turquoise][grey53]*[/grey53][dark_turquoise]*[/dark_turquoise][grey53]*[/grey53][dark_turquoise]*[/dark_turquoise][grey53]*[/grey53]")
    print(
        f"[magenta]*[/magenta]  [grey53]Name: [/grey53][dark_turquoise]{package.name}")
    print(
        f"[magenta]*[/magenta]  [grey53]Command: [/grey53][dark_turquoise]{package.command}")
    print(
        f"[magenta]*[/magenta]  [grey53]Language: [/grey53][dark_turquoise]{PACKAGE_OWNER.name}")
    print("[dark_turquoise]*[/dark_turquoise][grey53]*[/grey53][dark_turquoise]*[/dark_turquoise][grey53]*[/grey53][dark_turquoise]*[/dark_turquoise][grey53]*[/grey53][dark_turquoise]*[/dark_turquoise][grey53]*[/grey53][dark_turquoise]*[/dark_turquoise][grey53]*[/grey53][dark_turquoise]*[/dark_turquoise][grey53]*[/grey53][dark_turquoise]*[/dark_turquoise][grey53]*[/grey53][dark_turquoise]*[/dark_turquoise][grey53]*[/grey53][dark_turquoise]*[/dark_turquoise][grey53]*[/grey53][dark_turquoise]*[/dark_turquoise][grey53]*[/grey53][dark_turquoise]*[/dark_turquoise][grey53]*[/grey53][dark_turquoise]*[/dark_turquoise][grey53]*[/grey53][dark_turquoise]*[/dark_turquoise][grey53]*[/grey53][dark_turquoise]*[/dark_turquoise][grey53]*[/grey53]")
    print("[grey53]*[/grey53]")
    print('[dark_turquoise]*[/dark_turquoise]  [bold][dark_turquoise]"back" [magenta][italic]OR[/italic][/magenta] "b"[/bold][/dark_turquoise][grey53] to return to the previous menu',
          ':right_arrow_curving_left:')
    print(
        '[grey53]*[/grey53]  [bold][dark_turquoise]"name" [magenta][italic]OR[/italic][/magenta] "n"[/bold][/dark_turquoise][grey53] to update package name', ':robot:')
    print(
        '[dark_turquoise]*[/dark_turquoise]  [bold][dark_turquoise]"com" [magenta][italic]OR[/italic][/magenta] "c"[/bold][/dark_turquoise][grey53] to update a package command', ':robot:')
    print(
        '[grey53]*[/grey53]  [bold][dark_turquoise]"lan" [magenta][italic]OR[/italic][/magenta] "l"[/bold][/dark_turquoise][grey53] to change a package language', ':robot:')
    print(
        '[dark_turquoise]*[/dark_turquoise]  [bold][dark_turquoise]"del" [magenta][italic]OR[/italic][/magenta] "d"[/bold][/dark_turquoise][grey53] to delete the package', ':robot:')
    print("[grey53]*[/grey53]")
    print("[dark_turquoise]*[/dark_turquoise][grey53]*[/grey53][dark_turquoise]*[/dark_turquoise][grey53]*[/grey53][dark_turquoise]*[/dark_turquoise][grey53]*[/grey53][dark_turquoise]*[/dark_turquoise][grey53]*[/grey53][dark_turquoise]*[/dark_turquoise][grey53]*[/grey53][dark_turquoise]*[/dark_turquoise][grey53]*[/grey53][dark_turquoise]*[/dark_turquoise][grey53]*[/grey53][dark_turquoise]*[/dark_turquoise][grey53]*[/grey53][dark_turquoise]*[/dark_turquoise][grey53]*[/grey53][dark_turquoise]*[/dark_turquoise][grey53]*[/grey53][dark_turquoise]*[/dark_turquoise][grey53]*[/grey53][dark_turquoise]*[/dark_turquoise][grey53]*[/grey53][dark_turquoise]*[/dark_turquoise][grey53]*[/grey53][dark_turquoise]*[/dark_turquoise][grey53]*[/grey53]")
