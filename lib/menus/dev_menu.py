from utils.seed import seed_database
from utils.debug import reset_database
from ascii_titles import DEVELOPER
from rich import print
import menus.main_menu  # main_menu()
import menu_helpers.menu_utils  # clear_screen()


def dev_menu():
    menu_helpers.menu_utils.clear_screen()
    print(f"[bold dark_turquoise]{DEVELOPER}")
    while True:
        developer_menu_options()
        choice = input("--> ")
        if ((choice.lower() == "b") or (choice.lower() == "back")):
            menus.main_menu.main_menu()
        elif ((choice.lower() == "s") or (choice.lower() == "seed")):
            while True:
                warning_message()
                choice = input("Y/N :> ")
                if (choice.lower() == 'y'):
                    seed_database()
                    dev_menu()
                elif (choice.lower() == 'n'):
                    dev_menu()
        elif ((choice.lower() == "r") or (choice.lower() == "reset")):
            while True:
                warning_message()
                choice = input("Y/N :> ")
                if (choice.lower() == 'y'):
                    reset_database()
                elif (choice.lower() == 'n'):
                    dev_menu()
        else:
            print(f"[bold dark_turquoise]{DEVELOPER}")
            print(":white_exclamation_mark:",
                  "[red blink][bold]Error:[/bold] Invalid option, try again.")


def developer_menu_options():
    print("[dark_turquoise]*[/dark_turquoise][grey53]*[/grey53][dark_turquoise]*[/dark_turquoise][grey53]*[/grey53][dark_turquoise]*[/dark_turquoise][grey53]*[/grey53][dark_turquoise]*[/dark_turquoise][grey53]*[/grey53][dark_turquoise]*[/dark_turquoise][grey53]*[/grey53][dark_turquoise]*[/dark_turquoise][grey53]*[/grey53][dark_turquoise]*[/dark_turquoise][grey53]*[/grey53][dark_turquoise]*[/dark_turquoise][grey53]*[/grey53][dark_turquoise]*[/dark_turquoise][grey53]*[/grey53][dark_turquoise]*[/dark_turquoise][grey53]*[/grey53][dark_turquoise]*[/dark_turquoise][grey53]*[/grey53][dark_turquoise]*[/dark_turquoise][grey53]*[/grey53][dark_turquoise]*[/dark_turquoise][grey53]*[/grey53][dark_turquoise]*[/dark_turquoise][grey53]*[/grey53]")
    print("[grey53]*[/grey53]")
    print('[dark_turquoise]*[/dark_turquoise]  [bold][dark_turquoise]"back" [magenta][italic]OR[/italic][/magenta] "b"[/bold][/dark_turquoise][grey53] to return to the previous menu',
          ':right_arrow_curving_left:')
    print(
        '[grey53]*[/grey53]  [bold][dark_turquoise]"seed" [magenta][italic]OR[/italic][/magenta] "s"[/bold][/dark_turquoise][dark_turquoise] to seed database with defaults', ':robot:')
    print('[dark_turquoise]*[/dark_turquoise]  [bold][dark_turquoise]"reset" [magenta][italic]OR[/italic][/magenta] "r"[/bold][/dark_turquoise][grey53] to reset database and debug',
          ':right_arrow_curving_left:')
    print("[grey53]*[/grey53]")
    print("[dark_turquoise]*[/dark_turquoise][grey53]*[/grey53][dark_turquoise]*[/dark_turquoise][grey53]*[/grey53][dark_turquoise]*[/dark_turquoise][grey53]*[/grey53][dark_turquoise]*[/dark_turquoise][grey53]*[/grey53][dark_turquoise]*[/dark_turquoise][grey53]*[/grey53][dark_turquoise]*[/dark_turquoise][grey53]*[/grey53][dark_turquoise]*[/dark_turquoise][grey53]*[/grey53][dark_turquoise]*[/dark_turquoise][grey53]*[/grey53][dark_turquoise]*[/dark_turquoise][grey53]*[/grey53][dark_turquoise]*[/dark_turquoise][grey53]*[/grey53][dark_turquoise]*[/dark_turquoise][grey53]*[/grey53][dark_turquoise]*[/dark_turquoise][grey53]*[/grey53][dark_turquoise]*[/dark_turquoise][grey53]*[/grey53][dark_turquoise]*[/dark_turquoise][grey53]*[/grey53]")


def warning_message():
    print(":white_exclamation_mark:",
          "[red blink] Are you sure? This will reset the databse to default! Y/N")
