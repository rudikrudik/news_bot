import requests
from bs4 import BeautifulSoup
import telebot
import time
import config

bot = telebot.TeleBot(config.config_dict['TOKEN'])

#chat_id = -1001677703053
chat_id = config.config_dict['CHAT_ID']

session = requests.Session()


def get_site_data():
    try:
        format_time = time.strftime("%d.%m.%Y")
        url = f'https://www.afanasy.biz/publications/?from={format_time}&to={format_time}'
        response = session.get(url)
        soup = BeautifulSoup(response.text, 'lxml')

        link_news = 'https://www.afanasy.biz' + soup.find('div', class_='daily-card__image image').find('a').get('href')
        response_news = session.get(link_news)

        soup = BeautifulSoup(response_news.text, 'lxml')
        news_text = soup.find('div', class_='single-news__item').get('data-title')
        news_text_alt = soup.find('div', class_='single-news__item').get('data-prev-text')
        image = soup.find('figure', class_='figure').find('img').get('src')

        image_news = session.get(image)
        out = open('news.jpg', 'wb')
        out.write(image_news.content)
        out.close()

        return link_news, news_text, news_text_alt, format_time
    except Exception as e:
        print(e)


def send_message():
    get_news = 'Пустоеслов'
    print(get_news)
    while True:
        try:
            news_text = get_site_data()
            if get_news != news_text[1][:10]:
                news_new_data = get_site_data()
                news = news_new_data[1]
                link = news_new_data[0]
                news_text_alt = news_new_data[2]
                bot.send_photo(chat_id, open('news.jpg', 'rb'), caption=f'*{news}*\n{link}\n\n{news_text_alt}\n',
                               parse_mode='Markdown')
                get_news = news_text[1][:10]
                time.sleep(60)
            else:
                new_news_text = get_site_data()
                news_cut = new_news_text[1][:10]
                get_news = news_cut
                time.sleep(60)
        except Exception as e:
            format_time = time.strftime("%d.%m.%Y")
            print(e)
            time.sleep(300)


send_message()


if __name__ == '__main__':
    while True:
        try:
            bot.polling(none_stop=True, interval=0)
        except Exception as e:
            print(e)
            time.sleep(15)
