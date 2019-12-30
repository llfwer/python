import requests
from bs4 import BeautifulSoup

url_wuhan = 'https://www.aqistudy.cn/historydata/monthdata.php?city=%E6%AD%A6%E6%B1%89'


def get_data(url):
    res = requests.get(url)

    html = res.content.decode('utf-8')

    soup = BeautifulSoup(html, 'html.parser')

    soup.find_all('tr')


if __name__ == '__main__':
    get_data(url_wuhan)