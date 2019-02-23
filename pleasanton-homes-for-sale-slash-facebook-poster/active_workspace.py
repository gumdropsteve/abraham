from time import sleep
from bs4 import BeautifulSoup
import multiprocessing
import itertools
import math
from _pile import prc, bdz, bths, stdsze, hdotp
from new_listing_scrape import basically_a_con


def pull(response, data):
    '''
    pool = multiprocessing.Pool()
    output = pool.map(check_prime, number_range)  # a list of booleans
    primes = [p for p in itertools.compress(number_range, output)]
    '''
    html = BeautifulSoup(response, hdotp)
    some_data = set()
    def scrape():
        for ul in html.select(data):
            for info in ul.text.split('\n'):
                    if len(info) > 0: 
                            some_data.add(info.strip(data))
        if len(some_data) < 1:
                return f'ERROR : NO DATA --get_price{response}'
        else:
                return list(some_data)
    if response is not None:
        pool = multiprocessing.Pool()
        output = pool.map(scrape, data)
        information = [i for i in itertools.compress(data, output)]
        return information

y = 'https://winstonrobson.bhhsdrysdale.com/single-family/mls/81737464/3305-hudson-ct-pleasanton-ca-94588'
z = pull(basically_a_con(y), (bdz, bths, stdsze, prc))
print(z)

'''def primes_parallel(number_range):
    """Computes primes in parallel using multiprocessing.

    Parameters
    ----------
    number_range: an iterable of ints to check for primeness.

    Returns
    -------
    list of primes
    """
    # multiprocessing.cpu_count() cores used.
    pool = multiprocessing.Pool()
    output = pool.map(check_prime, number_range)  # a list of booleans
    primes = [p for p in itertools.compress(number_range, output)]
    return primes'''

'''def check_prime(n):
    """Checks if a number is prime.

    Parameters
    ----------
    n: an Int

    Returns
    -------
    Bool
    """
    if n % 2 == 0:
        return False
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True'''


# print(primes_parallel(range(10)))
# sleep(100)

'''def price(response):
    if response is not None:
        html = BeautifulSoup(response, hdotp)
        somed = set()
        for ul in html.select(prc):
            for info in ul.text.split('\n'):
                if len(info) > 0: 
                    somed.add(info.strip(prc))
        if len(somed) < 1:
            return 'ERROR : NO DATA --get_price{}'.format(response)
        else:
            return list(somed)
    raise Exception('Error retrieving PRICE at {}'.format(response))  '''


from time import sleep
import random

def add_listing_to_log(listing, csv_log):
        '''
        input) unseen new listing {listing}
        input) log where listing belongs 
                i.e. log where unseen new listings of same sort have been placed
                        sort tbd , currently by city

        1) rearranges listing to list ['address', ' city', 'state_zip']  
                  # eventually want state, zip
        2) identified address, city, state_zip
        3) opens csv_log and appends new row 
                columns line up with list order
                with datetime column on end
        '''
        import csv   
        import datetime

        formatted = str(listing).replace('[', '').replace(']', '').replace("'", '').split(',')
       
        address = formatted[0]
        city = formatted[1]
        state_zip = formatted[2]

        fields = [address, city, state_zip, datetime.datetime.now()]

        with open(csv_log, 'a') as f:
                writer = csv.writer(f)
                writer.writerow(fields)


def to_list_from(csv_log):
        '''
        input) csv of previously seen (new) listings {csv_log}

        1) loads csv_log into pandas dataframe as df
        2) iterates over each row of df
        3) selects address (1), city (2), and state_zip (3) columns 
        4) joins each set of 1, 2, and 3 with ,
                result of join is the same as a freshly scraped address
        5) appends each rusult to log

        output) list of previously seen listings {log}
        '''
        import pandas as pd 
     
        df = pd.read_csv(csv_log)
        log = []
     
        for index, row in df.iterrows():  # vscode ids index as being unused, but taken out == breaks
                x = ','.join((row['address'], row['city'], row['state_zip']))
                log.append(x)
     
        return log 


# from new_listing_scrape import comps
# a = to_list_from('pleasanton_log.csv')
# print(len(a))
# from new_listing_scrape import comps
# test_000 = comps(a)
# print(len(test_000))  
# for i in test_000:
#         add_listing_to_log(i, 'pleasanton_log.csv')
# h = len(a) + len(test_000)
# print(f'expected: {h}')
# add_listing_to_log(listing, 'pleasanton_log.csv')
# b = to_list_from(r'pleasanton_log.csv')
# print(len(b))



# print(a.pop())

# print(a)
# print(df['state_zip'])
# print(len(pleasanton_log))
# def convert_pleasanton_(log):
#         for listing in log:
#                 test(listing)
# convert_pleasanton_(pleasanton_log)

import urllib.request
from new_listing_scrape import rere, on_site_search_links

bimage_url = 'https://winstonrobson.bhhsdrysdale.com/img/mls/MLSPhotos/EBRRES/'  # base image url


def download_web_image(url):
    request = urllib.request.Request(url)
    img = urllib.request.urlopen(request).read()
    with open ('test.jpg', 'wb') as f: f.write(img)


def download_these_(numbers, *base_url): 
    for x in numbers:
        url = 'https://winstonrobson.bhhsdrysdale.com/img/mls/MLSPhotos/EBRRES/40832731_' + x + '.jpg?mw=1000&mh=1000 '
        '''         
        on bhhsdrysdale links the following is the response
        urllib.error.HTTPError: HTTP Error 403: Forbidden: Access is denied.
        if the image is stored at a link like the the following
        https://mlslmedia.azureedge.net/property/MLSL/81738255/198c9194c26143d98629079e1d884460/2/1
        the image is downloadable using download_these_ and download_web_image
        solutions:
          make an if/then to download images for listings which store images at usable links
              would require if/then on facebook post to determine if have pictures for that specific listing/post
              could provide alternate link to use if these do not
                  using mls number or address, some public listing site  
        '''
        request = urllib.request.Request(url)
        img = urllib.request.urlopen(request).read()
        with open ('test_' + x + '.jpg', 'wb') as f: f.write(img)  


# https://mlslmedia.azureedge.net/property/MLSL/81738255/198c9194c26143d98629079e1d884460/2/1
# https://winstonrobson.bhhsdrysdale.com/img/mls/MLSPhotos/EBRRES/40832731_1.jpg?mw=1000&mh=1000 

sample_base_url = 'https://mlslmedia.azureedge.net/property/MLSL/40832731/198c9194c26143d98629079e1d884460/2/'
a_bhhs_example = 'https://winstonrobson.bhhsdrysdale.com/img/mls/MLSPhotos/EBRRES/40832731_1.jpg?mw=1000&mh=1000'

# download_web_image(sample_base_url + x)
# download_these_(['1','2'])
# test_000 = sample_base_url + '1'
# download_web_image(test_000)
