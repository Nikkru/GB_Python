# Get value of a Number
Get value of a Number - это телеграм-бот для поиска культурно-исторического значения того или иного числа.
Он отсылает пользовательский запрос на интернет-ресурс ![NUMBERSAPI](http://numbersapi.com/).
Демонстрирует полученный ответ, случайно выбранный из списка возможных. ![](request_response_telegram_bot.jpg)
### Для локального запуска бота выполнить слудующие действия:
```
pip install telebot
pip install PyTelegramBotAPI==2.2.3
pip install PyTelegramBotAPI==3.6.7
```
в файле get_number_value.py в 10-ой строчке переменной API_TOKEN присвоить значение ключа, полученного от BotFather
```
API_TOKEN = 'Апи ключ, который вы получили у BotFather'
```
### Запуск
Чтобы запустить бота, выполните в консоли:
```
python3 get_number_value.py
```

