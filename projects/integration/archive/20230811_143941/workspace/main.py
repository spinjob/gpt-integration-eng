import argparse
from file_organizer import FileOrganizer

def main():
    parser = argparse.ArgumentParser(description='Organize files in a directory based on their types.')
    parser.add_argument('directory', type=str, help='The directory to organize.')
    args = parser.parse_args()

    organizer = FileOrganizer(args.directory)
    organizer.organize()

if __name__ == "__main__":
    main()
