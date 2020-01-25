# -*- coding: utf-8 -*-
import telebot
import config
import random
from telebot import types
 
bot = telebot.TeleBot(config.TOKEN)
 
@bot.message_handler(commands=['start'])
def welcome(message):
    sti = open('static/welcome.webp', 'rb')
    bot.send_sticker(message.chat.id, sti)
 
    # keyboard
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("🎲 Рандомное число")
    item2 = types.KeyboardButton("ФИО")
    item3 = types.KeyboardButton("Номер телефона")
    item4 = types.KeyboardButton("Биометрия")
 
    markup.add(item1, item2, item3, item4)
 
    bot.send_message(message.chat.id, "Добро пожаловать, {0.first_name}!\nЯ - <b>{1.first_name}</b>, бот созданный чтобы помочь нарыть информацию о человеке.".format(message.from_user, bot.get_me()),
        parse_mode='html', reply_markup=markup)
 
@bot.message_handler(content_types=['text'])
def lalala(message):
    if message.chat.type == 'private':
        if message.text == '🎲 Рандомное число':
            bot.send_message(message.chat.id, str(random.randint(0,100)))
        elif message.text == 'ФИО':
 
            markup = types.InlineKeyboardMarkup(row_width=2)
            item1 = types.InlineKeyboardButton("Россия", callback_data='rus')
            item2 = types.InlineKeyboardButton("Другая страна", callback_data='grad')
 
            markup.add(item1, item2)
 
            bot.send_message(message.chat.id, 'Подскажи свою страну', reply_markup=markup)
        elif message.text == 'Номер телефона':
        	bot.send_message(message.chat.id, ' 1. @Smart_SearchBot — найдет ФИО, дату рождения и адрес\n2. @SafeCallsBot — бесплатные анонимные звонки на любой номер телефона с подменой Caller ID\n3. @mailsearchbot — найдет часть пароля\n4. @AvinfoBot – делает отчет где есть данные из социальных сетей, недвижимости, автомобилей, объявлений и телефонных книжек. Нужно приглачить другой аккаунт для отчета\n5. getcontact.com (r) — найдет информацию о том как записан номер в контактах\n6. @get_kontakt_bot — найдет как записан номер в контактах, дает результаты что и getcontact\n7. https://github.com/sundowndev/PhoneInfoga\n8. truecaller.com (r) — телефонная книга, найдет имя и оператора телефона\n9. mirror.bullshit.agency — поиск объявлений по номеру телефона\n10. bases-brothers.ru — поиск номера в объявлениях\n11. account.live.com — проверка привязанности номера к microsoft аккаунту\n12. avinfo.guru — проверка телефона владельца авто, иногда нужен VPN\n13. telefon.stop-list.info — поиск по всем фронтам, иногда нет информации\n14. @numberPhoneBot — найдет адрес и ФИО, не всегда находит\n15. zytely.rosfirm.info — найдет ФИО, адрес прописки и дату рождения, нужно знать город\n17. @TlgrmChckBot — краткая информация об операторе телефона и ссылка на аккаунт в Telegram если он есть\n18. nuga.app (r) — найдет Instagram аккаунт, авторизация через Google аккаунт и всего 1 попытка\n19. @MyGenisBot — найдет имя и фамилию владельца номера ')
        elif message.text == 'Биометрия':
        	bot.send_message(message.chat.id, '1. Findclone.ru (r) — поиск по базе из VK\n2. @AvinfoBot — найдет аккаунты в ВК, содержащие фотографии с лицом, просто пришлите ему фото с лицом\n3. pimeyes.com — индексирует фото с сайтов, не точен, ограниченные возможности\n4. vk.watch — поиск по базе из VK, не точен\n5. @Falcone_FaceID_bot —находит фото в ВК, только 1 бесплатный скан\n6. search4faces.com — поиск по базам лиц VK и OK. Не точен\n7. @face_detect_bot — находит человека в VK и дает ссылку на аккаунт вместе с краткой информацией об этом человеке')
        else:
            bot.send_message(message.chat.id, 'Я не знаю что ответить 😢')
 
@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    try:
        if call.message:
            if call.data == 'rus':
            	bot.send_message(call.message.chat.id, ' 1. @egrul_bot — найдет ИП и компании\n2. yandex.people http://yandex.ru/people — поиск по социальным сетям\n3. reestr-zalogov.ru — поиск по залогодателям, даст паспортные данные, место и дату рождения и т.д.\n4. zytely.rosfirm.info — найдет адрес прописки и дату рождения, необходимо знать город\n5. mmnt.ru — найдет упоминания в документах\n6. kad.arbitr.ru — дела, рассматриваемые арбитражными судами\n7. bankrot.fedresurs.ru — поиск по банкротам, можно узнать ИНН, СНИЛС и адрес\n8. sudact.ru — судебные и нормативные акты РФ, поиск по участникам и судам\n9. nomer.center — телефонный справочник, иногда нужен VPN\n10. spra.vkaru.net — телефонный справочник по России, Украине, Белоруссии, Казахстану, Литве и Молдове\n11. http://fssprus.ru/iss/ip/ — проверка задолженностей, для физ. лица\n12. fio.stop-list.info — поиск по ИП и судам, если есть ИНН, то можно узнать больше\n13. gcourts.ru — поиск решений судов общей юрисдикции\n14. service.nalog.ru https://service.nalog.ru/inn.do — найдет ИНН, нужно знать полное ФИО, дату рождения и документ удостоверяющий личность ')
            elif call.data == 'grad':
                bot.send_message(call.message.chat.id, 'Сори, ток рашка')
 
            # remove inline buttons
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Хм...",
                reply_markup=None)
 
            # show alert
            bot.answer_callback_query(callback_query_id=call.id, show_alert=False,
                text="by DENUWALL")
 
    except Exception as e:
        print(repr(e))
 
# RUN
bot.polling(none_stop=True)