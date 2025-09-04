# Generator Squad Name Russia 🚀

**Генератор наименований отрядов специального назначения Российской Федерации**  
**A generator for names of Russian Federation special purpose units**

---

## Описание / Description 📝

🇷🇺 **Русский**:  
Этот проект предназначен для генерации наименований подразделений специального назначения на русском языке. Названия взяты из реальных подразделений специального назначения Российской Федерации всех ведомств. Проект начался как простой Python-скрипт, затем стал консольным приложением, а теперь — современное приложение с графическим интерфейсом! ✨

🇬🇧 **English**:  
This project is designed to generate names for special purpose units in Russian. The names are sourced from real special purpose units of the Russian Federation across all agencies. It started as a simple Python script, evolved into a console application, and is now a modern app with a graphical interface! ✨

---

## Версии / Versions 🗂️

### Версия 1.0 (Dec 29, 2022, 10:57 PM GMT+7) 🖥️
🇷🇺 **Русский**:  
- Первая версия проекта, созданная как тестовый Python-скрипт.  
- Простой `main.py`, читающий названия из файла `squad.txt`.  
- Без интерактивного интерфейса, только базовая функциональность генерации названий.

🇬🇧 **English**:  
- The first version of the project, created as a test Python script.  
- A simple `main.py` that reads names from the `squad.txt` file.  
- No interactive interface, only basic name generation functionality.

### Версия 1.1 (Dec 30, 2022, 12:37 PM GMT+7) 📟
🇷🇺 **Русский**:  
- Переработана в консольное приложение, работающее через командную строку (cmd).  
- Читает названия из файла `squad.txt` и выводит случайное название по нажатию клавиши Enter.  
- Для выхода из программы нужно ввести `exit`.  
- Простая и удобная реализация для быстрого использования.

🇬🇧 **English**:  
- Reworked into a console application running via the command line (cmd).  
- Reads names from the `squad.txt` file and outputs a random name upon pressing Enter.  
- To exit the program, the user enters `exit`.  
- A simple and convenient implementation for quick use.

### Версия 1.2 (Sep 04, 2025, 9:10 PM GMT+7) 🌟
🇷🇺 **Русский**:  
- Переработана в современное приложение с графическим интерфейсом с использованием библиотеки CustomTkinter.  
- Добавлены следующие функции:  
  - Графический интерфейс с кнопками "Сгенерировать" и "Выход".  
  - Переключение между тёмной и светлой темой интерфейса.  
  - Копирование сгенерированного названия в буфер обмена по клику на текст.  
  - Защита от копирования начального текста ("Нажмите 'Сгенерировать'").  
- Улучшен дизайн: современный стиль, аккуратное расположение элементов.  
- Программа по-прежнему читает названия из файла `squad.txt`.  
- Создан `main.exe` с иконкой для удобного использования без установки Python.

🇬🇧 **English**:  
- Reworked into a modern application with a graphical interface using the CustomTkinter library.  
- Added the following features:  
  - Graphical interface with "Generate" and "Exit" buttons.  
  - Toggle between dark and light interface themes.  
  - Copy generated names to the clipboard by clicking the text.  
  - Prevents copying the initial text ("Press 'Generate'").  
- Improved design: modern style, clean layout of elements.  
- The program still reads names from the `squad.txt` file.  
- Created `main.exe` with an icon for convenient use without installing Python.

---

## Как использовать / How to Use 🛠️

### Требования / Requirements

🇷🇺 **Русский**: 
- **Для пользователей Python**:  
  - Python 3.12 или выше / Python 3.12 or higher.  
  - Установленная библиотека CustomTkinter (`pip install customtkinter`).  
  - Файл `squad.txt` в той же папке, что и `main.py`.  
- **Для обычных пользователей**:  
  - Файл `main.exe` и `squad.txt` в одной папке.  
  - Python устанавливать не нужно.

### Инструкции / Instructions
#### Вариант 1: Запуск через Python
1. Убедитесь, что файл `squad.txt` находится в той же папке, что и `main.py`.  
2. Установите CustomTkinter:  
   ```bash
   pip install customtkinter
   ```
3. Запустите программу:  
   ```bash
   python main.py
   ```

#### Вариант 2: Запуск через .exe
1. Убедитесь, что файл `squad.txt` находится в той же папке, что и `main.exe`.  
2. Дважды щёлкните по `main.exe` для запуска программы.  

#### Использование
- Нажимайте кнопку "Сгенерировать" для получения случайного названия.  
- Кликните на название, чтобы скопировать его в буфер обмена.  
- Используйте переключатель для смены темы (тёмная/светлая).  
- Нажмите "Выход" для закрытия программы.  

🇬🇧 **English**:  
#### Option 1: Run via Python
1. Ensure the `squad.txt` file is in the same folder as `main.py`.  
2. Install CustomTkinter:  
   ```bash
   pip install customtkinter
   ```
3. Run the program:  
   ```bash
   python main.py
   ```

#### Option 2: Run via .exe
1. Ensure the `squad.txt` file is in the same folder as `main.exe`.  
2. Double-click `main.exe` to launch the program.  

#### Usage
- Click the "Generate" button to get a random name.  
- Click the name to copy it to the clipboard.  
- Use the switch to toggle between dark and light themes.  
- Click "Exit" to close the program.

---

## Планы на будущее / Future Plans 🔮

🇷🇺 **Русский**: 
- Добавить возможность сохранения избранных названий.  
- Добавить фильтрацию названий по ключевым словам.  
- Поддержка дополнительных языков для названий.  

🇬🇧 **English**:  
- Add the ability to save favorite names.  
- Add filtering of names by keywords.  
- Support for additional languages for names.

---

## Автор / Author 👨‍💻

🇷🇺 **Русский**:  
Создано Omonik. Связаться со мной можно через [GitHub](https://github.com/omonik).  

🇬🇧 **English**:  
Created by Omonik. Contact me via [GitHub](https://github.com/omonik).

---

✨ **Спасибо за использование программы! Надеюсь, она принесёт вам вдохновение!**  
✨ **Thank you for using the program! I hope it brings you inspiration!**