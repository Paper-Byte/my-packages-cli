from models.language import Language
from ascii_titles import PACKAGE_CREATE
from rich import print
from menu_helpers.menu_utils import clear_screen
import menus.package_menus.packages_command_create_menu
import menus.package_menus.packages_confirm_create_menu


def packages_language_create_menu(new_package_name, new_package_command):
    new_package_language_name = ""
    clear_screen()
    print(f"[bold][dark_turquoise]{PACKAGE_CREATE}")
    while True:
        packages_language_create_menu_options(
            new_package_name, new_package_command, new_package_language_name)
        choice = input("INT :> ")
        if ((choice.lower() == "b") or (choice.lower() == "back")):
            menus.package_menus.packages_command_create_menu.packages_command_create_menu(
                new_package_name)
        elif (choice.isnumeric()):
            if (Language.find_by_id(int(choice))):
                chosen_language = Language.find_by_id(int(choice))
                new_package_language_name = chosen_language.name
                new_package_language_id = chosen_language.id
                menus.package_menus.packages_confirm_create_menu.packages_confirm_create_menu(
                    new_package_name, new_package_command, new_package_language_name, new_package_language_id)
            else:
                clear_screen()
                print(f"[bold dark_turquoise]{PACKAGE_CREATE}")
                print(":white_exclamation_mark:",
                      "[red blink][bold]Error:[/bold] Invalid language option, try again.")
        else:
            clear_screen()
            print(f"[bold dark_turquoise]{PACKAGE_CREATE}")
            print(":white_exclamation_mark:",
                  "[red blink][bold]Error:[/bold] Invalid command, try again.")


def packages_language_create_menu_options(new_package_name, new_package_command, new_package_language_name):
    all_languages = Language.get_all()
    print("[dark_turquoise]*[/dark_turquoise][grey53]*[/grey53][dark_turquoise]*[/dark_turquoise][grey53]*[/grey53][dark_turquoise]*[/dark_turquoise][grey53]*[/grey53][dark_turquoise]*[/dark_turquoise][grey53]*[/grey53][dark_turquoise]*[/dark_turquoise][grey53]*[/grey53][dark_turquoise]*[/dark_turquoise][grey53]*[/grey53][dark_turquoise]*[/dark_turquoise][grey53]*[/grey53][dark_turquoise]*[/dark_turquoise][grey53]*[/grey53][dark_turquoise]*[/dark_turquoise][grey53]*[/grey53][dark_turquoise]*[/dark_turquoise][grey53]*[/grey53][dark_turquoise]*[/dark_turquoise][grey53]*[/grey53][dark_turquoise]*[/dark_turquoise][grey53]*[/grey53][dark_turquoise]*[/dark_turquoise][grey53]*[/grey53][dark_turquoise]*[/dark_turquoise][grey53]*[/grey53]")
    for language in all_languages:
        print(
            f"[magenta]*[/magenta]  [dark_turquoise]{language.id}: [/dark_turquoise][grey53]{language.name}")
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
        f'[grey53]*[/grey53]  [bold][dark_turquoise]INT[/bold][/dark_turquoise][grey53] to set the package language [italic]*int in range of 1 - {str(len(all_languages))}*[/italic]', ':robot:')
    print("[dark_turquoise]*[/dark_turquoise]")
    print("[grey53]*[/grey53][dark_turquoise]*[/dark_turquoise][grey53]*[/grey53][dark_turquoise]*[/dark_turquoise][grey53]*[/grey53][dark_turquoise]*[/dark_turquoise][grey53]*[/grey53][dark_turquoise]*[/dark_turquoise][grey53]*[/grey53][dark_turquoise]*[/dark_turquoise][grey53]*[/grey53][dark_turquoise]*[/dark_turquoise][grey53]*[/grey53][dark_turquoise]*[/dark_turquoise][grey53]*[/grey53][dark_turquoise]*[/dark_turquoise][grey53]*[/grey53][dark_turquoise]*[/dark_turquoise][grey53]*[/grey53][dark_turquoise]*[/dark_turquoise][grey53]*[/grey53][dark_turquoise]*[/dark_turquoise][grey53]*[/grey53][dark_turquoise]*[/dark_turquoise][grey53]*[/grey53][dark_turquoise]*[/dark_turquoise][grey53]*[/grey53][dark_turquoise]*[/dark_turquoise]")
