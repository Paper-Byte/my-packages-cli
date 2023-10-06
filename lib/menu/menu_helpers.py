from models.language import Language
from models.package import Package
from utils.custom_progresses import progress
from rich import print
import time


def exit_program():

    with progress:
        exit = progress.add_task(
            "[italic dark_turquoise]Exiting gracefully...", total=20)

        while not progress.finished:
            progress.update(exit, advance=0.5)
            time.sleep(0.02)

    print("[dark_turquoise]You can find my other projects and contact me [bold][italic][link=https://www.linkedin.com/in/nr-hughes/]HERE[/link][/bold][/italic]")
    print("[dark_turquoise]Goodbye!", ":waving_hand:")
    time.sleep(3)
    exit()
# Language helpers
