from utils.custom_progresses import new_progress
from menu_helpers.menu_utils import clear_screen
from models.package import Package
from models.language import Language
from rich import print
from shlex import split
import menus.package_menus.packages_sub_menu
import menus.package_menus.packages_main_menu
import subprocess
import time


def update_package_name(package, choice):
    new_name_progress = new_progress()
    with new_name_progress:
        name = new_name_progress.add_task(
            "[italic][magenta]Updating package's name[/italic][magenta][dark_turqoise]...[/dark_turqoise]", total=20)
        while not new_name_progress.finished:
            new_name_progress.update(name, advance=0.5)
            time.sleep(0.02)
    clear_screen()
    package.name = choice
    package.update()
    print(f"[bold][magenta]Package name updated to '{choice}'!")
    time.sleep(2)
    menus.package_menus.packages_sub_menu.packages_sub_menu(package)


def update_package_command(package, choice):
    new_command_progress = new_progress()
    with new_command_progress:
        command = new_command_progress.add_task(
            "[italic][magenta]Updating package's command[/italic][magenta][dark_turqoise]...[/dark_turqoise]", total=20)
        while not new_command_progress.finished:
            new_command_progress.update(command, advance=0.5)
            time.sleep(0.02)
    clear_screen()
    package.command = choice
    package.update()
    print(f"[bold][magenta]Package command updated to '{choice}'!")
    time.sleep(2)
    menus.package_menus.packages_sub_menu.packages_sub_menu(package)


def update_package_language(package, choice):
    current_owner = Language.find_by_id(choice)
    new_language_progress = new_progress()
    with new_language_progress:
        language = new_language_progress.add_task(
            "[italic][magenta]Updating package's language[/italic][magenta][dark_turqoise]...[/dark_turqoise]", total=20)
        while not new_language_progress.finished:
            new_language_progress.update(language, advance=0.5)
            time.sleep(0.02)
    clear_screen()
    package.language_id = current_owner.id
    package.update()
    print(
        f"[bold][magenta]Package language updated to '{current_owner.name}'!")
    time.sleep(2)
    menus.package_menus.packages_sub_menu.packages_sub_menu(package)


def create_new_package(new_package_name, new_package_command, new_package_language_id):
    new_package_create_progress = new_progress()
    with new_package_create_progress:
        language = new_package_create_progress.add_task(
            "[italic][magenta]Create new package[/italic][magenta][dark_turqoise]...[/dark_turqoise]", total=20)
        while not new_package_create_progress.finished:
            new_package_create_progress.update(language, advance=0.5)
            time.sleep(0.02)
    clear_screen()
    Package.create(new_package_name, new_package_command,
                   new_package_language_id)
    print(
        f"[bold][magenta]{new_package_name} package created!")
    time.sleep(2)
    menus.package_menus.packages_main_menu.packages_main_menu()


def install_package(package, directory):
    install_command = split(package.command)
    install_run = subprocess.Popen(
        install_command, cwd=directory)
    exit_code = install_run.wait()
    print(":white_exclamation_mark:", '[bold spring_green3]Install succeeded!') if exit_code == 0 else print(
        '[red blink][bold]Install failed!')
    time.sleep(2)
    menus.package_menus.packages_main_menu.packages_main_menu()
