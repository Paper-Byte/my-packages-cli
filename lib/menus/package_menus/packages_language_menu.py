from rich import print
from models.language import Language
from menu_helpers.menu_utils import clear_screen
import menu_helpers.packages_menu_helpers
import menus.package_menus.packages_sub_menu
import pyfiglet

ALL_LANGUAGES = Language.get_all()


def packages_language_menu(package):

    PACKAGE_TITLE = pyfiglet.figlet_format((f'{package.name}'), font='mini')
    current_owner = Language.find_by_id(package.language_id)

    clear_screen()
    print(f"[bold dark_turquoise]{PACKAGE_TITLE}")
    while True:
        packages_language_menu_options(current_owner)
        choice = input("--> ")
        if ((choice.lower() == "b") or (choice.lower() == "back")):
            menus.package_menus.packages_sub_menu.packages_sub_menu(package)
        elif (choice.isnumeric()):
            if (int(choice) <= len(ALL_LANGUAGES)):
                menu_helpers.packages_menu_helpers.update_package_language(
                    package, int(choice))
            else:
                clear_screen()
                print(f"[bold dark_turquoise]{PACKAGE_TITLE}")
                print(":white_exclamation_mark:",
                      f"[red blink][bold]Error:[/bold] Invalid option, try again. INT must be in range of 1-{str(len(ALL_LANGUAGES))}")
        else:
            clear_screen()
            print(f"[bold dark_turquoise]{PACKAGE_TITLE}")
            print(":white_exclamation_mark:",
                  "[red blink][bold]Error:[/bold] Invalid command, try again.")


def packages_language_menu_options(current_owner):
    print("[dark_turquoise]*[/dark_turquoise][grey53]*[/grey53][dark_turquoise]*[/dark_turquoise][grey53]*[/grey53][dark_turquoise]*[/dark_turquoise][grey53]*[/grey53][dark_turquoise]*[/dark_turquoise][grey53]*[/grey53][dark_turquoise]*[/dark_turquoise][grey53]*[/grey53][dark_turquoise]*[/dark_turquoise][grey53]*[/grey53][dark_turquoise]*[/dark_turquoise][grey53]*[/grey53][dark_turquoise]*[/dark_turquoise][grey53]*[/grey53][dark_turquoise]*[/dark_turquoise][grey53]*[/grey53][dark_turquoise]*[/dark_turquoise][grey53]*[/grey53][dark_turquoise]*[/dark_turquoise][grey53]*[/grey53][dark_turquoise]*[/dark_turquoise][grey53]*[/grey53][dark_turquoise]*[/dark_turquoise][grey53]*[/grey53][dark_turquoise]*[/dark_turquoise][grey53]*[/grey53]")
    for language in ALL_LANGUAGES:
        print(
            f"[magenta]*[/magenta] [bold][dark_turquoise]{language.id}:[/bold][/dark_turquoise] [grey53]{language.name}")
    print(
        f"[magenta]*[/magenta]  [grey53]Current Language: [/grey53][dark_turquoise]{current_owner.name}")
    print("[dark_turquoise]*[/dark_turquoise][grey53]*[/grey53][dark_turquoise]*[/dark_turquoise][grey53]*[/grey53][dark_turquoise]*[/dark_turquoise][grey53]*[/grey53][dark_turquoise]*[/dark_turquoise][grey53]*[/grey53][dark_turquoise]*[/dark_turquoise][grey53]*[/grey53][dark_turquoise]*[/dark_turquoise][grey53]*[/grey53][dark_turquoise]*[/dark_turquoise][grey53]*[/grey53][dark_turquoise]*[/dark_turquoise][grey53]*[/grey53][dark_turquoise]*[/dark_turquoise][grey53]*[/grey53][dark_turquoise]*[/dark_turquoise][grey53]*[/grey53][dark_turquoise]*[/dark_turquoise][grey53]*[/grey53][dark_turquoise]*[/dark_turquoise][grey53]*[/grey53][dark_turquoise]*[/dark_turquoise][grey53]*[/grey53][dark_turquoise]*[/dark_turquoise][grey53]*[/grey53]")
    print("[grey53]*[/grey53]")
    print('[dark_turquoise]*[/dark_turquoise]  [bold][dark_turquoise]"back" [magenta][italic]OR[/italic][/magenta] "b"[/bold][/dark_turquoise][grey53] to return to the previous menu',
          ':right_arrow_curving_left:')
    print(
        f'[grey53]*[/grey53]  [bold][dark_turquoise]INT[/bold][/dark_turquoise][grey53] to change the package language [italic]*between 1 and {str(len(ALL_LANGUAGES))}*[/italic]', ':fountain_pen:')
    print("[dark_turquoise]*[/dark_turquoise]")
    print("[grey53]*[/grey53][dark_turquoise]*[/dark_turquoise][grey53]*[/grey53][dark_turquoise]*[/dark_turquoise][grey53]*[/grey53][dark_turquoise]*[/dark_turquoise][grey53]*[/grey53][dark_turquoise]*[/dark_turquoise][grey53]*[/grey53][dark_turquoise]*[/dark_turquoise][grey53]*[/grey53][dark_turquoise]*[/dark_turquoise][grey53]*[/grey53][dark_turquoise]*[/dark_turquoise][grey53]*[/grey53][dark_turquoise]*[/dark_turquoise][grey53]*[/grey53][dark_turquoise]*[/dark_turquoise][grey53]*[/grey53][dark_turquoise]*[/dark_turquoise][grey53]*[/grey53][dark_turquoise]*[/dark_turquoise][grey53]*[/grey53][dark_turquoise]*[/dark_turquoise][grey53]*[/grey53][dark_turquoise]*[/dark_turquoise][grey53]*[/grey53][dark_turquoise]*[/dark_turquoise]")
