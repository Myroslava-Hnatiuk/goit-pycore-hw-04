from pathlib import Path

def total_salary(path):
    path = Path(path)

    if not path.exists():
        raise FileNotFoundError(f"File {path} not found.")

    with open(path, 'r', encoding='utf-8') as file:
        data = file.readlines()
        total = 0

    for line in data:
        salary = line.strip().split(',')[1]
        total += int(salary)
        average = round(total / len(data), 2)
    return total, average

total, average = total_salary('salary_file.txt')

print(f"Total salary: {total}, Average salary: {average}")