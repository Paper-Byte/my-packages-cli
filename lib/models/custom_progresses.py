from rich.progress import Progress,  SpinnerColumn, BarColumn, TaskProgressColumn, TextColumn


debug_progress = Progress(
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
