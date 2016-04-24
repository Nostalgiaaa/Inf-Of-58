from bs4 import BeautifulSoup
import requests

main_url = 'http://bj.58.com/pbdn/0/pn1'
web_data = requests.get(main_url)
soup = BeautifulSoup(web_data.text,'lxml')
'''
#content > div.person_add_top.no_ident_top > div.per_ad_left > div.col_sub.mainTitle > h1
#index_show > ul.mtit_con_left.fl > li.time

'''
select = soup.select('td.t a.t')
leimu = main_url[:22]
print(leimu)
page_link = []
for href in select:
    page_link.append(href.get('href'))


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
        time = ['null']
    else:
        time = times[0].text
    if prices == []:
        price = ['null']
    else:
        price= prices[0].text
    if places == []:
        place = ['null']
    else:
        place = places[0].text[1:3]

    data = {
        'title': title,
        'time': time,
        'price': price,
        'places': place,
    }

    if(data!={'title': ['null'], 'price': ['null'], 'places': ['null'], 'time': ['null']}):
        print(data)



