import argparse
from string_processor import reverse_string

def main():
    parser = argparse.ArgumentParser(description='Reverse a string.')
    parser.add_argument('string', type=str, help='The string to reverse.')
    args = parser.parse_args()

    reversed_string = reverse_string(args.string)
    print(reversed_string)

if __name__ == "__main__":
    main()
