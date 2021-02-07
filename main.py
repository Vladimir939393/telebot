#-*-coding: utf-8-*-

import telebot
import sys
import settings
import menu
import config
import time
from telebot import types

def start_bot():

    bot = telebot.TeleBot(config.bot_token)

    @bot.message_handler(commands=['start'])
    def start_message(message):
     bot.send_message(message.chat.id, settings.start_text.format(firstname = message.chat.first_name))
     bot.send_message(message.chat.id, " 📃 Выберите пункт в меню: 📃", reply_markup=menu.start_menu)
     print ("Бота запустил пользователь",message.chat.username)

    @bot.message_handler(content_types=["text"])
    def next_menu(message):
         userid = message.chat.id
         if message.text in menu.rayon_list:
            settings.rayondict[userid] = message.text
            bot.send_message(message.chat.id, "🗣 Выберите необходимую категорию: ", reply_markup=menu.kategorii_menu)
            print("Пользователь",message.chat.username, "выбрал район")
         if message.text in menu.tovar_list:
             print("Пользователь",message.chat.username, "выбрал товар и находится в меню оплаты")
             userid = message.chat.id
             settings.tovardict[userid] = message.text
             settings.pricedict[userid] = menu.tovar_list[message.text]
             buy_text = f"🔺 Чтобы получить координаты/фото " \
               "товара - Совершите платёж на QIWI или BTC\n" \
               "〰️〰️〰️〰️〰️〰️〰️〰️〰️〰️\n" \
               f"🏷️QIWI кошелек: {config.qiwi_number} \n" \
               f"💲Сумма к оплате: {settings.pricedict[userid]} рублей\n" \
               "💬Комментарий к платежу: 11612 \n" \
               "〰️〰️〰️〰️〰️〰️〰️〰️〰️〰️ \n" \
               f"🏷️КАРТА: 4890 4947 2683 5937 \n" \
               f"💲Сумма к оплате: {settings.pricedict[userid]} рублей\n" \
               "〰️〰️〰️〰️〰️〰️〰️〰️〰️〰️ \n" \
               "Ваша быстрая ссылка на оплату: \n" \
               f"https://qiwi.com/payment/form/99?extra%5B%27account%27%5D=79058949621&amountInteger={settings.pricedict[userid]}&amountFraction=0&extra%5B%27comment%27%5D=30612&currency=643&blocked[0]=account \n" \
               "〰️〰️〰️〰️〰️〰️〰️〰️〰️〰️ \n" \
               "🔻 Сумма платежа должна быть равна указаной или выше.\n" \
               "🔺 Платежи обрабатываются в автоматическом режиме.\n" \
               "〰️〰️〰️〰️〰️〰️〰️〰️〰️〰️ \n" \
               f"🔻 При оплате с Bitcoin, необходимо перевести сумму эквивалентную {settings.pricedict[userid]} рублям на зарезервированный для вас Bitcoin адрес:\n" \
               f"{config.bitcoin_adress}"
             bot.send_message(message.chat.id, buy_text, reply_markup=menu.buy_menu)
         if message.text == "📨 Информация 📨":
              bot.send_message(message.chat.id, settings.info_text, reply_markup=menu.help_menu)
         if message.text == "😍 Акции 😍":
              bot.send_message(message.chat.id, "Акции на данный момент: \n\n" \
             "🔘 Альфа-ПВП (0,2гр)  800p - 699р\n" \
             "🔘 Гашиш (1гр)  1̶2̶0̶0̶р - 1000р \n" \
             "🔘 Кокаин MQ (1гр)  4̶0̶0̶0̶р - 3850p  \n" \
             "🔘 Бутират (100 мл)  2̶2̶0̶0̶р - 1950р \n" \
             "🔘 Амфетамин (1гр)  1̶30̶0̶р - 1000p \n" \
             "🔘 Мефедрон (1гр)  1̶5̶0̶0̶р - 1300p \n" \
             "🔘 Мефедрон (3гр)  4̶0̶0̶0̶р - 3700р \n" \
             , reply_markup=menu.help_menu)
         if message.text == "❓ Как совершить покупку ❓":
              bot.send_message(message.chat.id, settings.help_text, reply_markup=menu.help_menu)
         if message.text == "🔙 Вернуться в меню 🔙":
              bot.send_message(message.chat.id, "Возвращаемся в меню...", reply_markup=menu.start_menu)
         if message.text == "🤑 Скидки 🤑":
              bot.send_message(message.chat.id, "🤑 Скидки 🤑 \n\n" \
              "〰️〰️〰️〰️〰️〰️〰️〰️ \n" \
              "В нашем боте работает скидочная система: \n" 
              "(Действует только при первой покупке) \n\n" \
              "1️⃣ При покупке товара/ов на сумму выше 1000 рублей, вы получаете 2% от стоимости товара на свой реферальный баланс \n\n" \
              "2️⃣ При покупке товара/ов на сумму выше 3000 рублей, вы получаете 8% от стоимости товара на свой реферальный баланс \n\n" \
              "3️⃣ При покупке товара/ов на сумму выше 5000 рублей, вы получаете 10% от стоимости товара на свой реферальный баланс \n\n" \
              "4️⃣ При покупке товара/ов на сумму выше 10000 рублей, вы получаете 14% от стоимости товара на свой реферальный баланс \n", reply_markup=menu.start_menu)
         if message.text == "🔙 Назад 🔙":
              bot.send_message(message.chat.id, "Возвращаемся к выбору категории...", reply_markup=menu.kategorii_menu)
         if message.text == "🔙 Вернуться к выбору товара 🔙":
              bot.send_message(message.chat.id, "🧪 Выберите категорию товара 🧪", reply_markup=menu.kategorii_menu)
         if message.text == "📦 Купить товар 📦":
              bot.send_message(message.chat.id, "🏙 Выберите город 🏙", reply_markup=menu.cities_menu)
         if message.text == "🔜 Перейти к выбору товара 🔜":
              bot.send_message(message.chat.id, "🧪 Выберите категорию товара 🧪", reply_markup=menu.kategorii_menu)
         if message.text == "🔙 Вернуться к выбору города 🔙":
              bot.send_message(message.chat.id, "🏙 Выберите город 🏙", reply_markup=menu.cities_menu)
         if message.text == "🔸 Москва 🔸":
              bot.send_message(message.chat.id, "🏢 Выберите район 🏢", reply_markup=menu.moscow_menu)
              settings.citydict[userid] = "🔸 Mосква 🔸"
              print("Пользователь",message.chat.username, "выбрал город Москва")
         if message.text == "🔸 Санкт-Петербург 🔸":
              bot.send_message(message.chat.id, "🏢 Выберите район 🏢", reply_markup=menu.spb_menu)
              settings.citydict[userid] = "🔸 Санкт-Петербург 🔸"
              print("Пользователь",message.chat.username, "выбрал город Санкт-Петербург")
         if message.text == "🔸 Тула 🔸":
              bot.send_message(message.chat.id, "🏢 Выберите район 🏢", reply_markup=menu.tula_menu)
              settings.citydict[userid] = "🔸 Тула 🔸"
              print("Пользователь",message.chat.username, "выбрал город Тула")
         if message.text == "🔸 Екатеринбург 🔸":
              bot.send_message(message.chat.id, "🏢 Выберите район 🏢", reply_markup=menu.ekb_menu)
              settings.citydict[userid] = "🔸 Екатеринбург 🔸"
              print("Пользователь",message.chat.username, "выбрал город Екатеринбург")
         if message.text == "🔸 Барнаул 🔸":
              bot.send_message(message.chat.id, "🏢 Выберите район 🏢", reply_markup=menu.barnaul_menu)
              settings.citydict[userid] = "🔸 Барнаул 🔸"
              print("Пользователь",message.chat.username, "выбрал город Барнаул")
         if message.text == "🔸 Томск 🔸":
              bot.send_message(message.chat.id, "🏢 Выберите район 🏢", reply_markup=menu.tomsk_menu)
              settings.citydict[userid] = "🔸 Томск 🔸"
              print("Пользователь",message.chat.username, "выбрал город Томск")
         if message.text == "🔸 Тюмень 🔸":
              bot.send_message(message.chat.id, "🏢 Выберите район 🏢", reply_markup=menu.tumen_menu)
              settings.citydict[userid] = "🔸 Тюмень 🔸"
              print("Пользователь",message.chat.username, "выбрал город Тюмень")
         if message.text == "🔸 Нижний Новгород 🔸":
              bot.send_message(message.chat.id, "🏢 Выберите район 🏢", reply_markup=menu.nn_menu)
              settings.citydict[userid] = "🔸 Нижний Новгород 🔸"
              print("Пользователь",message.chat.username, "выбрал город Нижний Новгород")
         if message.text == "🔸 Самара 🔸":
              bot.send_message(message.chat.id, "🏢 Выберите район🏢", reply_markup=menu.samara_menu)
              settings.citydict[userid] = "🔸 Самара 🔸"
              print("Пользователь",message.chat.username, "выбрал город Самара")
         if message.text == "🔸 Омск 🔸":
              bot.send_message(message.chat.id, "🏢 Выберите район ⬇️", reply_markup=menu.omsk_menu)
              settings.citydict[userid] = "🔸 Омск 🔸"
              print("Пользователь",message.chat.username, "выбрал город Омск")
         if message.text == "🔸 Саратов 🔸":
              bot.send_message(message.chat.id, "🏢 Выберите район 🏢", reply_markup=menu.saratov_menu)
              settings.citydict[userid] = "🔸  Саратов 🔸"
              print("Пользователь",message.chat.username, "выбрал город Саратов")
         if message.text == "🔸 Краснодар 🔸":
              bot.send_message(message.chat.id, "🏢 Выберите район 🏢", reply_markup=menu.krasnodar_menu)
              settings.citydict[userid] = "🔸 Краснодар 🔸"
              print("Пользователь",message.chat.username, "выбрал город Краснодар")
         if message.text == "🔸 Воронеж 🔸":
              bot.send_message(message.chat.id, "🏢 Выберите район 🏢", reply_markup=menu.voronej_menu)
              settings.citydict[userid] = "🔸 Воронеж 🔸"
              print("Пользователь",message.chat.username, "выбрал город Воронеж")
         if message.text == "🔸 Казань 🔸":
              bot.send_message(message.chat.id, "🏢 Выберите район 🏢", reply_markup=menu.kasan_menu)
              settings.citydict[userid] = "🔸 Казань 🔸"
              print("Пользователь",message.chat.username, "выбрал город Казань")
         if message.text == "🔸 Пермь 🔸":
              bot.send_message(message.chat.id, "🏢 Выберите район 🏢", reply_markup=menu.perm_menu)
              settings.citydict[userid] = "🔸 Пермь 🔸"
              print("Пользователь",message.chat.username, "выбрал город Пермь")
         if message.text == "🔸 Новосибирск 🔸":
              bot.send_message(message.chat.id, "🏢 Выберите район 🏢", reply_markup=menu.ns_menu)
              settings.citydict[userid] = "🔸 Новосибирск 🔸"
              print("Пользователь",message.chat.username, "выбрал город Новосибирск")
         if message.text == "🔸 Челябинск 🔸":
              bot.send_message(message.chat.id, "🏢 Выберите район 🏢", reply_markup=menu.chel_menu)
              settings.citydict[userid] = "🔸 Челябинск 🔸"
              print("Пользователь",message.chat.username, "выбрал город Челябинск")
         if message.text == "🔸 Иваново 🔸":
              bot.send_message(message.chat.id, "🏢 Выберите район 🏢", reply_markup=menu.iva_menu)
              settings.citydict[userid] = "🔸 Иваново 🔸"
              print("Пользователь",message.chat.username, "выбрал город Иваново")
         if message.text == "🔸 Волгоград 🔸":
              bot.send_message(message.chat.id, "🏢 Выберите район 🏢", reply_markup=menu.volga_menu)
              settings.citydict[userid] = "🔸 Волгоград 🔸"
              print("Пользователь",message.chat.username, "выбрал город Волгоград")
         if message.text == "🔸 Красноярск 🔸":
              bot.send_message(message.chat.id, "🏢 Выберите район 🏢", reply_markup=menu.krasno_menu)
              settings.citydict[userid] = "🔸 Красноярск 🔸"
              print("Пользователь",message.chat.username, "выбрал город Красноярск")
         if message.text == "🔸 Тольятти 🔸":
              bot.send_message(message.chat.id, "🏢 Выберите район 🏢", reply_markup=menu.tol_menu)
              settings.citydict[userid] = "🔸 Тольятти 🔸"
              print("Пользователь",message.chat.username, "выбрал город Тольятти")
         if message.text == "🔸 Уфа 🔸":
              bot.send_message(message.chat.id, "🏢 Выберите район 🏢", reply_markup=menu.ufa_menu)
              settings.citydict[userid] = "🔸 Уфа 🔸"
              print("Пользователь",message.chat.username, "выбрал город Уфа")
         if message.text == "🔸 Астрахань 🔸":
              bot.send_message(message.chat.id, "🏢 Выберите район 🏢", reply_markup=menu.astr_menu)
              settings.citydict[userid] = "🔸 Астрахань 🔸"
              print("Пользователь",message.chat.username, "выбрал город Астрахань")
         if message.text == "🔸 Великий Новгород 🔸":
             bot.send_message(message.chat.id, "🏢 Выберите район 🏢", reply_markup=menu.vn_menu)
             settings.citydict[userid] = "🔸 Великий Новгород 🔸"
             print("Пользователь", message.chat.username, "выбрал город Великий Новгород")
         if message.text == "🔸 Владивосток 🔸":
              bot.send_message(message.chat.id, "🏢 Выберите район 🏢", reply_markup=menu.vlad_menu)
              settings.citydict[userid] = "🔸 Владивосток 🔸"
              print("Пользователь",message.chat.username, "выбрал город Владивосток")
         if message.text == "🔸 Вологда 🔸":
              bot.send_message(message.chat.id, "🏢 Выберите район 🏢", reply_markup=menu.vologda_menu)
              settings.citydict[userid] = "🔸 Вологда 🔸"
              print("Пользователь",message.chat.username, "выбрал город Вологда")
         if message.text == "🔸 Ижевск 🔸":
              bot.send_message(message.chat.id, "🏢 Выберите район 🏢", reply_markup=menu.ijevsk_menu)
              settings.citydict[userid] = "🔸 Ижевск 🔸"
              print("Пользователь",message.chat.username, "выбрал город Ижевск")
         if message.text == "🔸 Йошкар-Ола 🔸":
              bot.send_message(message.chat.id, "🏢 Выберите район 🏢", reply_markup=menu.ioshka_menu)
              settings.citydict[userid] = "🔸 Йошкар-Ола 🔸"
              print("Пользователь",message.chat.username, "выбрал город Йошкар-Ола")
         if message.text == "🔸 Калининград 🔸":
              bot.send_message(message.chat.id, "🏢 Выберите район 🏢", reply_markup=menu.kalik_menu)
              settings.citydict[userid] = "🔸 Калининград 🔸"
              print("Пользователь",message.chat.username, "выбрал город Калининград")
         if message.text == "🔸 Калуга 🔸":
              bot.send_message(message.chat.id, "🏢 Выберите район 🏢", reply_markup=menu.kaluga_menu)
              settings.citydict[userid] = "🔸 Калуга 🔸"
              print("Пользователь",message.chat.username, "выбрал город Калуга")
         if message.text == "🔸 Кемерово 🔸":
              bot.send_message(message.chat.id, "🏢 Выберите район 🏢", reply_markup=menu.kemerovo_menu)
              settings.citydict[userid] = "🔸 Кемерово 🔸"
              print("Пользователь",message.chat.username, "выбрал город Кемерово")
         if message.text == "🔸 Киров 🔸":
              bot.send_message(message.chat.id, "🏢 Выберите район 🏢", reply_markup=menu.kirov_menu)
              settings.citydict[userid] = "🔸 Киров 🔸"
              print("Пользователь",message.chat.username, "выбрал город Киров")
         if message.text == "🔸 Курск 🔸":
              bot.send_message(message.chat.id, "🏢 Выберите район 🏢", reply_markup=menu.kursk_menu)
              settings.citydict[userid] = "🔸 Курск 🔸"
              print("Пользователь",message.chat.username, "выбрал город Курск")
         if message.text == "🔸 Мурманск 🔸":
              bot.send_message(message.chat.id, "🏢 Выберите район 🏢", reply_markup=menu.murmansk_menu)
              settings.citydict[userid] = "🔸 Мурманск 🔸"
              print("Пользователь",message.chat.username, "выбрал город Мурманск")
         if message.text == "🔸 Набережные челны 🔸":
              bot.send_message(message.chat.id, "🏢 Выберите район 🏢", reply_markup=menu.nc_menu)
              settings.citydict[userid] = "🔸 Набережные челны 🔸"
              print("Пользователь",message.chat.username, "выбрал город Набережные челны")
         if message.text == "🔸 Нижневартовск 🔸":
              bot.send_message(message.chat.id, "🏢 Выберите район 🏢", reply_markup=menu.nijnevatorsk_menu)
              settings.citydict[userid] = "🔸 Нижневартовск 🔸"
              print("Пользователь",message.chat.username, "выбрал город Нижневартовск")
         if message.text == "🔸 Новокузнецк 🔸":
              bot.send_message(message.chat.id, "🏢 Выберите район 🏢", reply_markup=menu.novokuzn_menu)
              settings.citydict[userid] = "🔸 Новокузнецк 🔸"
              print("Пользователь",message.chat.username, "выбрал город Новокузнецк")
         if message.text == "🔸 Оренбург 🔸":
              bot.send_message(message.chat.id, "🏢 Выберите район 🏢", reply_markup=menu.orenburg_menu)
              settings.citydict[userid] = "🔸 Оренбург 🔸"
              print("Пользователь",message.chat.username, "выбрал город Оренбург")
         if message.text == "🔸 Орел 🔸":
              bot.send_message(message.chat.id, "🏢 Выберите район 🏢", reply_markup=menu.orel_menu)
              settings.citydict[userid] = "🔸 Орел 🔸"
              print("Пользователь",message.chat.username, "выбрал город Орел")
         if message.text == "🔸 Пенза 🔸":
              bot.send_message(message.chat.id, "🏢 Выберите район 🏢", reply_markup=menu.penza_menu)
              settings.citydict[userid] = "🔸 Пенза 🔸"
              print("Пользователь",message.chat.username, "выбрал город Пенза")
         if message.text == "🔸 Ростов-на-Дону 🔸":
              bot.send_message(message.chat.id, "🏢 Выберите район 🏢", reply_markup=menu.rostov_menu)
              settings.citydict[userid] = "🔸 Ростов-на-Дону 🔸"
              print("Пользователь",message.chat.username, "выбрал город Ростов-на-Дону")
         if message.text == "🔸 Саранск 🔸":
              bot.send_message(message.chat.id, "🏢 Выберите район 🏢", reply_markup=menu.saransk_menu)
              settings.citydict[userid] = "🔸 Саранск 🔸"
              print("Пользователь",message.chat.username, "выбрал город Саранск")
         if message.text == "🔸 Ульяновск 🔸":
              bot.send_message(message.chat.id, "🏢 Выберите район 🏢", reply_markup=menu.ulyanovsk_menu)
              settings.citydict[userid] = "🔸 Ульяновск 🔸"
              print("Пользователь",message.chat.username, "выбрал город Ульяновск")
         if message.text == "🔸 Иркутск 🔸":
              bot.send_message(message.chat.id, "🏢 Выберите район 🏢", reply_markup=menu.irkutsk_menu)
              settings.citydict[userid] = "🔸 Иркутск 🔸"
              print("Пользователь",message.chat.username, "выбрал город Иркутск")
         if message.text == "🔸 Хабаровск 🔸":
              bot.send_message(message.chat.id, "🏢 Выберите район 🏢", reply_markup=menu.habarovsk_menu)
              settings.citydict[userid] = "🔸 Хабаровск 🔸"
              print("Пользователь",message.chat.username, "выбрал город Хабаровск")
         if message.text == "🔸 Ярославль 🔸":
              bot.send_message(message.chat.id, "🏢 Выберите район 🏢", reply_markup=menu.yaroslavl_menu)
              settings.citydict[userid] = "🔸 Ярославль 🔸"
              print("Пользователь",message.chat.username, "выбрал город Ярославль")
         if message.text == "🔸 Рязань 🔸":
              bot.send_message(message.chat.id, "🏢 Выберите район 🏢", reply_markup=menu.ryazan_menu)
              settings.citydict[userid] = "🔸 Рязань 🔸"
              print("Пользователь",message.chat.username, "выбрал город Рязань")
         if message.text == "🔸 Липецк 🔸":
             bot.send_message(message.chat.id, "🏢 Выберите район 🏢", reply_markup=menu.lipeck_menu)
             settings.citydict[userid] = "🔸 Липецк 🔸"
             print("Пользователь", message.chat.username, "выбрал город Липецк")
         if message.text == "🔸 Чебоксары 🔸":
              bot.send_message(message.chat.id, "🏢 Выберите район 🏢", reply_markup=menu.ceboksar_menu)
              settings.citydict[userid] = "🔸 Чебоксары 🔸"
              print("Пользователь",message.chat.username, "выбрал город Чебоксары")
         if message.text == "🔸 Ставрополь 🔸":
              bot.send_message(message.chat.id, "🏢 Выберите район 🏢", reply_markup=menu.stavropol_menu)
              settings.citydict[userid] = "🔸 Ставрополь 🔸"
              print("Пользователь",message.chat.username, "выбрал город Ставрополь")
         if message.text == "🔸 Севастополь 🔸":
              bot.send_message(message.chat.id, "🏢 Выберите район 🏢", reply_markup=menu.sevastopol_menu)
              settings.citydict[userid] = "🔸 Севастополь 🔸"
              print("Пользователь",message.chat.username, "выбрал город Севастополь")
         if message.text == "🔸 Сочи 🔸":
              bot.send_message(message.chat.id, "🏢 Выберите район 🏢", reply_markup=menu.soci_menu)
              settings.citydict[userid] = "🔸 Сочи 🔸"
              print("Пользователь",message.chat.username, "выбрал город Сочи")
         if message.text == "🔸 Тверь 🔸":
              bot.send_message(message.chat.id, "🏢 Выберите район 🏢", reply_markup=menu.tver_menu)
              settings.citydict[userid] = "🔸 Тверь 🔸"
              print("Пользователь",message.chat.username, "выбрал город Тверь")
         if message.text == "🔸 Брянск 🔸":
              bot.send_message(message.chat.id, "🏢 Выберите район 🏢", reply_markup=menu.bransk_menu)
              settings.citydict[userid] = "🔸 Брянск 🔸"
              print("Пользователь",message.chat.username, "выбрал город Брянск")
         if message.text == "🔸 Белгород 🔸":
              bot.send_message(message.chat.id, "🏢 Выберите район 🏢", reply_markup=menu.belgorod_menu)
              settings.citydict[userid] = "🔸 Белгород 🔸"
              print("Пользователь",message.chat.username, "выбрал город Белгород")
         if message.text == "🔸 Владиимр 🔸":
              bot.send_message(message.chat.id, "🏢 Выберите район 🏢", reply_markup=menu.vladimir_menu)
              settings.citydict[userid] = "🔸 Владиимр 🔸"
              print("Пользователь",message.chat.username, "выбрал город Владиимр")
         if message.text == "🔸 Чита 🔸":
              bot.send_message(message.chat.id, "🏢 Выберите район 🏢", reply_markup=menu.cida_menu)
              settings.citydict[userid] = "🔸 Чита 🔸"
              print("Пользователь",message.chat.username, "выбрал город Чита")
         if message.text == "🔸 Смоленск 🔸":
              bot.send_message(message.chat.id, "🏢 Выберите район 🏢", reply_markup=menu.smolensk_menu)
              settings.citydict[userid] = "🔸 Смоленск 🔸"
              print("Пользователь",message.chat.username, "выбрал город Смоленск")
         if message.text == "🔸 Якутск 🔸":
              bot.send_message(message.chat.id, "🏢 Выберите район 🏢", reply_markup=menu.yakutsk_menu)
              settings.citydict[userid] = "🔸 Якутск 🔸"
              print("Пользователь",message.chat.username, "выбрал город Якутск")
         if message.text == "🔸 Череповец 🔸":
              bot.send_message(message.chat.id, "🏢 Выберите район 🏢", reply_markup=menu.cerepovec_menu)
              settings.citydict[userid] = "🔸 Череповец 🔸"
              print("Пользователь",message.chat.username, "выбрал город Череповец")
         if message.text == "🔸 Тамбов 🔸":
              bot.send_message(message.chat.id, "🏢 Выберите район 🏢", reply_markup=menu.tambov_menu)
              settings.citydict[userid] = "🔸 Тамбов 🔸"
              print("Пользователь",message.chat.username, "выбрал город Тамбов")
         if message.text == "🔸 Петрозаводск 🔸":
              bot.send_message(message.chat.id, "🏢 Выберите район 🏢", reply_markup=menu.petrozavodsk_menu)
              settings.citydict[userid] = "🔸 Петрозаводск 🔸"
              print("Пользователь",message.chat.username, "выбрал город Петрозаводск")
         if message.text == "🔸 Абакан 🔸":
              bot.send_message(message.chat.id, "🏢 Выберите район 🏢", reply_markup=menu.abokan_menu)
              settings.citydict[userid] = "🔸 Абакан 🔸"
              print("Пользователь",message.chat.username, "выбрал город Абакан")
         if message.text == "🔸 Южно-Сахалинск 🔸":
              bot.send_message(message.chat.id, "🏢 Выберите район 🏢", reply_markup=menu.ysahal_menu)
              settings.citydict[userid] = "🔸 Южно-Сахалинск 🔸"
              print("Пользователь",message.chat.username, "выбрал город Южно-Сахалинск")
         if message.text == "🧮 Проверить оплату 🧮":
              bot.send_message(message.chat.id, "🔍 Идёт проверка платежа, пожалуйста, подождите...", reply_markup=menu.buy_menu)
              time.sleep(6)
              bot.send_message(message.chat.id, "❌ Платеж не найден. \n" \
              "Попробуйте ещё раз через несколько минут", reply_markup=menu.buy_menu)
              print("Пользователь",message.chat.username, "подтвердил оплату")
       
         if message.text == "👨‍👨‍👦 Реферальная система 👨‍👨‍👦":
              bot.send_message(message.chat.id, settings.ref_text.format(iduser = message.from_user.id), reply_markup=menu.start_menu)

           #drugs_kategorii
         if message.text == "🔸 Альфа-ПВП 🔸":
              bot.send_message(message.chat.id, "АЛЬФА PVP Crystal \n" \
              "\n" \
              "Психоактивное вещество со стимулирующими свойствами!\n" \
              "Это один из лучших видов товара как по качеству, так и по структуре.\n" \
              "Успейте попробовать и оценить качество.\n" \
              "Эффекты:\n" \
              "\n" \
              "Ярко выженная стимуляция, удовольствие от любого дела, которым ты бы не занялся.\n" \
              "Прекрасно подходит для монотонной работы.\n" \
              "Повышение коммуникабельности, сексуального желания, яркие волны эйфории.", reply_markup=menu.alfa_menu)
         if message.text == "🔸 Гашиш 🔸":
              bot.send_message(message.chat.id, "В наличии айс отличного качества этикетка Mclaren. Hа вид зелёно-коричневый, сильно пахнет шишками, полумягкий, липкий, не крошится ломится руками и идеально лепится, настоящее импортное добро класса AAA+. \n" \
              "\n" \
              "Эффект гибридный с уклоном в сативу, однозначно развеселит, плотно накурит и долго не отпустит. Удовольствие от всего - внешний вид, структура, аромат, вкус и конечно же трип. \n" \
              "Плитки почти ровные, есть и выше, говорит о том что гаш свежий и хранился правильно.\n", reply_markup=menu.gash_menu)
         if message.text == "🔸 Шишки АК-47 🔸":
              bot.send_message(message.chat.id, "Всеми любимый АК47\n" \
              "\n" \
              "Данный сорт не нуждается в описании, Вы его и так все знаете, \n" \
              "или как минимум слышали о нем и настал момент его попробовать! \n" \
              "Всегда только свежие поставки в Durman. В данном товаре вы не почувствуете  намека на прелость, недосушенность. \n" \
              "\n" \
              "Весь товар выращен на органике, пролечивался минимум месяц для идеального вкуса.", reply_markup=menu.shish_menu)
         if message.text == "🔸 Амфетамин 🔸":
              bot.send_message(message.chat.id, "Продукт импортного производства, изготовлен в Европейской Лаборатории под контролем по всем Стандартам качества! \n" \
                "\n" \
                "Обладает максимальной степенью очистки! \n" \

                "Высокая концентрация! \n" \

                "Цвет - Белый (основной), - Бело-розовый ,- Желтоватый! \n" \

                "Мощный и яркий эффект! \n" \

                "Без побочных последствий и тяжелых отходов!  \n" \
                "\n" \
                "Эффект достигается даже при небольшой дозировке: \n" \
                "\n" \
                "- ускоряет мыслительные процессы; \n" \
                "- повышает работоспособность и мотивацию; \n" \
                "- умеренная эйфория; \n" \
                "\n" \
                "Способы применения: \n" \

                "1. Интраназальный – максимально быстрый эффект. \n" \

                "2. Пероральный – более долгий период воздействия.\n" , reply_markup=menu.amf_menu)
         if message.text == "🔸 Мефедрон 🔸":
              bot.send_message(message.chat.id, "Многолетний опыт и стремление сделать лучший продукт в своей категории дали результат, и этот результат перед тобой. Сухая, и такая эйфоричная! \n" \
                "\n" \
               "Лучшее качество в своей категории. Наша мука даст фору многим кристаллам, не веришь? Попробуй и убедись в этом сам!", reply_markup=menu.mef_menu)
         if message.text == "🔸 МДМА 🔸":
              bot.send_message(message.chat.id, "Шедевр эйфорической алхимии. Настоящая находка для ценителя и неутомимого покорителя вершин наслаждения. \n" \
                "\n" \
                "Магическое сплетение молекул этого продукта наполняет душу радостью и заставляет сердца биться быстрее. Перед Вами МДМА высшей категории, синтезированный мастерами своего дела из самых качественных компонентов. \n" \
                "Вы получите радость и тепло даже от небольшой крупинки. Кристаллы от Durman поражают своей многогранностью и постепенно раскрывается все новыми красками на протяжении всего сеанса. \n" \
                "\n" \
                "Вы чувствуете интенсивную неземную эйфорию и непреодолимое желание двигаться. Абсолютный экстаз и наслаждение. \n" \
                "\n" \
                "Кристаллы очень сильные, поэтому будьте внимательны при расчёте своей нормы. 1.2 - 1.5мг МДМА на 1кг Вашей массы.", reply_markup=menu.mdma_menu)
         if message.text == "🔸 Кокаин 🔸":
              bot.send_message(message.chat.id, "Легендарный кокаин, импортированный из Колумбии , который успел полюбиться покупателям за свое премиальное качество и приемлемую цену.\n" \
                "\n" \
                "Высокое качество + мощное действие + минимум побочных эффектов = Кокаин HQ." "\n" \
                "\n" \
                "Этот чистейший стафф дает приятную эйфорию и сильную стимуляцию, которая позволит вам почувствовать себя властелином этой вселенной.\n" \
                "\n" \
                "Главное знать меру и не перебарщивать, дабы не потерять всю космическую магию вещества.  Употребление: интраназально – 50-80 мг \n" \
                "\n" \
                "Плавный стимулирующий и эйфоричный эффект. \n" \
                "Морозит в меру. \n" \
                "Не раздражает слизистую. \n" \
                "Без депрессивных остаточных ощущений.\n" , reply_markup=menu.koka_menu)
         if message.text == "🔸 Мефедрон 🔸":
              bot.send_message(message.chat.id, "Употребляется перорально, интраназально. \n" \
              "Перорально: \n" \
              "Средняя дозировка 200-350 мг. \n" \
              "Продолжительность действия 1-3 часа. \n" \
            "\n" \
              "Интраназально: \n" \
              "Средняя дозировка 100-250 мг. \n" \
              "Продолжительность действия 40-90 минут. \n" \
              "\n" \
              "Кристаллическая форма \n" \
              "\n" \
              "Эффекты: \n" \
              "•Эйфория, удовлетворение, радость  \n" \
              "•Стимуляция, прилив сил, энергии (большая, по сравнению с MDMA)  \n" \
              "•Ускорение мыслительных процессов, расширение когнитивной функции  \n" \
              "•Эмпатия, повышение коммуникабельности, общительность (меньшая, по сравнению с MDMA)  \n" \
              "•Ощущение ускорения хода времени  \n" \
              "•Расширение зрачков  \n" \
              "•Повышение потоотделения, секреции  \n" \
              "•Изменение тактильных ощущений, появление легкости тела \n" , reply_markup=menu.mef_menu)
         if message.text == "🔸 LSD 🔸":
              bot.send_message(message.chat.id, "Первое, что хочется сказать, многие, кто употреблял данную дозировку, находили ответы на все интересующие себя вопросы, погружались вглубь своего сознания и далеко за его пределы! \n" \
              "Большинство описывают это состояние, как знакомство с Богом, познание Вселенной! \n" \
              "Кто-то после трипа бросал пагубные привычки и находил для себя правильную дорогу в жизни! \n" \
              "Если Вы уверенны в себе, своих силах и устойчивости психики, то несомненно, эта волшебная бумажка именно для Вас! \n" \
              "Остается только пожелать Вам прекрасного путешествия", reply_markup=menu.lsd_menu)
         if message.text == "🔸 Метамфетамин 🔸":
              bot.send_message(message.chat.id, "Высококачественный, настоящий метамфетамин рацемат. \n" \
              "\n" \
              "Эффекты: стимуляция и эйфория, что-то среднее между амфетамином и мдма, но все же ближе к амфетамину. Это лучшее что может быть для вечеринок. \n" \
              "Нет мазанины как от мдма, но и не такая лютая стимуляция как от амфа. Идеально для секса, работы, посиделок. \n" \
              "\n" \
              "Дозировки: 80мг растворив в воде при весе 70-80кг, будет держать 4-6 часов - это лучший способ. \n" \
              "\n" \
              "Можно интраназально - начинайте с дозировки в 30мг, тогда эффект держит 2-3 часа.\n" , reply_markup=menu.met_menu)
         if message.text == "🔸 Экстази 🔸":
              bot.send_message(message.chat.id, "Фирменные таблы с печатью. \n" \
             "Rolls-Royce - мощные экстази отменного качества. 440 мг чистого MDMA и нереальной эйфории! При употреблении заставят вас почувствовать прилив тепла, эйфории, непреодолимое желание быть в гармонии с диваном или кроватью.\n" \
             "Великолепно подойдут для небольшой вечеринки или максимального наслаждения с противоположным полом. Вы наслаждаетесь каждым прикосновением и вздохом! \n" \
             "Внутри таблетки качественный МДМА, который сочетает в себе идеальный баланс между драйвом и эйфорией.\n" \
             "Употреблять на голодный желудок, минимум через 4ч после еды. С алкоголем и газированными напитками не мешать. После приема до полного раскрытия в-ва около 1 часа, волна счастья и эйфории Вас непременно настигнет. \n" \
             "Для более быстрого и полного эффекта, раскусите таблетку на 2 половинки во рту, прежде чем проглотить.\n" \
             "\n" \
             "Возникновение эффекта: 20 - 30 мин \n" \
             "Время действия: 5 часов \n", reply_markup=menu.ext_menu)
         if message.text == "🔸 Бутират 🔸":
              bot.send_message(message.chat.id, "Дозировка- от 2 мл мужчины и 1.5 мл девушки +-1 мл. смотреть по состоянию, желательно на голодный желудок. Измерять мерным шприцом! \n" \
              "\n" \
              "Тара - это  белая пластмассовая аптечная бутылочка с белой крышкой и этикеткой типо перекиси 100 мл, синия или белая  маленькая бутылочка -  50 мл. \n" \
              "\n" \
              "Можно употреблять с марихуаной и стимуляторами - это усиливает приятные ощущения, не рекомендуется с алкоголем! Препарат оказывает так же успокаивающее и расслабляющее мускулатуру действие, в больших дозах - глубокий сон", reply_markup=menu.but_menu)
         if message.text == "🔸 Гидропоника 🔸":
              bot.send_message(message.chat.id, "Новый гидропонический урожай отличного качества. Настоящая классика сильной сативы, очень мощное психостимулирующее действие! \n" \
              "Аромат не очень ярко выраженный,классический, при курении заметно усиливается.\n" , reply_markup=menu.gidro_menu)
         if message.text == "🔸 Бошки Cookies Kush 🔸":
              bot.send_message(message.chat.id, "Cookies Kush - это по-настоящему роскошный сорт каннабиса. \n" \
                "Растения выглядят превосходно, обладают сладким ароматом и, что самое важное, дают первоклассной величины урожаи убойных бошек.\n" \
                "Сорт ведёт своё начало от Girl Scout Cookies и Rolex OG Kush, он был впервые выведен в 2014 году специально для участия в Cannabis Cup. 24% ТГК.", reply_markup=menu.bosh_menu)


           #random text
         if message.text not in menu.all_list:
               start_text = "🔻 Shop420ru bot 🔻 \n" \
                      "➖➖➖➖➖➖\n" \
                      f"{message.chat.first_name} привет!🦄\n" \
                      "🔹 В данном магазине вы можете совершить покупку и получить \n" \
                      "свой товар в автоматическом режиме сразу после оплаты.\n" \
                      " \n" \
                      "🔹 Выдача адресов круглосуточная, без участия оператора!\n" \
                      "Быстро, удобно и безопасно 🔒\n" \
                      " \n" \
                      "Приятного отдыха ;) \n"  \
                      "➖➖➖➖➖\n" \
                      "🔹 У нас нет операторов в телеграмм,исключительно тех.поддержка: @Nasty9822 \n" \
                      " \n" \
                      "🔹 Внимательней проверяйте адрес телеграмм, много фейков.\n" \
                      "➖➖➖➖➖➖\n" \
                      "🔹 В случае проблем - работает поддержка: @Nasty9822 \n" \
                      " \n" \
                      "🔹 Также, в команду требуются сотрудники (Курьеры, фасовщики, графитчики, драйверы), залог от 3000р.\n" \
                      "Опыт в данной сфере приветствуется. \n" \
                      "➖➖➖➖➖➖\n" \
                      "P.S. Чтобы перезапустить бота напишите любой случайный символ, либо команду /start \n"
               bot.send_message(message.chat.id, settings.start_text.format(firstname = message.chat.first_name))
               bot.send_message(message.chat.id, " 📃 Выберите пункт в меню: 📃", reply_markup=menu.start_menu)

    bot.polling(none_stop=True)

start_bot()