import os
import shutil
import mimetypes

def get_file_type(filename):
    # Use the mimetypes module to get the file type based on the extension
    type_info = mimetypes.guess_type(filename)
    if type_info[0] is None:
        return 'Unknown'
    return type_info[0].split('/')[0]

def move_file(source, destination):
    shutil.move(source, destination)

def create_folder(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)
