from utils.custom_progresses import exit_progress
from os import system, name
from rich import print
import time


def clear_screen():

    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')


def exit_program():

    with exit_progress:
        exit = exit_progress.add_task(
            "[italic dark_turquoise]Exiting gracefully...", total=20)

        while not exit_progress.finished:
            exit_progress.update(exit, advance=0.5)
            time.sleep(0.02)

    print("[dark_turquoise]You can find my other projects and contact me [bold][italic][link=https://www.linkedin.com/in/nr-hughes/]HERE[/link][/bold][/italic]")
    print("[dark_turquoise]Goodbye!", ":waving_hand:")
    time.sleep(3)
    exit()
