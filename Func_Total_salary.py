from pathlib import Path

def total_salary(path):
        
    # Створення об'єкту Path для файлу та перевірка на існування та чи файл(не певен поки що у необхідності такої)
    file_path = Path(path)

    '''
    Перевірка існування файлу в даному каталозі (зявилася ідея з пошуком файлу, 
    якщо він відсутній у поточному каталозі, на РС користувача за допомогою Python, 
    та вказання шляху та/або підказки для переходу у вказану(знайдену) директорію через термінал Python,  
    але поки наявних знань замало для реалізації)
    '''
    if not file_path.exists() or not file_path.is_file():

        print(f"Файл {path} відсутній у даному каталозі. Ваш поточний каталог {Path.cwd()} ")
        return
    
    # Обробка, поділ рядків, перетворення у числовий формат та обробка можливих помилок
    salaries = []

    with open(path, "r", encoding="utf-8") as file:
        for line in file:
            line = line.strip()
            if line:
                try:
                    name, salary_str = line.split(',')
                except ValueError:
                    print(f"Неправильний формат рядка: {line}")
                    continue
                try:
                    salary = int(salary_str)
                    salaries.append(salary)
                except ValueError:
                    print(f"Неправильне значення зарплати для: {name}: {salary_str}")
                    continue

    # print(salaries)

    # Обчислення та вивід результатів. 
    if salaries:
        total = sum(salaries)
        average = total / len(salaries)
        print(f"Загальна сума заробітної плати: {total}")
        print(f"Середня заробітна плата: {average:.2f}")
    else:
        print("Не знайдено записів про зарплату.")

total_salary("salary_file.txt") # Correct code execution
# total, average = total_salary("salary_file.txt")

total, average = total_salary("salary_file.txt") # Code execution with error
#print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")


