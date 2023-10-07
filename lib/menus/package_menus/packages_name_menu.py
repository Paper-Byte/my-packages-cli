from models.package import Package
from rich import print
from menu_helpers.menu_utils import clear_screen
from utils.custom_progresses import new_package_name_progress
import menus.package_menus.packages_sub_menu  # packages_sub_menu()
import pyfiglet
import time


def packages_sub_menu(package):

    PACKAGE_TITLE = pyfiglet.figlet_format((f'{package.name}'), font='mini')

    clear_screen()
    print(f"[bold dark_turquoise]{PACKAGE_TITLE}")
    while True:
        packages_name_menu_options(package)
        choice = input("--> ")
        if ((choice.lower() == "b") or (choice.lower() == "back")):
            menus.package_menus.packages_sub_menu.packages_sub_menu(package)
        else:
            if (len(choice) <= 20):
                package_name_progress = new_package_name_progress()
                with package_name_progress:
                    name = package_name_progress.add_task(
                        "[italic][magenta]Updating package's name[/italic][magenta][dark_turqoise]...[/dark_turqoise]", total=20)
                    while not package_name_progress.finished:
                        package_name_progress.update(name, advance=0.5)
                        time.sleep(0.02)
                        # put helper function here
                print(f"[bold][magenta]Package name updated to {choice}!")
                time.sleep(2)
                menus.package_menus.packages_sub_menu.packages_sub_menu(
                    package)
            else:
                print(f"[bold dark_turquoise]{PACKAGE_TITLE}")
                print(":white_exclamation_mark:",
                      "[red blink][bold]Error:[/bold] Invalid option, try again.")


def packages_name_menu_options(package):
    print("[dark_turquoise]*[/dark_turquoise][grey53]*[/grey53][dark_turquoise]*[/dark_turquoise][grey53]*[/grey53][dark_turquoise]*[/dark_turquoise][grey53]*[/grey53][dark_turquoise]*[/dark_turquoise][grey53]*[/grey53][dark_turquoise]*[/dark_turquoise][grey53]*[/grey53][dark_turquoise]*[/dark_turquoise][grey53]*[/grey53][dark_turquoise]*[/dark_turquoise][grey53]*[/grey53][dark_turquoise]*[/dark_turquoise][grey53]*[/grey53][dark_turquoise]*[/dark_turquoise][grey53]*[/grey53][dark_turquoise]*[/dark_turquoise][grey53]*[/grey53][dark_turquoise]*[/dark_turquoise][grey53]*[/grey53][dark_turquoise]*[/dark_turquoise][grey53]*[/grey53][dark_turquoise]*[/dark_turquoise][grey53]*[/grey53][dark_turquoise]*[/dark_turquoise][grey53]*[/grey53]")
    print(
        f"[magenta]*[/magenta]  [grey53]Name: [/grey53][dark_turquoise]{package.name}")
    print("[dark_turquoise]*[/dark_turquoise][grey53]*[/grey53][dark_turquoise]*[/dark_turquoise][grey53]*[/grey53][dark_turquoise]*[/dark_turquoise][grey53]*[/grey53][dark_turquoise]*[/dark_turquoise][grey53]*[/grey53][dark_turquoise]*[/dark_turquoise][grey53]*[/grey53][dark_turquoise]*[/dark_turquoise][grey53]*[/grey53][dark_turquoise]*[/dark_turquoise][grey53]*[/grey53][dark_turquoise]*[/dark_turquoise][grey53]*[/grey53][dark_turquoise]*[/dark_turquoise][grey53]*[/grey53][dark_turquoise]*[/dark_turquoise][grey53]*[/grey53][dark_turquoise]*[/dark_turquoise][grey53]*[/grey53][dark_turquoise]*[/dark_turquoise][grey53]*[/grey53][dark_turquoise]*[/dark_turquoise][grey53]*[/grey53][dark_turquoise]*[/dark_turquoise][grey53]*[/grey53]")
    print("[grey53]*[/grey53]")
    print('[dark_turquoise]*[/dark_turquoise]  [bold][dark_turquoise]"back" [magenta][italic]OR[/italic][/magenta] "b"[/bold][/dark_turquoise][grey53] to return to the previous menu',
          ':right_arrow_curving_left:')
    print(
        '[grey53]*[/grey53]  [bold][dark_turquoise]INPUT[/bold][/dark_turquoise][grey53] to change the package name [italic]*max 20 chars*[/italic]', ':robot:')
    print("[dark_turquoise]*[/dark_turquoise]")
    print("[grey53]*[/grey53][dark_turquoise]*[/dark_turquoise][grey53]*[/grey53][dark_turquoise]*[/dark_turquoise][grey53]*[/grey53][dark_turquoise]*[/dark_turquoise][grey53]*[/grey53][dark_turquoise]*[/dark_turquoise][grey53]*[/grey53][dark_turquoise]*[/dark_turquoise][grey53]*[/grey53][dark_turquoise]*[/dark_turquoise][grey53]*[/grey53][dark_turquoise]*[/dark_turquoise][grey53]*[/grey53][dark_turquoise]*[/dark_turquoise][grey53]*[/grey53][dark_turquoise]*[/dark_turquoise][grey53]*[/grey53][dark_turquoise]*[/dark_turquoise][grey53]*[/grey53][dark_turquoise]*[/dark_turquoise][grey53]*[/grey53][dark_turquoise]*[/dark_turquoise][grey53]*[/grey53][dark_turquoise]*[/dark_turquoise][grey53]*[/grey53][dark_turquoise]*[/dark_turquoise]")
