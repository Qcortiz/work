from tkinter import *
import random

# Инициализация переменных
complexity = 0
a = 0
attemp = 0
live = 5

# Функция для обработки ввода пользователя
def check_guess():
    global attemp, live
    guess = int(entry_box.get())
    attemp += 1

    if guess == a:
        result_label.config(text='Ты выиграл, количество попыток: ' + str(attemp))
    elif guess > a:
        result_label.config(text='Мое число меньше твоего, попробуй снова')
        live -= 1
        lives_label.config(text='Жизней осталось: ' + str(live))
    elif guess < a:
        result_label.config(text='Мое число больше твоего, попробуй снова')
        live -= 1
        lives_label.config(text='Жизней осталось: ' + str(live))

    if live == 0:
        result_label.config(text='Ты проиграл, игра окончена')

# Функция для начала новой игры
def new_game():
    global complexity, a, attemp, live
    attemp = 0
    live = 5

    complexity = int(complexity_var.get())
    if complexity == 1:
        a = random.randint(1, 10)
    elif complexity == 2:
        a = random.randint(1, 50)
    elif complexity == 3:
        a = random.randint(1, 100)

    lives_label.config(text='Жизней осталось: ' + str(live))
    result_label.config(text='')

# Создание окна
root = Tk()
root.title('Угадай число')
root.geometry('800x600')
root.resizable(width=False, height=False)

root.configure(background='#F0F0F0')

# Создание виджетов
complexity_var = StringVar()
complexity_var.set('1')  # Значение по умолчанию

difficulty_label = Label(root, text='Выберите сложность:', bg='#F0F0F0', font=('Arial', 12))
difficulty_label.pack()

easy_radio = Radiobutton(root, text='Легкая', variable=complexity_var, value='1', bg='#F0F0F0', font=('Arial', 10))
easy_radio.pack()
medium_radio = Radiobutton(root, text='Средняя', variable=complexity_var, value='2', bg='#F0F0F0', font=('Arial', 10))
medium_radio.pack()
hard_radio = Radiobutton(root, text='Сложная', variable=complexity_var, value='3', bg='#F0F0F0', font=('Arial', 10))
hard_radio.pack()

start_button = Button(root, text='Начать игру', command=new_game, bg='#FFD700', font=('Arial', 12))
start_button.pack(pady=10)

entry_box = Entry(root, width=15, font=('Arial', 12))
entry_box.pack(pady=10)

check_button = Button(root, text='Проверить', command=check_guess, bg='#FFD700', font=('Arial', 12))
check_button.pack(pady=10)

result_label = Label(root, text='', bg='#F0F0F0', font=('Arial', 12))
result_label.pack(pady=10)

lives_label = Label(root, text='', bg='#F0F0F0', font=('Arial', 12))
lives_label.pack(pady=10)

root.mainloop()
    