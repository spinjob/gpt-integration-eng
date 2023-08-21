import os
from file_utils import get_file_type, move_file, create_folder

class FileOrganizer:
    def __init__(self, directory):
        self.directory = directory

    def organize(self):
        for filename in os.listdir(self.directory):
            file_type = get_file_type(filename)
            target_folder = os.path.join(self.directory, file_type)
            create_folder(target_folder)
            move_file(os.path.join(self.directory, filename), target_folder)
