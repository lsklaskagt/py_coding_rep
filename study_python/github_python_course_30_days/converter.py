def celsius_to_fahrenheit(temp):
    return temp * 9 / 5 + 32

if __name__ == "__main__":
    # Выполнится только при прямом запуске converter.py
    print("Тест 0°C ->", celsius_to_fahrenheit(0))  # 32.0
    print("Тест 100°C ->", celsius_to_fahrenheit(100))  # 212.0

# Переменная __name__ — это встроенная переменная Python, которая показывает, в каком контексте исполняется файл:
# Если файл запущен напрямую (например через терминал python converter.py), Python автоматически присваивает переменной __name__ значение "__main__".
# Если файл импортирован в другой скрипт (например, в main.py написано import converter), Python присваивает переменной __name__ имя самого модуля — "converter".