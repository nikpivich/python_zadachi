import subprocess

# Замените 'путь_к_программе' на полный путь к исполняемой программе, которую вы хотите запустить
put = r'C:\Users\pivic\PycharmProjects\python_zadachi/qwerty.py'

# C:\Users\pivic\PycharmProjects\python_zadachi

try:
    subprocess.run([put])
except FileNotFoundError:
    print(f"Ошибка: Файл {put} не найден.")
except Exception as e:
    print(f"Произошла ошибка: {e}")