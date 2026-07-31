from pathlib import Path

def total_salary(path):
    current_dir = Path(__file__).parent
    path = Path(path)

    try:
        with open(current_dir / path, "r", encoding="utf-8", errors="strict") as file:
            data = file.readlines()
            total = 0
            average = 0
            valid_lines = 0
    
            for line in data:
                try:
                    if(len(line.strip()) > 0): # Line is valid
                        salary = line.strip().split(',')[1]
                        valid_lines += 1
                        total += int(salary)

                        if valid_lines == 0: # Cover the case dividing to zero
                            print("No valid salary entries found")
                            
                        else:
                            average = round(total / valid_lines, 2)
                except:
                    print(f"Line in file {path} is invalid")
                    continue
            return total, average

    except FileNotFoundError:
        print(f"File {path} cannot be found")
        return 0, 0
    except UnicodeDecodeError:
        print(f"File {path} has issues with encoding")
        return 0, 0


total, average = total_salary('salary.txt')

print(f"Total salary: {total}, Average salary: {average}")