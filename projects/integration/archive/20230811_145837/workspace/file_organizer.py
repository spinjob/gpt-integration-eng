import os
import shutil
import click

class FileOrganizer:
    def __init__(self, directory):
        self.directory = directory

    def get_file_type(self, filename):
        """
        Identify the file type based on the file extension
        """
        _, ext = os.path.splitext(filename)
        ext = ext.lower()
        if ext in ['.jpg', '.png', '.gif']:
            return 'images'
        elif ext in ['.doc', '.docx', '.pdf']:
            return 'documents'
        elif ext in ['.mp3', '.wav']:
            return 'audio'
        else:
            return 'others'

    def move_file(self, filename, file_type):
        """
        Move the file to the corresponding folder
        """
        source = os.path.join(self.directory, filename)
        destination = os.path.join(self.directory, file_type, filename)
        os.makedirs(os.path.dirname(destination), exist_ok=True)
        shutil.move(source, destination)

    def organize(self):
        """
        Iterate over all files in the directory and organize them
        """
        for filename in os.listdir(self.directory):
            if os.path.isfile(os.path.join(self.directory, filename)):
                file_type = self.get_file_type(filename)
                self.move_file(filename, file_type)

@click.command()
@click.argument('directory')
def main(directory):
    """
    The entry point of the CLI tool. It parses command line arguments and calls the organize function.
    """
    organizer = FileOrganizer(directory)
    organizer.organize()

if __name__ == "__main__":
    main()
