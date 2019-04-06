import requests
from bs4 import BeautifulSoup
from pyecharts import Bar


def main():
    urls = ['http://www.weather.com.cn/textFC/hb.shtml#',
            'http://www.weather.com.cn/textFC/db.shtml',
            'http://www.weather.com.cn/textFC/hd.shtml',
            'http://www.weather.com.cn/textFC/hz.shtml',
            'http://www.weather.com.cn/textFC/hn.shtml',
            'http://www.weather.com.cn/textFC/xb.shtml',
            'http://www.weather.com.cn/textFC/xn.shtml',
            'http://www.weather.com.cn/textFC/gat.shtml']
    for url in urls:
        parse_page(url)
    ALL_data.sort(key=lambda data: data['min_temp'])
    print(ALL_data)
    data = ALL_data[0:10]
    cities = list(map(lambda x: x['city'], data))
    temps = list(map(lambda x: x['min_temp'], data))
    chars = Bar('天气')
    chars.add('', cities, temps)  # 设置最右侧工具栏
    # chars.show_config()  # 调试输出pyecharts的js配置信息
    chars.render('tianqi.html')


ALL_data = []


def parse_page(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:66.0) Gecko/20100101 Firefox/66.0",

    }
    response = requests.get(url, headers=headers)
    text = response.content.decode('utf-8')
    soup = BeautifulSoup(text, 'html5lib')
    conMidtab = soup.find('div', class_='conMidtab')
    # print(conMidtab)
    tables = conMidtab.find_all('table')
    for table in tables:
        trs = table.find_all('tr')[2:]
        for index, tr in enumerate(trs):
            tds = tr.find_all('td')
            city_td = tds[0]
            if index == 0:
                city_td = tds[1]
            city = list(city_td.stripped_strings)[0]
            temp_td = tds[-2]
            min_temp = list(temp_td.stripped_strings)[0]
            ALL_data.append({'city': city, 'min_temp': int(min_temp)})
            # print({'city': city, 'min_temp': int(min_temp)})


if __name__ == '__main__':
    main()
