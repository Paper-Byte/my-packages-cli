from rich import print
from utils.custom_progresses import new_progress
from menu_helpers.menu_utils import clear_screen
import menus.language_menus.languages_name_menu
import menus.language_menus.languages_main_menu
import time
import pyfiglet


def languages_sub_menu(language):

    LANGUAGE_TITLE = pyfiglet.figlet_format((f'{language.name}'), font='mini')
    LANGUAGE_PACKAGES = language.packages()

    clear_screen()
    print(f"[bold dark_turquoise]{LANGUAGE_TITLE}")
    while True:
        languages_sub_menu_options(language, LANGUAGE_PACKAGES)
        choice = input("--> ")
        if ((choice.lower() == "b") or (choice.lower() == "back")):
            menus.language_menus.languages_main_menu.languages_main_menu()
        elif ((choice.lower() == "n") or (choice.lower() == "nam")):
            menus.language_menus.languages_name_menu.languages_name_menu(
                language)
        elif ((choice.lower() == "d") or (choice.lower() == "del")):
            while True:
                warning_message()
                choice = input("Y/N :> ")
                if (choice.lower() == 'y'):
                    language_del_progress = new_progress()
                    with language_del_progress:
                        delete = language_del_progress.add_task(
                            "[italic][magenta]Deleting language[/italic][magenta][dark_turqoise]...[/dark_turqoise]", total=20)
                        while not language_del_progress.finished:
                            language_del_progress.update(delete, advance=0.5)
                            time.sleep(0.02)
                    clear_screen()
                    for package in LANGUAGE_PACKAGES:
                        package.delete()
                    language.delete()
                    print(
                        f"[bold][magenta]Package was deleted!")
                    time.sleep(2)
                    menus.language_menus.languages_main_menu.languages_main_menu()
        else:
            clear_screen()
            print(f"[bold dark_turquoise]{LANGUAGE_TITLE}")
            print(":white_exclamation_mark:",
                  "[red blink][bold]Error:[/bold] Invalid option, try again.")


def languages_sub_menu_options(language, LANGUAGE_PACKAGES):
    print("[dark_turquoise]*[/dark_turquoise][grey53]*[/grey53][dark_turquoise]*[/dark_turquoise][grey53]*[/grey53][dark_turquoise]*[/dark_turquoise][grey53]*[/grey53][dark_turquoise]*[/dark_turquoise][grey53]*[/grey53][dark_turquoise]*[/dark_turquoise][grey53]*[/grey53][dark_turquoise]*[/dark_turquoise][grey53]*[/grey53][dark_turquoise]*[/dark_turquoise][grey53]*[/grey53][dark_turquoise]*[/dark_turquoise][grey53]*[/grey53][dark_turquoise]*[/dark_turquoise][grey53]*[/grey53][dark_turquoise]*[/dark_turquoise][grey53]*[/grey53][dark_turquoise]*[/dark_turquoise][grey53]*[/grey53][dark_turquoise]*[/dark_turquoise][grey53]*[/grey53][dark_turquoise]*[/dark_turquoise][grey53]*[/grey53][dark_turquoise]*[/dark_turquoise][grey53]*[/grey53]")
    print(f"[magenta]*[/magenta]  [dark_turquoise]{language.name}")
    print(f"[magenta]*  [italic]Packages[/italic]")
    for package in LANGUAGE_PACKAGES:
        print(f"[magenta]*[/magenta]  [dark_turquoise]{package.name}")
    print("[dark_turquoise]*[/dark_turquoise][grey53]*[/grey53][dark_turquoise]*[/dark_turquoise][grey53]*[/grey53][dark_turquoise]*[/dark_turquoise][grey53]*[/grey53][dark_turquoise]*[/dark_turquoise][grey53]*[/grey53][dark_turquoise]*[/dark_turquoise][grey53]*[/grey53][dark_turquoise]*[/dark_turquoise][grey53]*[/grey53][dark_turquoise]*[/dark_turquoise][grey53]*[/grey53][dark_turquoise]*[/dark_turquoise][grey53]*[/grey53][dark_turquoise]*[/dark_turquoise][grey53]*[/grey53][dark_turquoise]*[/dark_turquoise][grey53]*[/grey53][dark_turquoise]*[/dark_turquoise][grey53]*[/grey53][dark_turquoise]*[/dark_turquoise][grey53]*[/grey53][dark_turquoise]*[/dark_turquoise][grey53]*[/grey53][dark_turquoise]*[/dark_turquoise][grey53]*[/grey53]")
    print("[grey53]*[/grey53]")
    print('[dark_turquoise]*[/dark_turquoise]  [bold][dark_turquoise]"back" [magenta][italic]OR[/italic][/magenta] "b"[/bold][/dark_turquoise][grey53] to return to the previous menu',
          ':right_arrow_curving_left:')
    print(
        "[grey53]*[/grey53]  [bold][dark_turquoise]'name' [magenta][italic]OR[/italic][/magenta] 'n'[/bold][/dark_turquoise][grey53] to modify a language's name", ':gear:')
    print(
        "[dark_turquoise]*[/dark_turquoise]  [bold][dark_turquoise]'del' [magenta][italic]OR[/italic][/magenta] 'd'[/bold][/dark_turquoise][grey53] to delete this language", ':cross_mark:')
    print("[grey53]*[/grey53]")
    print("[dark_turquoise]*[/dark_turquoise][grey53]*[/grey53][dark_turquoise]*[/dark_turquoise][grey53]*[/grey53][dark_turquoise]*[/dark_turquoise][grey53]*[/grey53][dark_turquoise]*[/dark_turquoise][grey53]*[/grey53][dark_turquoise]*[/dark_turquoise][grey53]*[/grey53][dark_turquoise]*[/dark_turquoise][grey53]*[/grey53][dark_turquoise]*[/dark_turquoise][grey53]*[/grey53][dark_turquoise]*[/dark_turquoise][grey53]*[/grey53][dark_turquoise]*[/dark_turquoise][grey53]*[/grey53][dark_turquoise]*[/dark_turquoise][grey53]*[/grey53][dark_turquoise]*[/dark_turquoise][grey53]*[/grey53][dark_turquoise]*[/dark_turquoise][grey53]*[/grey53][dark_turquoise]*[/dark_turquoise][grey53]*[/grey53][dark_turquoise]*[/dark_turquoise][grey53]*[/grey53]")


def warning_message():
    print(":white_exclamation_mark:",
          "[red blink] Are you sure? This will delete the language and all references to it! Y/N")
