from ascii_titles import INSTALL_PACKAGE
from rich import print
from menu_helpers.menu_utils import clear_screen
from menu_helpers.packages_menu_helpers import install_package
import menus.package_menus.packages_directory_menu


def packages_install_confirm_menu(package, package_language, directory):
    clear_screen()
    print(f"[bold][dark_turquoise]{INSTALL_PACKAGE}")
    while True:
        packages_install_confirm_menu_options(
            package, package_language, directory)
        choice = input("Y/N :> ")
        if (choice.lower() == "n"):
            menus.package_menus.packages_directory_menu.packages_directory_menu(
                package)
        elif (choice.lower() == 'y'):
            install_package(package, directory)
        else:
            clear_screen()
            print(f"[bold dark_turquoise]{INSTALL_PACKAGE}")
            print(":white_exclamation_mark:",
                  "[red blink][bold]Error:[/bold] Invalid option, try again.")


def packages_install_confirm_menu_options(package, package_language, directory):
    print("[dark_turquoise]*[/dark_turquoise][grey53]*[/grey53][dark_turquoise]*[/dark_turquoise][grey53]*[/grey53][dark_turquoise]*[/dark_turquoise][grey53]*[/grey53][dark_turquoise]*[/dark_turquoise][grey53]*[/grey53][dark_turquoise]*[/dark_turquoise][grey53]*[/grey53][dark_turquoise]*[/dark_turquoise][grey53]*[/grey53][dark_turquoise]*[/dark_turquoise][grey53]*[/grey53][dark_turquoise]*[/dark_turquoise][grey53]*[/grey53][dark_turquoise]*[/dark_turquoise][grey53]*[/grey53][dark_turquoise]*[/dark_turquoise][grey53]*[/grey53][dark_turquoise]*[/dark_turquoise][grey53]*[/grey53][dark_turquoise]*[/dark_turquoise][grey53]*[/grey53][dark_turquoise]*[/dark_turquoise][grey53]*[/grey53][dark_turquoise]*[/dark_turquoise][grey53]*[/grey53]")
    print(
        f"[magenta]*[/magenta]  [dark_turquoise]Package: [/dark_turquoise][grey53]{package.name}")
    print(
        f"[magenta]*[/magenta]  [dark_turquoise]Language: [/dark_turquoise][grey53]{package_language.name}")
    print(
        f"[magenta]*[/magenta]  [dark_turquoise]Directory: [/dark_turquoise][grey53]{directory}")
    print("[dark_turquoise]*[/dark_turquoise][grey53]*[/grey53][dark_turquoise]*[/dark_turquoise][grey53]*[/grey53][dark_turquoise]*[/dark_turquoise][grey53]*[/grey53][dark_turquoise]*[/dark_turquoise][grey53]*[/grey53][dark_turquoise]*[/dark_turquoise][grey53]*[/grey53][dark_turquoise]*[/dark_turquoise][grey53]*[/grey53][dark_turquoise]*[/dark_turquoise][grey53]*[/grey53][dark_turquoise]*[/dark_turquoise][grey53]*[/grey53][dark_turquoise]*[/dark_turquoise][grey53]*[/grey53][dark_turquoise]*[/dark_turquoise][grey53]*[/grey53][dark_turquoise]*[/dark_turquoise][grey53]*[/grey53][dark_turquoise]*[/dark_turquoise][grey53]*[/grey53][dark_turquoise]*[/dark_turquoise][grey53]*[/grey53][dark_turquoise]*[/dark_turquoise][grey53]*[/grey53]")
    print("[grey53]*[/grey53]")
    print(
        '[dark_turquoise]*[/dark_turquoise]  [bold][dark_turquoise]Y/N[/bold][/dark_turquoise][grey53] is this correct?', ':robot:')
    print("[grey53]*[/grey53]")
    print("[dark_turquoise]*[/dark_turquoise][grey53]*[/grey53][dark_turquoise]*[/dark_turquoise][grey53]*[/grey53][dark_turquoise]*[/dark_turquoise][grey53]*[/grey53][dark_turquoise]*[/dark_turquoise][grey53]*[/grey53][dark_turquoise]*[/dark_turquoise][grey53]*[/grey53][dark_turquoise]*[/dark_turquoise][grey53]*[/grey53][dark_turquoise]*[/dark_turquoise][grey53]*[/grey53][dark_turquoise]*[/dark_turquoise][grey53]*[/grey53][dark_turquoise]*[/dark_turquoise][grey53]*[/grey53][dark_turquoise]*[/dark_turquoise][grey53]*[/grey53][dark_turquoise]*[/dark_turquoise][grey53]*[/grey53][dark_turquoise]*[/dark_turquoise][grey53]*[/grey53][dark_turquoise]*[/dark_turquoise][grey53]*[/grey53][dark_turquoise]*[/dark_turquoise][grey53]*[/grey53]")
