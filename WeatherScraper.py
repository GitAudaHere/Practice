from urllib.request import urlopen
from bs4 import BeautifulSoup
import sched, time
s = sched.scheduler(time.time, time.sleep)

websites = ['https://weather.com/weather/today/l/19335:4:US',
            'https://weather.com/weather/today/l/19341:4:US']

def scrape(sites):
    for site in sites:
        
        quote_page = site
        page = urlopen(quote_page)
        soup = BeautifulSoup(page, 'html.parser')
        name_box = soup.find('h1', attrs={'class': 'h4 today_nowcard-location'})
        name = name_box.text.strip()
        print(name)

        temp_box = soup.find('div', attrs={'class':'today_nowcard-temp'})
        temp = temp_box.text
        print(temp)

        weather_card = soup.find('div', attrs={'class':'today_nowcard-phrase'})
        weather = weather_card.text
        print(weather)
        print()
    s.enter(1800, 1, scrape, argument=(websites,))

s.enter(0, 1, scrape, argument=(websites,))
s.run()
