from models.language import Language
from rich import print
from menu_helpers.menu_utils import clear_screen
from utils.custom_progresses import new_progress
import menus.package_menus.packages_main_menu
import menus.package_menus.packages_name_menu
import menus.package_menus.packages_command_menu
import menus.package_menus.packages_language_menu
import pyfiglet
import time


def packages_sub_menu(package):

    PACKAGE_TITLE = pyfiglet.figlet_format((f'{package.name}'), font='mini')
    PACKAGE_OWNER = Language.find_by_id(package.language_id)

    clear_screen()
    print(f"[bold][dark_turquoise]{PACKAGE_TITLE}")
    while True:
        packages_crud_menu_options(package, PACKAGE_OWNER)
        choice = input("--> ")
        if ((choice.lower() == "b") or (choice.lower() == "back")):
            menus.package_menus.packages_main_menu.packages_main_menu()
        elif ((choice.lower() == "n") or (choice.lower() == "name")):
            menus.package_menus.packages_name_menu.packages_name_menu(package)
        elif ((choice.lower() == "c") or (choice.lower() == "com")):
            menus.package_menus.packages_command_menu.packages_command_menu(
                package)
        elif ((choice.lower() == "l") or (choice.lower() == "lan")):
            menus.package_menus.packages_language_menu.packages_language_menu(
                package)
        elif ((choice.lower() == "d") or (choice.lower() == "del")):
            while True:
                warning_message()
                choice = input("Y/N :> ")
                if (choice.lower() == 'y'):
                    package_del_progress = new_progress()
                    with package_del_progress:
                        delete = package_del_progress.add_task(
                            "[italic][magenta]Deleting package[/italic][magenta][dark_turqoise]...[/dark_turqoise]", total=20)
                        while not package_del_progress.finished:
                            package_del_progress.update(delete, advance=0.5)
                            time.sleep(0.02)
                    clear_screen()
                    package.delete()
                    print(
                        f"[bold][magenta]Package was deleted!")
                    time.sleep(2)
                    menus.package_menus.packages_main_menu.packages_main_menu()
                elif (choice.lower() == 'n'):
                    packages_sub_menu(package)
                else:
                    clear_screen()
                    print(":white_exclamation_mark:",
                          "[red blink][bold]Error:[/bold] Invalid package option, try again.")
        else:
            clear_screen()
            print(f"[bold dark_turquoise]{PACKAGE_TITLE}")
            print(":white_exclamation_mark:",
                  "[red blink][bold]Error:[/bold] Invalid command, try again.")


def packages_crud_menu_options(package, PACKAGE_OWNER):
    print("[dark_turquoise]*[/dark_turquoise][grey53]*[/grey53][dark_turquoise]*[/dark_turquoise][grey53]*[/grey53][dark_turquoise]*[/dark_turquoise][grey53]*[/grey53][dark_turquoise]*[/dark_turquoise][grey53]*[/grey53][dark_turquoise]*[/dark_turquoise][grey53]*[/grey53][dark_turquoise]*[/dark_turquoise][grey53]*[/grey53][dark_turquoise]*[/dark_turquoise][grey53]*[/grey53][dark_turquoise]*[/dark_turquoise][grey53]*[/grey53][dark_turquoise]*[/dark_turquoise][grey53]*[/grey53][dark_turquoise]*[/dark_turquoise][grey53]*[/grey53][dark_turquoise]*[/dark_turquoise][grey53]*[/grey53][dark_turquoise]*[/dark_turquoise][grey53]*[/grey53][dark_turquoise]*[/dark_turquoise][grey53]*[/grey53][dark_turquoise]*[/dark_turquoise][grey53]*[/grey53]")
    print(
        f"[magenta]*[/magenta]  [dark_turquoise]Name: [/dark_turquoise][grey53]{package.name}")
    print(
        f"[magenta]*[/magenta]  [dark_turquoise]Command: [/dark_turquoise][grey53]{package.command}")
    print(
        f"[magenta]*[/magenta]  [dark_turquoise]Language: [/dark_turquoise][grey53]{PACKAGE_OWNER.name}")
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


def warning_message():
    print(":white_exclamation_mark:",
          "[red blink] Are you sure? This will delete the package and all references to it! Y/N")
