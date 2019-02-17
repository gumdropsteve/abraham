import csv
from bs4 import BeautifulSoup
from new_listing_scrape import basically_a_con
from _pile import addresses, hdotp, new_pleasanton_short_link


def pull_the_new_pleasanton_listings(base_url):
    response = basically_a_con(base_url)
    if response is not None:  # url accessibility check
        html = BeautifulSoup(response, hdotp)
        many_datas = set()
        for ul in html.select(addresses):  # 12 addresses (max seen)
            for info in ul.text.split('\n'):
                if len(info) > 0:
                    many_datas.add(info.strip())
        pulled_listings = list(many_datas)
        return pulled_listings
    # Raise an exception if we failed to get any data from the url
    raise Exception(f'Error retrieving new_listings_on_base_page_to_scrape at {base_url}')
    # use of 'raise' eliminates need for 'else' following 'if'  # seems to be in a replacing fashion


x = pull_the_new_pleasanton_listings(new_pleasanton_short_link)
# print(len(x))
