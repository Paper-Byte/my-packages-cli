from rich.progress import Progress,  SpinnerColumn, BarColumn, TaskProgressColumn, TextColumn


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
