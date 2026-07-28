from pathlib import Path

def get_cats_info(path):

    path = Path(path)

    if not path.exists():
        raise FileNotFoundError(f"File {path} not found.")

    with open(path, 'r', encoding='utf-8') as file:
        cats_info = file.read()

    cats = []

    lines = [el.strip() for el in cats_info.splitlines()] # Parse the file content into lines and strip whitespace

    for line in lines:
        id, name, age = line.strip().split(',') # Destructure each line into id, name, and age
        cats.append({'id': id, 'name': name, 'age': int(age)}) # Append a dictionary with the cat's information to the cats list

    return cats

cats_info = get_cats_info("cats_file.txt")
print(cats_info)