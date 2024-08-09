import telebot

# Создаем экземпляр бота
bot = telebot.TeleBot("7176832425:AAHirxVEfz7EFvU4fEMNwpjGtqkaRDzH7HI")


# Обработчик команды '/start' и '/help'
@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Привет! Напиши любое слово")


# Функция для преобразования слова
def transform_word(word):
    special_cases = {
        "владимир": "хуимир"
        "владимир": "хуимир"
    }

    # Проверка на особые случаи
    if word.lower() in special_cases:
        return special_cases[word.lower()]

    vowels = "аеёиоуыэюяАЕЁИОУЫЭЮЯ"

    for i, letter in enumerate(word):
        if letter in vowels:
            if letter == "е" or letter == "Е":
                # Если гласная "е", заменяем на "хуе"
                return "хуе" + word[i + 1:]
            elif letter == "а" or letter == "А":
                return "хуя" + word[i + 1:]
            elif letter == "о" or letter == "О":
                return "хуё" + word[i + 1:]
            elif letter == "у" or letter == "У":
                return "хую" + word[i + 1:]
            elif letter == "я" or letter == "Я":
                return "хуя" + word[i + 1:]
            else:
                return "хуи" + word[i + 1:]

    # Если по какой-то причине гласная не найдена (хотя такого не должно быть)
    return "Слово должно содержать хотя бы одну гласную и должно быть написано на русском языке"


# Обработчик текстовых сообщений
@bot.message_handler(func=lambda message: True)
def echo_all(message):
    transformed_word = transform_word(message.text)
    bot.reply_to(message, transformed_word)


# Запуск бота
bot.polling()













