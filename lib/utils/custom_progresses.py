from rich.progress import Progress,  SpinnerColumn, BarColumn, TaskProgressColumn, TextColumn

PACKAGE_NAME_COUNT = -1
NEW_PACKAGE_NAME_LIST = []


def new_package_name_progress():
    new_progress = Progress(
        TextColumn("[progress.description]{task.description}"),
        SpinnerColumn(),
        BarColumn(),
        TaskProgressColumn()
    )
    global NEW_PACKAGE_NAME_LIST
    NEW_PACKAGE_NAME_LIST.append(new_progress)
    global PACKAGE_NAME_COUNT
    PACKAGE_NAME_COUNT += 1
    return NEW_PACKAGE_NAME_LIST[PACKAGE_NAME_COUNT]


exit_progress = Progress(
    TextColumn("[progress.description]{task.description}"),
    SpinnerColumn(),
    BarColumn(),
    TaskProgressColumn()
)

seed_progress = Progress(
    TextColumn("[progress.description]{task.description}"),
    SpinnerColumn(),
    BarColumn(),
    TaskProgressColumn()
)

debug_progress = Progress(
    TextColumn("[progress.description]{task.description}"),
    SpinnerColumn(),
    BarColumn(),
    TaskProgressColumn()
)
