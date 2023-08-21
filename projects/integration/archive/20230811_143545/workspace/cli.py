import click
from file_organizer import FileOrganizer

@click.command()
@click.argument('directory')
def organize(directory: str) -> None:
    """
    Organize the files in the directory.
    """
    organizer = FileOrganizer(directory)
    organizer.organize()

if __name__ == '__main__':
    organize()
