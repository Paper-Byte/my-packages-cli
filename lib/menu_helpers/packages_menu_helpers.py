from utils.custom_progresses import new_package_name_progress
from utils.custom_progresses import new_package_command_progress
from menu_helpers.menu_utils import clear_screen
from rich import print
import menus.package_menus.packages_sub_menu  # packages_sub_menu()
import time


def update_package_name(package, choice):
    package_name_progress = new_package_name_progress()
    with package_name_progress:
        name = package_name_progress.add_task(
            "[italic][magenta]Updating package's name[/italic][magenta][dark_turqoise]...[/dark_turqoise]", total=20)
        while not package_name_progress.finished:
            package_name_progress.update(name, advance=0.5)
            time.sleep(0.02)
    clear_screen()
    package.name = choice
    package.update()
    print(f"[bold][magenta]Package name updated to '{choice}'!")
    time.sleep(2)
    menus.package_menus.packages_sub_menu.packages_sub_menu(package)


def update_package_command(package, choice):
    package_command_progress = new_package_command_progress()
    with package_command_progress:
        command = package_command_progress.add_task(
            "[italic][magenta]Updating package's command[/italic][magenta][dark_turqoise]...[/dark_turqoise]", total=20)
        while not package_command_progress.finished:
            package_command_progress.update(command, advance=0.5)
            time.sleep(0.02)
    clear_screen()
    package.command = choice
    package.update()
    print(f"[bold][magenta]Package command updated to '{choice}'!")
    time.sleep(2)
    menus.package_menus.packages_sub_menu.packages_sub_menu(package)
