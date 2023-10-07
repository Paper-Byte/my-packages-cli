from rich.progress import Progress,  SpinnerColumn, BarColumn, TaskProgressColumn, TextColumn

PROGRESS_COUNT = -1
NEW_PROGRESS_LIST = []


def new_progress():
    new_progress = Progress(
        TextColumn("[progress.description]{task.description}"),
        SpinnerColumn(),
        BarColumn(),
        TaskProgressColumn()
    )
    global NEW_PROGRESS_LIST
    NEW_PROGRESS_LIST.append(new_progress)
    global PROGRESS_COUNT
    PROGRESS_COUNT += 1
    return NEW_PROGRESS_LIST[PROGRESS_COUNT]


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
