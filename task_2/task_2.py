from pathlib import Path

def get_cats_info(path):
    current_dir = Path(__file__).parent
    path = Path(path)

    try:
        with open(current_dir / path, "r", encoding="utf-8", errors="strict") as file:
            cats_info = file.read()
            cats = []
            lines = [el.strip() for el in cats_info.splitlines()] # Parse the file content into lines and strip whitespace

            for index, line in enumerate(lines, start=1):
                try:    
                    id, name, age = line.strip().split(',') # Destructure each line into id, name, and age
                    cats.append({'id': id, 'name': name, 'age': int(age)}) # Append a dictionary with the cat's information to the cats list
                except:
                    print(f"Line {index} is invalid")

            return cats

    except FileNotFoundError:
        print(f"File {path} cannot be found")
        return []
    except UnicodeDecodeError:
        print(f"File {path} has issues with encoding")
        return []

cats_info = get_cats_info('cats.txt')
print(cats_info)