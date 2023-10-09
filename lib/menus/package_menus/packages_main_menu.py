from models.packages import Package
from rich import print
from menu_helpers.menu_utils import clear_screen
from ascii_titles import PACKAGE
import menus.package_menus.packages_install_choice_menu
import menus.package_menus.packages_sub_menu
import menus.package_menus.packages_name_create_menu
import menus.main_menu


def packages_main_menu():
    clear_screen()
    print(f"[bold dark_turquoise]{PACKAGE}")
    while True:
        packages_main_menu_options()
        choice = input("--> ")
        if ((choice.lower() == "b") or (choice.lower() == "back")):
            menus.main_menu.main_menu()
        elif ((choice.lower() == "c") or (choice.lower() == "create")):
            menus.package_menus.packages_name_create_menu.packages_name_create_menu()
        elif (choice.isnumeric()):
            if (Package.find_by_id(int(choice))):
                menus.package_menus.packages_sub_menu.packages_sub_menu(
                    Package.find_by_id(int(choice)))
            else:
                clear_screen()
                print(f"[bold dark_turquoise]{PACKAGE}")
                print(":white_exclamation_mark:",
                      "[red blink][bold]Error:[/bold] Invalid package option, try again.")
        elif ((choice.lower() == "i") or (choice.lower() == "install")):
            menus.package_menus.packages_install_choice_menu.packages_install_choice_menu()
        else:
            clear_screen()
            print(f"[bold dark_turquoise]{PACKAGE}")
            print(":white_exclamation_mark:",
                  "[red blink][bold]Error:[/bold] Invalid command, try again.")


def packages_main_menu_options():
    all_packages = Package.get_all()
    print("[dark_turquoise]*[/dark_turquoise][grey53]*[/grey53][dark_turquoise]*[/dark_turquoise][grey53]*[/grey53][dark_turquoise]*[/dark_turquoise][grey53]*[/grey53][dark_turquoise]*[/dark_turquoise][grey53]*[/grey53][dark_turquoise]*[/dark_turquoise][grey53]*[/grey53][dark_turquoise]*[/dark_turquoise][grey53]*[/grey53][dark_turquoise]*[/dark_turquoise][grey53]*[/grey53][dark_turquoise]*[/dark_turquoise][grey53]*[/grey53][dark_turquoise]*[/dark_turquoise][grey53]*[/grey53][dark_turquoise]*[/dark_turquoise][grey53]*[/grey53][dark_turquoise]*[/dark_turquoise][grey53]*[/grey53][dark_turquoise]*[/dark_turquoise][grey53]*[/grey53][dark_turquoise]*[/dark_turquoise][grey53]*[/grey53][dark_turquoise]*[/dark_turquoise][grey53]*[/grey53]")
    for package in all_packages:
        print(
            f"[magenta]*[/magenta]  [dark_turquoise]{package.id}: [/dark_turquoise][grey53]{package.name}")
    print("[dark_turquoise]*[/dark_turquoise][grey53]*[/grey53][dark_turquoise]*[/dark_turquoise][grey53]*[/grey53][dark_turquoise]*[/dark_turquoise][grey53]*[/grey53][dark_turquoise]*[/dark_turquoise][grey53]*[/grey53][dark_turquoise]*[/dark_turquoise][grey53]*[/grey53][dark_turquoise]*[/dark_turquoise][grey53]*[/grey53][dark_turquoise]*[/dark_turquoise][grey53]*[/grey53][dark_turquoise]*[/dark_turquoise][grey53]*[/grey53][dark_turquoise]*[/dark_turquoise][grey53]*[/grey53][dark_turquoise]*[/dark_turquoise][grey53]*[/grey53][dark_turquoise]*[/dark_turquoise][grey53]*[/grey53][dark_turquoise]*[/dark_turquoise][grey53]*[/grey53][dark_turquoise]*[/dark_turquoise][grey53]*[/grey53][dark_turquoise]*[/dark_turquoise][grey53]*[/grey53]")
    print("[grey53]*[/grey53]")
    print('[dark_turquoise]*[/dark_turquoise]  [bold][dark_turquoise]"back" [magenta][italic]OR[/italic][/magenta] "b"[/bold][/dark_turquoise][grey53] to return to the previous menu',
          ':right_arrow_curving_left:')
    print(
        '[grey53]*[/grey53]  [bold][dark_turquoise]"create" [magenta][italic]OR[/italic][/magenta] "c"[/bold][/dark_turquoise][grey53] to create a new package', ':floppy_disk:')
    print('[dark_turquoise]*[/dark_turquoise]  [bold][dark_turquoise]"install" [magenta][italic]OR[/italic][/magenta] "i"[/bold][/dark_turquoise][grey53] to install a package',
          ':wrench:')
    print(
        '[grey53]*[/grey53]  [bold][dark_turquoise]NUM[/bold][/dark_turquoise][grey53] to modify a package', ':gear:')
    print("[dark_turquoise]*[/dark_turquoise]")
    print("[grey53]*[/grey53][dark_turquoise]*[/dark_turquoise][grey53]*[/grey53][dark_turquoise]*[/dark_turquoise][grey53]*[/grey53][dark_turquoise]*[/dark_turquoise][grey53]*[/grey53][dark_turquoise]*[/dark_turquoise][grey53]*[/grey53][dark_turquoise]*[/dark_turquoise][grey53]*[/grey53][dark_turquoise]*[/dark_turquoise][grey53]*[/grey53][dark_turquoise]*[/dark_turquoise][grey53]*[/grey53][dark_turquoise]*[/dark_turquoise][grey53]*[/grey53][dark_turquoise]*[/dark_turquoise][grey53]*[/grey53][dark_turquoise]*[/dark_turquoise][grey53]*[/grey53][dark_turquoise]*[/dark_turquoise][grey53]*[/grey53][dark_turquoise]*[/dark_turquoise][grey53]*[/grey53][dark_turquoise]*[/dark_turquoise][grey53]*[/grey53][dark_turquoise]*[/dark_turquoise]")
