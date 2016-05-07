from bs4 import BeautifulSoup
import requests



def who_sell(who_sells=0):
    list_view = 'http://bj.58.com/pbdn/{}/pn1/'.format(str(who_sells))
    return list_view
main_url = who_sell(0)
web_data = requests.get(main_url)
soup = BeautifulSoup(web_data.text,'lxml')
select = soup.select('td.t a.t')

leimu = who_sell(0)[:22]
print(leimu)
page_link = []
for href in select:
    page_link.append(href.get('href'))


def get_count(url):
    id = url.split('/')[-1].strip('x.shtml')
    api = 'http://jst1.58.com/counter?infoid={}'.format(id)
    headers = {'Referer': 'http://bj.58.com/pingbandiannao/{}'.format(id),
               'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.112 Safari/537.36'}
    js = requests.get(api, headers=headers)

    views = js.text.split('=')[-1]
    return views

for url in page_link:
    inf = requests.get(url)
    inf_soup = BeautifulSoup(inf.text,'lxml')
    titles = inf_soup.select('div.col_sub.mainTitle > h1')
    times = inf_soup.select('li.time')
    prices = inf_soup.select('div.su_con > span.price')
    places = inf_soup.select('div.su_con > span.c_25d')
    if titles==[]:
        title=['null']
    else:
        title=titles[0].get_text()
    if times == []:
        time = ['空']
    else:
        time = times[0].text
    if prices == []:
        price = ['null']
    else:
        price= prices[0].text
    if places == []:
        place = ['null']
    else:
        place = places[0].text[1:3]+places[0].text[-3:-1]
    data = {
        'title': title,
        'time': time,
        'price': price,
        'places': place,
        'count': get_count(url),
        '类型': '个人' if(main_url[22:23] == '0') else '商家'
    }

    if(title!=['null']):
        print(data)



