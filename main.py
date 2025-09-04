import random
import customtkinter as ctk
import tkinter as tk
from tkinter import messagebox

# Чтение названий из файла squad.txt
def load_squad_names():
    try:
        with open('squad.txt', encoding='utf-8') as file:
            return [line.strip() for line in file]
    except FileNotFoundError:
        messagebox.showerror("Ошибка", "Файл squad.txt не найден!")
        return []

# Функция для генерации случайного названия
def generate_squad_name():
    if idea:
        squad_name = random.choice(idea)
        name_label.configure(text=squad_name)
        name_label.can_copy = True  # Разрешаем копирование
    else:
        name_label.configure(text="Список названий пуст!")
        name_label.can_copy = False  # Запрещаем копирование

# Функция для копирования текста в буфер обмена
def copy_to_clipboard(event):
    if hasattr(name_label, 'can_copy') and name_label.can_copy:
        root.clipboard_clear()
        root.clipboard_append(name_label.cget("text"))
        messagebox.showinfo("Успех", "Название скопировано в буфер обмена!")

# Функция для переключения темы
def toggle_theme():
    theme = "light" if theme_switch.get() else "dark"
    ctk.set_appearance_mode(theme)
    theme_switch.configure(text="Тёмная тема" if theme == "light" else "Светлая тема")

# Создание основного окна
ctk.set_appearance_mode("dark")  # Тёмная тема по умолчанию
ctk.set_default_color_theme("blue")  # Синяя цветовая схема

root = ctk.CTk()
root.title("Генератор наименований отряда")
root.geometry("400x300")
root.resizable(False, False)  # Запрет изменения размера окна

# Загрузка названий
idea = load_squad_names()

# Создание элементов интерфейса
title_label = ctk.CTkLabel(master=root, text="Генератор названий отрядов", font=("Arial", 20))
title_label.pack(pady=20)

name_label = ctk.CTkLabel(master=root, text="Нажмите 'Сгенерировать'", font=("Arial", 16))
name_label.can_copy = False  # Запрещаем копирование начального текста
name_label.bind("<Button-1>", copy_to_clipboard)  # Привязываем клик для копирования
name_label.pack(pady=20)

generate_button = ctk.CTkButton(master=root, text="Сгенерировать", command=generate_squad_name)
generate_button.pack(pady=10)

exit_button = ctk.CTkButton(master=root, text="Выход", command=root.quit)
exit_button.pack(pady=10)

# Переключатель темы
theme_switch = ctk.CTkSwitch(master=root, text="Светлая тема", command=toggle_theme)
theme_switch.pack(pady=10)

# Запуск основного цикла
root.mainloop()