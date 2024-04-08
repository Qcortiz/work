import random 
from tkinter import *

root = Tk()
root.title('Игрра "Угадай число" ')
root.geometry('800x600')
root.resizable(width=False, height=False)

root.mainloop()



complexity = 0
a = 0
# Логирование 
i = 0
attemp = 0
live = 5
complexity = int(input('выберите сложность 1 - легкая. 2 - средняя. 3 - сложная: '))
if complexity == 1:
    a = random.randint(1, 10)
elif complexity == 2:
    a = random.randint(1, 50)
elif complexity == 3:
    a = random.randint(1, 100)
while True:
    
    i = int(input('ваша догадка: '))

    if i == a:
        print('Ты выйграл, твое число попыток\n' + str(attemp))
        break 
    elif i>a:
        print('мое число меньше твоего, попробуй снова')
        attemp += 1
        live -= 1
        print ('\n жизний осталось: ' + str(live))
    elif i<a:
        print('мое число больше твоего, попробуй снова')
        attemp += 1
        live -= 1
        print ('\n жизний осталось: ' + str(live))
    if live == 0: 
        print('ты проиграл, игра окончена')
        break 
        
        
    