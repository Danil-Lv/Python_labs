import telebot
import requests

bot = telebot.TeleBot('8181383363:AAFUExlsJb9cOwwf57jWu6bYR1hiBJ9_SD8')
start_txt = 'Напишите город'


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, start_txt, parse_mode='Markdown')


def get_weather(city):
    url = 'http://api.openweathermap.org/data/2.5/weather'
    params = {
        "q": city,
        "units": "metric",
        "lang": "ru",
        "appid": "79d1ca96933b0328e1c7e3e7a26cb347"
    }


@bot.message_handler(content_types=['text'])
def weather(message):
    city = message.text
    weather_data = get_weather(city)

    if weather_data is None:
        bot.send_message(message.chat.id, "Произошла ошибка при запросе погоды. Попробуйте позже.")
        return

    if weather_data.get('cod') != 200:
        error_message = weather_data.get('message', 'Неизвестная ошибка')
        bot.send_message(message.chat.id, f"Не удалось получить погоду: {error_message}")
        return

    try:
        temperature = round(weather_data['main']['temp'])
        temperature_feels = round(weather_data['main']['feels_like'])
        w_now = f'В городе {city} {temperature} °C'
        w_feels = f'Ощущается как {temperature_feels} °C'
        bot.send_message(message.chat.id, w_now)
        bot.send_message(message.chat.id, w_feels)
    except KeyError as e:
        bot.send_message(message.chat.id, "Произошла ошибка при обработке данных о погоде.")
        print(f"Ошибка ключа в данных погоды: {e}")


if __name__ == '__main__':
    try:
        bot.polling(non_stop=True)
    except Exception as e:
        print('Исключение:', e)
