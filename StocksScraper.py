from urllib.request import urlopen
from bs4 import BeautifulSoup
import sched, time
s = sched.scheduler(time.time, time.sleep)

websites = ['https://www.marketwatch.com/investing/currency/usdjpy',
            'https://www.marketwatch.com/investing/currency/usdeur',
            'https://www.marketwatch.com/investing/currency/usdcny']

def scrape(sites):
    for site in sites:
        
        quote_page = site
        page = urlopen(quote_page)
        soup = BeautifulSoup(page, 'html.parser')
        name_box = soup.find('h1', attrs={'class': 'company__name'})
        name = name_box.text.strip()
        print(name)

        price_box = soup.find('h3', attrs={'class':'intraday__price '})
        price = price_box.text.strip()
        print(price)

        change_point = soup.find('span', attrs={'class':'change--point--q'})
        change = change_point.text
        print(change)
        print()
    s.enter(60, 1, scrape, argument=(websites,))

s.enter(0, 1, scrape, argument=(websites,))
s.run()
