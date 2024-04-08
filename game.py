import random 
a = random.randint(1, 100)
# Логирование 
i = 0
attemp = 0
live = 5
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
        
        
    