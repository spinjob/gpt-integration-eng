import os
import shutil
from typing import Dict

class FileOrganizer:
    def __init__(self, directory: str):
        self.directory = directory
        self.file_types: Dict[str, str] = {
            'images': ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff', '.ico'],
            'documents': ['.doc', '.docx', '.pdf', '.txt', '.xls', '.xlsx', '.ppt', '.pptx'],
            'audio': ['.mp3', '.wav', '.ogg', '.flac', '.aac']
        }

    def get_file_type(self, file_name: str) -> str:
        """
        Identify the type of a file based on its extension.
        """
        _, extension = os.path.splitext(file_name)
        for file_type, extensions in self.file_types.items():
            if extension in extensions:
                return file_type
        return 'others'

    def move_file(self, file_name: str, file_type: str) -> None:
        """
        Move a file from its current location to a new location.
        """
        source = os.path.join(self.directory, file_name)
        destination = os.path.join(self.directory, file_type, file_name)
        os.makedirs(os.path.dirname(destination), exist_ok=True)
        shutil.move(source, destination)

    def organize(self) -> None:
        """
        Organize the files in the directory.
        """
        for file_name in os.listdir(self.directory):
            if os.path.isfile(os.path.join(self.directory, file_name)):
                file_type = self.get_file_type(file_name)
                self.move_file(file_name, file_type)
