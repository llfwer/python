import matplotlib.pyplot as plt
import requests
from bs4 import BeautifulSoup

from 数据存储 import DataWriter, DataReader

url_wuhan = 'http://www.tianqihoubao.com/aqi/wuhan-{0}.html'


# 下载数据到本地存储在excel文件中
def save_data(date):
    res = requests.get(url_wuhan.format(date))

    html = res.content.decode('gbk')

    soup = BeautifulSoup(html, 'html.parser')

    # print(soup.prettify())

    trs = soup.find('div', class_='api_month_list').find('table').find_all('tr')

    # print(format(trs))

    # for item in trs:
    #     for td in item.find_all('td'):
    #         print(format(td))

    columns = []

    data = DataWriter('{0}.xlsx'.format(date))

    for i in range(len(trs)):
        tds = trs[i].find_all('td')

        if i == 0:
            for j in range(len(tds)):
                column = tds[j].get_text().strip()

                data.column(column)
                columns.append(column)
        else:
            for j in range(len(tds)):
                value = tds[j].get_text().strip()

                data.set(i, columns[j], value)

    data.save()

    print('日期{0}:数据下载完成'.format(date))


# 下载2018年所有数据
def init_data():
    for i in range(12):
        save_data('2018{0}'.format('%02d' % (i + 1)))


# AQI全年走势图
def show_aqi_year():
    xticks = []
    xlabels = []
    dates = []
    values = []

    index = 0

    for i in range(12):
        data = DataReader('2018{0}.xlsx'.format('%02d' % (i + 1)))

        for j in range(data.len()):
            item = data.loc(j)

            date = item.loc['日期'][-5:].replace('-', '/')
            value = item.loc['AQI指数']

            index += 1

            if j == 0:
                xticks.append(index)
                xlabels.append(date)

            dates.append(date)
            values.append(value)

    plt.figure()
    plt.title('2018年武汉AQI全年走势图')
    plt.xlabel('日期')
    plt.ylabel('AQI指数')

    plt.xticks(xticks, xlabels, rotation=40)
    plt.plot(dates, values, color='r', linewidth=1.0)

    plt.show()


# AQI月均走势图
def show_aqi_month():
    dates = []
    values = []

    for i in range(12):
        data = DataReader('2018{0}.xlsx'.format('%02d' % (i + 1)))

        dates.append('{0}月'.format((i + 1)))
        values.append(data.avg('AQI指数'))

    plt.figure()
    plt.title('2018年武汉AQI月均走势图')
    plt.xlabel('日期')
    plt.ylabel('AQI指数')

    plt.plot(dates, values, color='r', linewidth=1.0)

    plt.show()


# AQI季度箱形图
def show_aqi_quarter():
    pass


if __name__ == '__main__':
    # 1.下载数据
    # init_data()

    # 中文乱码问题
    plt.rcParams['font.sans-serif'] = ['SimHei']
    plt.rcParams['axes.unicode_minus'] = False

    # 2.输出AQI全年走势图
    show_aqi_year()

    # 3.输出AQI月均走势图
    show_aqi_month()

    # 3.输出AQI季度箱形图
    show_aqi_quarter()
