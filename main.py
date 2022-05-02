from bs4 import BeautifulSoup
import requests

x = 0



while True:
    if x == 0:
        url = 'https://auto.ria.com/car/used/'
    else:
        url = 'https://auto.ria.com/car/used/' + next_page_link

    request = requests.get(url)
    soup = BeautifulSoup(request.text, 'html.parser')
    contents = soup.find_all('div', class_='content')

    for content in contents:
        name = content.find('a', attrs={'class':'address'}).get('title')
        if name.__contains__('BMW'):
            sublink = content.find('a', attrs={'class': 'address'}).get('href')
            price = content.find('div', attrs={'class': 'price-ticket'}).get('data-main-price')
            print(str(name) + ' - ' + str(price) + ' USD' + ' - ' + str(sublink))
        else:
            break

    btn_next = soup.find('a', class_='page-link js-next')
    if btn_next is not None:
        url_next_page = btn_next.get('href')
        next_page_link = url_next_page[32:]
        x = x + 1
    else:
        break
