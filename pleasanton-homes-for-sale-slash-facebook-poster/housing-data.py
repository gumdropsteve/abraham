import csv
from bs4 import BeautifulSoup
from functions import *

add_listing_to_log('pleasanton_log.csv')

ß = pull_the_new_pleasanton_listings(npsl)
print(ß)
