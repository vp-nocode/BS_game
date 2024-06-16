from bs4 import BeautifulSoup
import requests
from googletrans import Translator


translator = Translator()


# Создаём функцию, которая будет получать информацию
def get_english_words():
    url = "https://randomword.com/"
    try:
        response = requests.get(url)

        # Создаём объект Soup
        soup = BeautifulSoup(response.content, "html.parser")
        # Получаем слово. text.strip удаляет все пробелы из результата
        english_word = soup.find("div", id="random_word").text.strip()
        # Получаем описание слова
        english_word_definition = soup.find("div", id="random_word_definition").text.strip()

        # Чтобы программа возвращала словарь
        return {
            "russian_word": translator.translate(english_word, src="en", dest="ru").text,
            "russian_word_definition": translator.translate(english_word_definition, src="en", dest="ru").text
        }
    # Функция, которая сообщит об ошибке, но не остановит программу
    except:
        print("Произошла ошибка")


# Создаём функцию, которая будет делать саму игру
def word_game():
    print("Добро пожаловать в игру")
    while True:
        # Создаём функцию, чтобы использовать результат функции-словаря
        word_dict = get_english_words()
        word = word_dict.get("russian_word")
        word_definition = word_dict.get("russian_word_definition")

        # Начинаем игру
        print(f"Значение слова - {word_definition}")
        user = input("Что это за слово? ")
        if user == word:
            print("Все верно!")
        else:
            print(f"Ответ неверный, было загадано это слово - {word}")

        # Создаём возможность закончить игру
        play_again = input("Хотите сыграть еще раз? д/н").lower()
        if play_again != "д":
            print("Спасибо за игру!")
            break


word_game()
