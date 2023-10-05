#!/usr/bin/env python3

from models.language import Language
from models.package import Package
from rich import print
from rich.progress import Progress,  SpinnerColumn, BarColumn, TaskProgressColumn, TextColumn
import time

progress = Progress(
    TextColumn("[progress.description]{task.description}"),
    SpinnerColumn(),
    BarColumn(),
    TaskProgressColumn()
)


def seed_database():
    Package.drop_table()
    Language.drop_table()
    Language.create_table()
    Package.create_table()

    vainilla_js = Language.create("Vanilla JS")
    react = Language.create(
        "React")
    Package.create(
        "Chakra UI", "npm install @chakra-ui/react @emotion/react @emotion/styled framer-motion", react.id)
    Package.create(
        "Tailwind CSS", "npm install -D tailwindcss", vainilla_js.id)
    Package.create("react-icons", "npm install react-icons --save", react.id)
    Package.create("Redux", "npm install @reduxjs/toolkit", react.id)
    Package.create("React-Redux", "npm install react-redux", react.id)
    Package.create("HowlerJS", "npm install howler", vainilla_js.id)
    Package.create("HowlerJS", "npm install howler", vainilla_js.id)
    Package.create("PushJS", "npm install push.js --save", vainilla_js.id)


with progress:
    seeding = progress.add_task(
        "[italic spring_green3]Seeding database[/italic spring_green3][dark_turqoise]...[/dark_turqoise]", total=20)

    while not progress.finished:
        progress.update(seeding, advance=0.5)
        time.sleep(0.02)

seed_database()
print("[bold spring_green3]Seeded database!", ":seedling:")
