import tkinter as tk
from tkinter import ttk
import inspect

# Глобальные переменные для демонстрации
a = 123
b = "abc"
c = 3.1415

# Игнорируемые атрибуты и переменные
ignored_attributes = ['__loader__', '__spec__', '__builtins__']


def get_variables():
    # Получаем текущие локальные и глобальные переменные
    frame = inspect.currentframe().f_back
    local_vars = frame.f_locals
    global_vars = frame.f_globals

    # Очищаем текстовое поле от предыдущего содержимого
    text.delete(1.0, tk.END)

    # Выводим значения локальных переменных
    text.insert(tk.END, "Локальные переменные:\n")
    for var_name, var_value in local_vars.items():
        if not is_ignored(var_name):
            text.insert(tk.END, f"{var_name}: {var_value}\n")

    # Выводим значения глобальных переменных
    text.insert(tk.END, "\nГлобальные переменные:\n")
    for var_name, var_value in global_vars.items():
        if not is_ignored(var_name):
            text.insert(tk.END, f"{var_name}: {var_value}\n")


def is_ignored(var_name):
    # Проверяем, является ли переменная или её атрибут игнорируемым
    if var_name.startswith("__") and var_name.endswith("__"):
        return True
    if var_name in ignored_attributes:
        return True
    return False


# Создаем основное окно
root = tk.Tk()
root.title("Отладка переменных")
root.geometry("600x400")  # Устанавливаем размер окна

# Создаем текстовое поле для вывода переменных
text = tk.Text(root, wrap=tk.WORD, width=80, height=20)
text.pack(padx=10, pady=10)

# Создаем кнопку для получения переменных
button_get = ttk.Button(root, text="Получить переменные", command=get_variables)
button_get.pack(pady=10)

# Запускаем главный цикл обработки событий
root.mainloop()
