from os.path import join
from pandas import DataFrame
from mysql.connector import Error
from crypto_scraper import CryptoScraper
from util import check_directory, get_datetime


def save_as_csv(data, file_name, table_heading):
    check_directory('Crypto Data (csv)')

    DataFrame(data, columns=table_heading).to_csv(
        join('Crypto Data (csv)', file_name + '.csv'), index=False)
    print(f'--> CSV created! (Name): {file_name}')


if __name__ == '__main__':
    
    date_time = get_datetime()
    crypto_scraper = CryptoScraper()
    crypto_data, heading = crypto_scraper.get_crypto_data()
    save_as_csv(crypto_data, date_time, heading)
