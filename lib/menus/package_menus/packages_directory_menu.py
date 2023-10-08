from ascii_titles import INSTALL_PACKAGE
from models.language import Language
from rich import print
from menu_helpers.menu_utils import clear_screen
import menus.package_menus.packages_install_choice_menu
import menus.package_menus.packages_install_confirm_menu


def packages_directory_menu(package):

    package_language = Language.find_by_id(package.language_id)

    clear_screen()
    print(f"[bold dark_turquoise]{INSTALL_PACKAGE}")
    while True:
        packages_directory_menu_options(package, package_language)
        choice = input("FILEPATH :> ")
        if ((choice.lower() == "b") or (choice.lower() == "back")):
            menus.package_menus.packages_install_choice_menu.packages_install_choice_menu()
        if ((not choice.isnumeric()) and (len(choice) >= 10)):
            directory = choice
            menus.package_menus.packages_install_confirm_menu.packages_install_confirm_menu(
                package, package_language, directory)
        else:
            print(f"[bold dark_turquoise]{INSTALL_PACKAGE}")
            print(":white_exclamation_mark:",
                  "[red blink][bold]Error:[/bold] Invalid path, try again.")


def packages_directory_menu_options(package, package_language):
    print("[dark_turquoise]*[/dark_turquoise][grey53]*[/grey53][dark_turquoise]*[/dark_turquoise][grey53]*[/grey53][dark_turquoise]*[/dark_turquoise][grey53]*[/grey53][dark_turquoise]*[/dark_turquoise][grey53]*[/grey53][dark_turquoise]*[/dark_turquoise][grey53]*[/grey53][dark_turquoise]*[/dark_turquoise][grey53]*[/grey53][dark_turquoise]*[/dark_turquoise][grey53]*[/grey53][dark_turquoise]*[/dark_turquoise][grey53]*[/grey53][dark_turquoise]*[/dark_turquoise][grey53]*[/grey53][dark_turquoise]*[/dark_turquoise][grey53]*[/grey53][dark_turquoise]*[/dark_turquoise][grey53]*[/grey53][dark_turquoise]*[/dark_turquoise][grey53]*[/grey53][dark_turquoise]*[/dark_turquoise][grey53]*[/grey53][dark_turquoise]*[/dark_turquoise][grey53]*[/grey53]")
    print(
        f"[magenta]*[/magenta]  [dark_turquoise]Package: [/dark_turquoise][grey53]{package.name}")
    print(
        f"[magenta]*[/magenta]  [dark_turquoise]Language: [/dark_turquoise][grey53]{package_language.name}")
    print(
        f"[magenta]*[/magenta]  [dark_turquoise]Exact file path: [/dark_turquoise][grey53][itlaic]input below...")
    print("[dark_turquoise]*[/dark_turquoise][grey53]*[/grey53][dark_turquoise]*[/dark_turquoise][grey53]*[/grey53][dark_turquoise]*[/dark_turquoise][grey53]*[/grey53][dark_turquoise]*[/dark_turquoise][grey53]*[/grey53][dark_turquoise]*[/dark_turquoise][grey53]*[/grey53][dark_turquoise]*[/dark_turquoise][grey53]*[/grey53][dark_turquoise]*[/dark_turquoise][grey53]*[/grey53][dark_turquoise]*[/dark_turquoise][grey53]*[/grey53][dark_turquoise]*[/dark_turquoise][grey53]*[/grey53][dark_turquoise]*[/dark_turquoise][grey53]*[/grey53][dark_turquoise]*[/dark_turquoise][grey53]*[/grey53][dark_turquoise]*[/dark_turquoise][grey53]*[/grey53][dark_turquoise]*[/dark_turquoise][grey53]*[/grey53][dark_turquoise]*[/dark_turquoise][grey53]*[/grey53]")
    print("[grey53]*[/grey53]")
    print('[dark_turquoise]*[/dark_turquoise]  [bold][dark_turquoise]"back" [magenta][italic]OR[/italic][/magenta] "b"[/bold][/dark_turquoise][grey53] to return to the previous menu',
          ':right_arrow_curving_left:')
    print(
        '[grey53]*[/grey53]  [bold][dark_turquoise]INPUT[/bold][/dark_turquoise][grey53] to set [bold]exact[/bold] file path', ':robot:')
    print("[dark_turquoise]*[/dark_turquoise]")
    print("[grey53]*[/grey53][dark_turquoise]*[/dark_turquoise][grey53]*[/grey53][dark_turquoise]*[/dark_turquoise][grey53]*[/grey53][dark_turquoise]*[/dark_turquoise][grey53]*[/grey53][dark_turquoise]*[/dark_turquoise][grey53]*[/grey53][dark_turquoise]*[/dark_turquoise][grey53]*[/grey53][dark_turquoise]*[/dark_turquoise][grey53]*[/grey53][dark_turquoise]*[/dark_turquoise][grey53]*[/grey53][dark_turquoise]*[/dark_turquoise][grey53]*[/grey53][dark_turquoise]*[/dark_turquoise][grey53]*[/grey53][dark_turquoise]*[/dark_turquoise][grey53]*[/grey53][dark_turquoise]*[/dark_turquoise][grey53]*[/grey53][dark_turquoise]*[/dark_turquoise][grey53]*[/grey53][dark_turquoise]*[/dark_turquoise][grey53]*[/grey53][dark_turquoise]*[/dark_turquoise]")
