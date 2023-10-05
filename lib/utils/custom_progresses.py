from rich.progress import Progress,  SpinnerColumn, BarColumn, TaskProgressColumn, TextColumn


progress = Progress(
    TextColumn("[progress.description]{task.description}"),
    SpinnerColumn(),
    BarColumn(),
    TaskProgressColumn()
)
