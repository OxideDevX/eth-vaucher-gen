#ммпортируем библиотеку
import random

print(' ')
print('////////OxideDevX привевствует вас!')
print('......[ ETHCheckGen 2.0 ]......')
print('Генератор чеков для Telegram bot @ETH_CHANGE_BOT')
print('Разработчик: t.me/hassenso_kardotto')
print(' ')
print('......[ ETHCheckGen 2.0 ]......')
print(' ')
chars = 'abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'
number = input('◾ Укажите желаемое количество ссылок для генерации:'+ "\n")
print(' ')
length = input('◾ Укажите длинну чека (рекомендованое значение 32):'+ "\n")
print(' ')
number = int(number)
length = int(length)
print(' ')
print('ВНИМАНИЕ! Работа скрипта успешно завершена: ', number, ' чеков сгенерировано.')
print('ВНИМАНИЕ: Скрипт генерирует рандомные чеки, проверять на валидность придется вручную.')
print('На данный момент ведуться работы по реализации автоматической валидации чеков')
print(' ')
for n in range(number):
    password =''
    for i in range(length):
        password += random.choice(chars)
# общую ссылку не менять, ибо чеки приниматься не будут! 
# где password: сгенерированный нами массив данных
    print('https://t.me/ETH_CHANGE_BOT?start=b_',password)
print(' ')
print('➕ Удачного поиска! :) ')
print()
toexit = input("[ETHCheckGen] ⚠️ Нажмите любую клавишу для завершения работы. Хорошего дня!")
