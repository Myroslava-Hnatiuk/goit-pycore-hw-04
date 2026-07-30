from pathlib import Path

def total_salary(path):
    current_dir = Path(__file__).parent
    path = Path(path)

    try:
        with open(current_dir / path, "r", encoding="utf-8", errors="strict") as file:
            data = file.readlines()
            total = 0
    
            for line in data:
                salary = line.strip().split(',')[1]
                total += int(salary)
                average = round(total / len(data), 2)
            return total, average

    except FileNotFoundError:
        print(f"File {path} cannot be found")
    except UnicodeDecodeError:
        print(f"File {path} has issues with encoding")

total, average = total_salary('salary.txt')

print(f"Total salary: {total}, Average salary: {average}")