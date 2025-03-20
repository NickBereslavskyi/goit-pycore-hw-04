import sys
from pathlib import Path
from colorama import init, Fore, Style

def visualize_directory_structure(directory, indent=""):
    """Рекурсивно виводить структуру директорії з кольоровим форматуванням, використовуючи пробіли для відступів."""
    entries = sorted(directory.iterdir())  # Сортуємо список файлів і папок
    for entry in entries:
        if entry.is_dir():
            print(f"{indent}{Fore.BLUE}{entry.name}/{Style.RESET_ALL}")  # Виводимо папку синім кольором з додаванням символу "/" після назви 
            visualize_directory_structure(entry, indent + "    ")  # Рекурсивно обробляємо вкладену папку
        else:
            print(f"{indent}{Fore.GREEN}{entry.name}{Style.RESET_ALL}")  # Виводимо файл зеленим кольором

def main():
    init(autoreset=True)  # Ініціалізуємо colorama для автоматичного скидання кольорів

    # Перевіряємо, чи передано шлях до директорії у командному рядку
    if len(sys.argv) != 2:
        print(f"Використання: python {sys.argv[0]} /шлях/до/директорії")
        sys.exit(1)

    directory_path = Path(sys.argv[1])  # Отримуємо шлях до директорії

    # Перевіряємо, чи існує цей шлях і чи є він директорією
    if not directory_path.exists() or not directory_path.is_dir():
        print(f"Помилка: {directory_path} не є валідною директорією.")
        sys.exit(1)

    # Виводимо назву кореневої директорії
    print(f"{Fore.BLUE}{directory_path.resolve()}{Style.RESET_ALL}")
    visualize_directory_structure(directory_path)  # Викликаємо функцію для виведення структури

if __name__ == "__main__":
    main()