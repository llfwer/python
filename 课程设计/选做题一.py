import pandas
import requests
from bs4 import BeautifulSoup

# url_wuhan = 'https://www.aqistudy.cn/historydata/monthdata.php?city=%E6%AD%A6%E6%B1%89'
url_wuhan = 'http://www.tianqihoubao.com/aqi/wuhan-201809.html'


def get_data(url):
    res = requests.get(url)

    html = res.content.decode('gbk')

    soup = BeautifulSoup(html, 'html.parser')

    # print(soup.prettify())

    trs = soup.find('div', class_='api_month_list').find('table').find_all('tr')

    # print(format(trs))

    # for item in trs:
    #     for td in item.find_all('td'):
    #         print(format(td))

    data = pandas.DataFrame()

    for i in range(len(trs)):
        tds = trs[i].find_all('td')

        for j in range(len(tds)):
            if i == 0:
                data[tds[j].get_text().strip()] = None
            else:
                if j == 0:
                    pass

    data.to_excel('weather.xlsx', sheet_name='Sheet1', index=False, header=True)


if __name__ == '__main__':
    get_data(url_wuhan)
