import telebot
from telebot import types
from bs4 import BeautifulSoup as b
import requests

#Запуск бота

# 5860392992:AAG-ePrvCUDtb6ZL6bJAUVMVx04l5hXofs4
bot = telebot.TeleBot("5860392992:AAG-ePrvCUDtb6ZL6bJAUVMVx04l5hXofs4")
URL = 'https://bms.it-tv.org/stat/index.php?p=message'
r = requests.get(URL)
soup = b(r.text, 'html parser')
news = soup.find_all('span', style_='#text')
print(news)



@bot.message_handler(commands=['start'])
def start(message):
	markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
	item1 = types.KeyboardButton('Контакти📞')
	item2 = types.KeyboardButton('Тарифи🤑')
	item3 = types.KeyboardButton('Оплата тарифу💳')
	item4 = types.KeyboardButton('Перейти на сайт📲')

	markup.add(item1, item2, item3, item4)

	bot.send_message(message.chat.id, 'Вітаю, {0.first_name}, Оберіть послугу для подальшої роботи в боті!'.format(message.from_user), reply_markup = markup)

#Початкова клавіатура

@bot.message_handler(func=lambda message: True)
def get_text(message):
	#if message.chat.type == 'private:':
	if message.text == 'Контакти📞':
		bot.reply_to(message,'Підключення і тарифи 24/7 \n (044) 364-8888, (093) 170-1218 \n Підтримка ТБ і оплати 24/7 \n (044) 586-4411, (093) 170-1216 \n Тех.підтримка Інтернет 24/7 \n (044) 364-4955, (093) 170-1219')

	elif message.text == 'Оплата тарифу💳':
		bot.send_message(message.chat.id, 'https://www.ipay.ua/ua/bills/oplata-informacionnye-tehnologii')

	elif message.text == 'Перейти на сайт📲':
		bot.send_message(message.chat.id, 'https://www.it-tv.org/ua/complex')


	elif message.text == 'Тарифи🤑':
		foto1 = open(r'C:\Users\ViP/Desktop\ITbot\foto1.jpg', 'rb')
		foto2 = open(r'C:\Users\ViP\Desktop\ITbot\foto2.jpg', 'rb')
		foto3 = open(r'C:\Users\ViP\Desktop\ITbot\foto3.jpg', 'rb')
		foto4 = open(r'C:\Users\ViP\Desktop\ITbot\foto4.jpg', 'rb')
		bot.send_photo(message.chat.id, photo=foto1)
		bot.send_photo(message.chat.id, photo=foto2)
		bot.send_photo(message.chat.id, photo=foto3)
		bot.send_photo(message.chat.id, photo=foto4)
		bot.send_message(message.chat.id, 'Залишити заявку на підключення можна на сайті - https://www.it-tv.org/ua/complex')

	#Команди які не використовуються

	elif message.text == 'Назад⬅':
		markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
		item1 = types.KeyboardButton('Контакти📞')
		item2 = types.KeyboardButton('Тарифи🤑')
		item3 = types.KeyboardButton('Оплата тарифу💳')
		item4 = types.KeyboardButton('Перейти на сайт📲')
		markup.add(item1, item2, item3, item4)
		bot.send_message(message.chat.id, 'Назад⬅')

	elif message.text == 'оплата рахунку через iPay - VISA/MasterCard':
		bot.send_message(message.chat.id, 'https://www.ipay.ua/ua/bills/oplata-informacionnye-tehnologii')

	elif message.text == 'оплата рахунку через FONDY.eu - Приват24':
		bot.send_message(message.chat.id, 'Цей спосіб поповнення тимчасово не доступний. Приносимо вибачення за незручності.')

	elif message.text == 'оплата рахунку через FONDY.eu - VISA/MasterCard':
		bot.send_message(message.chat.id, 'Цей спосіб поповнення тимчасово не доступний. Приносимо вибачення за незручності.')

#Інші команди

@bot.message_handler(func=lambda message: True)
def get_text (message):
	if message.text == '':
		bot.reply_to(message, "")


bot.polling(none_stop=True)
