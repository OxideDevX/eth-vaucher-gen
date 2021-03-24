# ETH vaucher generator
***Привет. Данный проект создан кодером OxideDevX(Pentester). Telegram: @pwntt .***

*Что это такое?*
Генератор ETH чеков. 
По своему функционалу идентичен вот этому скрпиту(link дальше по курсу), только генерит чеки ЕТН https://github.com/OxideDevX/btc-vaucher-bruter.git
Скрипт генерирует ссылки для обнала ETH чеков в боте @ETH_CHANGE_BOT
Генерируем ссылки и переходим по ним, если повезет обналичиваем чек.
Для работы нужен ПК либо сервер под управлением ОС Linux.
Как установить: 

    apt update -y && apt upgrade -y

    apt install git python -y

    pip install requests

Скачиваем сам скрипт:

    git clone https://github.com/OxideDevX/eth-vaucher-gen/

    cd ETHVoucherGen

Запускаем скрипт командой:

    python ETHCheckGen.py

Далее запустится скрипт, и начнет генерировать ссылки.
Если все сделали правильно то скрипт сгенерирует вам ссылки такого типа:
    https://t.me/ETH_CHANGE_BOT?start=b_6aAjgfhfjhdg4754BLa6aZIFedRlvcET5Ea1N5
Удачи в поисках!