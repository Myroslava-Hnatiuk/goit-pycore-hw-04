import sys
from pathlib import Path
from colorama import Fore
from show_directory import show_directory 

current_dir = Path(__file__).parent
print(current_dir)

def main():
    # Check number of arguments
    if len(sys.argv) != 2:
        print(f"{Fore.RED}Wrong usage: python main.py <path to directory>")
        sys.exit(1)

    directory = Path(sys.argv[1])

    # Check if directory exists
    if not directory.exists():
        print(f"{Fore.RED}Error: path does not exist.")
        sys.exit(1)

    # Check if this is directory
    if not directory.is_dir():
        print(f"{Fore.RED}Error: entered path is not directory.")
        sys.exit(1)

    print(f"{Fore.YELLOW}{directory.resolve().name}")
    show_directory(directory)

if __name__ == "__main__":
    main()