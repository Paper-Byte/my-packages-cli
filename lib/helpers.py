from models.language import Language
from models.package import Package
from rich.progress import Progress,  SpinnerColumn, BarColumn, TaskProgressColumn, TextColumn
import time
from rich import print


def exit_program():
    print("Goodbye!", ":waving hand:")
    exit()

# Language helpers
