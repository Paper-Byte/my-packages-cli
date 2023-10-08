from utils.custom_progresses import new_progress
from menu_helpers.menu_utils import clear_screen
from models.language import Language
from rich import print
import menus.language_menus.languages_sub_menu
import menus.language_menus.languages_main_menu
import time


def update_language_name(language, choice):
    new_name_progress = new_progress()
    with new_name_progress:
        name = new_name_progress.add_task(
            "[italic][magenta]Updating language's name[/italic][magenta][dark_turqoise]...[/dark_turqoise]", total=20)
        while not new_name_progress.finished:
            new_name_progress.update(name, advance=0.5)
            time.sleep(0.02)
    clear_screen()
    language.name = choice
    language.update()
    print(f"[bold][magenta]Language name updated to '{choice}'!")
    time.sleep(2)
    menus.language_menus.languages_sub_menu.languages_sub_menu(language)


def create_new_language(new_language_name):
    new_language_create_progress = new_progress()
    with new_language_create_progress:
        language = new_language_create_progress.add_task(
            "[italic][magenta]Create new language[/italic][magenta][dark_turqoise]...[/dark_turqoise]", total=20)
        while not new_language_create_progress.finished:
            new_language_create_progress.update(language, advance=0.5)
            time.sleep(0.02)
    clear_screen()
    Language.create(new_language_name)
    print(
        f"[bold][magenta]{new_language_name} language created!")
    time.sleep(2)
    menus.language_menus.languages_main_menu.languages_main_menu()
