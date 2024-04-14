import requests
from bs4 import BeautifulSoup


class CryptoScraper:
    def __init__(self):
        '''Initialization Function'''

        self.crypto_list = list()

        for i in range(1, 2):
            url = f'https://crypto.com/price?page={i}'
            print('--> Scraping:', url)

            # scraping data from webpage
            soup = BeautifulSoup(requests.get(url).text, 'html.parser')
            table = soup.find('table')

            # extracting data from table element
            self.extract_crypto_data(table)

    def get_crypto_data(self):
        '''Return Crypto Dataframe'''

        return self.crypto_list, self.get_table_heading()

    @staticmethod
    def get_table_heading(url='https://crypto.com/price'):
        '''Extracting Table Heading From Webpage'''

        # scraping data from webpage
        soup = BeautifulSoup(requests.get(url).text, 'html.parser')
        table = soup.find('table')

        # extracting table heading from table element
        heading = list()
        thead = table.find('thead').find('tr').find_all('th')[1:8]
        for th in thead:
            heading.append(th.text)

        return heading

    def extract_crypto_data(self, table):
        '''Extracting Crypto Data From Table'''

        tbody = table.find('tbody').find_all('tr')
        for tr in tbody:
            tds = tr.find_all('td')[1:8]
            # appending crypto data to a class list
            self.crypto_list.append((
                tds[0].text,
                tds[1].find('p').text,
                tds[2].find('div').text,
                tds[3].text,
                tds[4].text,
                tds[5].text,
                tds[6].find('svg'),))
