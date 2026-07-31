from pathlib import Path
from colorama import Fore, Style

current_dir = Path(__file__).parent

def show_directory(path: Path, indent: str = ""):
    # Recursive function to search a directory

    try:
        for item in sorted(path.iterdir()):
            if item.is_dir():
                print(f"{indent}{Fore.BLUE}📁 {item.name}")
                show_directory(item, indent + "    ")
            else:
                print(f"{indent}{Fore.GREEN}📄 {item.name}")

    except PermissionError:
        print(f"{indent}{Fore.RED}No access to: {path}")