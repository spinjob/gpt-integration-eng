The core classes and functions that will be necessary for this task are:

1. `FileOrganizer`: This class will be responsible for the main functionality of the tool. It will have methods to scan the directory, identify file types, create corresponding folders, and move files.

2. `main`: This function will be the entry point of the CLI tool. It will parse command line arguments and call the appropriate methods of the `FileOrganizer` class.

3. `get_file_type`: This function will determine the type of a file based on its extension.

4. `move_file`: This function will move a file from one directory to another.

5. `create_folder`: This function will create a new folder if it doesn't already exist.

Now, let's start with the entry point file, `main.py`.

main.py
