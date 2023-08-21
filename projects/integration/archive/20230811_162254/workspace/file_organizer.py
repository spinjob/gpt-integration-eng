import os
import shutil
import click

class FileOrganizer:
    def __init__(self, directory):
        self.directory = directory

    def get_file_type(self, filename):
        """
        Determine the file type based on the file extension.
        """
        _, ext = os.path.splitext(filename)
        ext = ext.lower()

        if ext in ['.jpg', '.png', '.gif']:
            return 'images'
        elif ext in ['.doc', '.docx', '.pdf']:
            return 'documents'
        elif ext in ['.mp3', '.wav', '.flac']:
            return 'audio'
        else:
            return 'others'

    def move_file(self, filename, file_type):
        """
        Move a file to the corresponding folder based on its file type.
        """
        src = os.path.join(self.directory, filename)
        dest_dir = os.path.join(self.directory, file_type)
        os.makedirs(dest_dir, exist_ok=True)
        dest = os.path.join(dest_dir, filename)
        shutil.move(src, dest)

    def organize(self):
        """
        Organize files in the directory.
        """
        for filename in os.listdir(self.directory):
            if os.path.isfile(os.path.join(self.directory, filename)):
                file_type = self.get_file_type(filename)
                self.move_file(filename, file_type)

@click.command()
@click.argument('directory')
def main(directory):
    """
    The entry point of the CLI tool.
    """
    organizer = FileOrganizer(directory)
    organizer.organize()

if __name__ == "__main__":
    main()
