from rich.progress import Progress,  SpinnerColumn, BarColumn, TaskProgressColumn, TextColumn

SEED_COUNT = -1
NEW_SEED_LIST = []
PACKAGE_NAME_COUNT = -1
NEW_PACKAGE_NAME_LIST = []
PACKAGE_COMMAND_COUNT = -1
NEW_PACKAGE_COMMAND_LIST = []


def new_seed_progress():
    new_progress = Progress(
        TextColumn("[progress.description]{task.description}"),
        SpinnerColumn(),
        BarColumn(),
        TaskProgressColumn()
    )
    global NEW_SEED_LIST
    NEW_SEED_LIST.append(new_progress)
    global SEED_COUNT
    SEED_COUNT += 1
    return NEW_SEED_LIST[SEED_COUNT]


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


def new_package_command_progress():
    new_progress = Progress(
        TextColumn("[progress.description]{task.description}"),
        SpinnerColumn(),
        BarColumn(),
        TaskProgressColumn()
    )
    global NEW_PACKAGE_COMMAND_LIST
    NEW_PACKAGE_COMMAND_LIST.append(new_progress)
    global PACKAGE_COMMAND_COUNT
    PACKAGE_COMMAND_COUNT += 1
    return NEW_PACKAGE_COMMAND_LIST[PACKAGE_COMMAND_COUNT]


debug_progress = Progress(
    TextColumn("[progress.description]{task.description}"),
    SpinnerColumn(),
    BarColumn(),
    TaskProgressColumn()
)

exit_progress = Progress(
    TextColumn("[progress.description]{task.description}"),
    SpinnerColumn(),
    BarColumn(),
    TaskProgressColumn()
)
