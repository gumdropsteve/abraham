import os
from requests import get
from bs4 import BeautifulSoup
from contextlib import closing
from requests.exceptions import RequestException
from _pile import tol, lmilsst, stts, addresses, prc, bdz, bths, stdsze, bsearch_url, base_url, new_pleasanton_short_link, hdotp


def l(e):  # prints errors  # need to make this post to permanent log
    print(e)


def good_respons(e):  # Returns True if the response seems to be HTML, False otherwise.
    content_type = e.headers['Content-Type'].lower()
    return (e.status_code == 200
            and content_type is not None
            and content_type.find('html') > -1)


def basically_a_con(dom, *stream):  # Attempts to get the content at `url` (dom) by making an HTTP GET request.
    try:
        if stream:
            with closing(get(dom, stream=stream)) as e:
                if good_respons(e):  # If the content-type of response is some kind of HTML/XML
                    return e.content  # return the text content
        else:
            with closing(get(dom, stream=True)) as e:
                if good_respons(e):  # If the content-type of response is some kind of HTML/XML
                    return e.content  # return the text content
    except RequestException as e:  # otherwise return None
        raise Exception(f'Error during requests to {dom} : {str(e)}')


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


def comps(existing_results):
    results = []  # short term log for first encounter listings
    in_existing_results_count: int = 0  # specified int, not sure if any different from just x = 0, doubt it is
    for listing in pull_the_new_pleasanton_listings(new_pleasanton_short_link):  # for data in datas
        if listing not in results:  # if not a double post
            if listing not in existing_results:  # if an unseen listing
                results.append(listing)  # add listing to results
            elif listing in existing_results:  # if previously logged
                in_existing_results_count += 1  # add 1 to in_existing_results_count
        elif listing in results:  # instance unseen
            print('existing in results (possible double listing?)', listing)  # error unseen (hedge)
        else:
            print('we got to else.. f.')
    if len(results) > 1:  # if multiple new listings
        multi_result_dict = []
        for result in results:
            multi_result_dict.append(result)
        return multi_result_dict
    elif len(results) == 1:  # expected most common actionable response once in routine
        return results  # broken down asap
    elif len(results) == 0:  # expected most common response once in routine
        raise Exception(f'No New Listings in Pleasanton {new_pleasanton_short_link}')
    else:
        raise Exception('F')


def on_site_search_links(s):  # links as if searched the exact address on site
    some_data = []  # for later processing of multiple new listings 
    news = comps(s)
    num_news = len(news)
    if num_news == 1:
        for prop_of_interest in news:  # for unseen new listing  # meant to expand later for processing multiple new listings 
            some_data.append(bsearch_url + prop_of_interest.lower().replace(' ', ';'))  # adds address after conversion to resemble end of search url
        return some_data  # list of end pieces for on site search links
    else:
        raise Exception(f'MULTIPLE NEW LISTINGS: \n {num_news} new listings. {news}')


def rere(url):  # all around utility of sorts
    if len(url) == 1:
        x = (str(url).replace('[', '').replace("'", "").replace(']', ''))
        r = basically_a_con(str(x))
        if r is not None:
            html = BeautifulSoup(r, hdotp)
            t_o_l = set()  # type_of_listing
            for ul in html.select(tol):  # type_listing
                for info in ul.text.split('\n'):
                    if len(info) > 0:
                        t_o_l.add(info.strip())
            ct = ''.join(t_o_l)  # clean_type
            mlsnum = set()  # mls_number_of_listing
            for ul in html.select(lmilsst):  # mls of listing
                for info in ul.text.split('\n'):
                    if len(info) > 0:
                        mlsnum.add(info.strip())
            cmls = ''.join(mlsnum)  # clean_mls
            sol = set()
            for ul in html.select(stts):  # status of listing
                for info in ul.text.split('\n'):  # 
                    if len(info) > 0:
                        sol.add(info.strip())
            chk = ''.join(sol)  # check_status
            return [ct, cmls, chk]
        raise Exception(f're_inform_re_evaluate {url} response == {r}') # failed get
    elif len(url) > 1:
        raise Exception(f'More than one new listing {url}')


def gen_link_of_interest(psl):  # builds link for listing of interest
    lsl = on_site_search_links(psl)
    bd = rere(lsl)
    mls = (bd.pop(1)).replace('MLS #', '/ebr/')
    if len(lsl) > 0:
        if len(lsl) > 1:
            w = 0
            link_dct = []
            while w in range(0, len(lsl)):
                if bd.pop() == 'Active':  # don't want to be posting anything but Active 
                    targ_url = (base_url + mls).lower()  # current = shortest, length seems to + p(e)
                    # url w/o .bhhsdrysdale result = endless site loading screen
                    link_dct.append(targ_url)
                    w += 1
                else:
                    raise Exception(f'Listing Status = {rere(on_site_search_links(psl).pop())}')
            return link_dct  # *
        else:
            if bd.pop() == 'Active':
                return (base_url + mls).lower()  # current = shortest, length seems to + p(e)
            else:
                raise Exception(f'Listing Status = {rere(on_site_search_links(psl).pop())}')

    raise Exception(f'len(listing_search_link {len(lsl)} < 0')   # **
    # ** if don't return before this and logical next, will return when not meant to
    # * aka putting print() instead of return here


def formated_h4s(location, data):
    header = 'New/Listing/in', '/', location, '!'
    footer = 'More info: '
    x = '\n > '.join(data)  # pleasanton(pleasanton_log) '\n- ' 
    y = ' > ', x  # '- '
    z = ''.join(y)
    a = z
    b = ''.join(a)
    c = ''.join(header).replace(' ', '').replace('/', ' ')
    d = c, b
    e = '\n'.join(d)
    f = str(e)  # + ' ' + '\n' + '-'  # + 'k'
    g = f, footer
    h = '\n'.join(g)
    edit_file = open("temp.txt", "w")
    edit_file.write(h)
    edit_file.close()
    read_file = open("temp.txt", "r")
    q = read_file.read()
    read_file.close()
    return q


def clean_listing_data(psl, location):  # done here to hedge for readability of pull_listing_data
    x = bbsp(gen_link_of_interest(psl))
    # listing_images([1, 2])
    price = ''.join((list(x)).pop())
    beds = ''.join((list(x)).pop(0)).replace('Beds', ' Beds')
    baths = ''.join((list(x)).pop(1)).replace('Baths', ' Baths')
    sqft = ''.join((list(x)).pop(2)).replace('Sqft', ' SqFt')
    big_4 = beds, baths, sqft, price  # ('4 Beds', '2 Baths', '1,965 SqFt', '$1,025,500')
    return formated_h4s(location, big_4)


def price(response):
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
    raise Exception('Error retrieving PRICE at {}'.format(response))  # Raise an exception if failed to get response


def sqft(response):
    if response is not None:
        html = BeautifulSoup(response, hdotp)
        somed = set()
        for ul in html.select(stdsze):
            for info in ul.text.split('\n'):
                if len(info) > 0:
                    somed.add(info.strip())
        if len(somed) < 1:
            raise Exception(f'ERROR : NO DATA --get_sqft{response}')
        else:
            return list(somed)
    raise Exception(f'Error retrieving SQFT at {response}')  # Raise an exception if failed to get response


def beds(response):
    if response is not None:
        html = BeautifulSoup(response, hdotp)
        somed = set()
        for ul in html.select(bdz):
            for info in ul.text.split('\n'):
                if len(info) > 0:
                    somed.add(info.strip())
        if len(somed) < 1:
            raise Exception(f'ERROR : NO DATA --get_beds{response}')
        else:
            return list(somed)
    raise Exception(f'Error retrieving BEDS at {response}')  # Raise an exception if failed to get response


def baths(response):
    if response is not None:
        html = BeautifulSoup(response, hdotp)
        somed = set()
        for ul in html.select(bths):
            for info in ul.text.split('\n'):
                if len(info) > 0:
                    somed.add(info.strip())
        if len(somed) < 1:
            raise Exception(f'ERROR : NO DATA ; get_baths{response}')
        else:
            return list(somed)
    raise Exception(f'Error retrieving BATHS at {response}')  # Raise an exception if failed to get response


def get_beds_baths_sqft_price(response):
    return beds(response), baths(response), sqft(response), price(response)


def bbsp(listing_url):
    return get_beds_baths_sqft_price(basically_a_con(listing_url))


# WHERE WE STARTED (Jan 2019)
"""
import time
from requests import get
from bs4 import BeautifulSoup
from contextlib import closing
from requests.exceptions import RequestException

now = time.time()


def is_good_response(resp):
    # Returns True if the response seems to be HTML, False otherwise.
    content_type = resp.headers['Content-Type'].lower()
    return (resp.status_code == 200
            and content_type is not None
            and content_type.find('html') > -1)


def log_error(e):  # need to make this post to permanent log
    # prints errors, log pending
    print(e)


def simple_get(url):
    # Attempts to get the content at `url` by making an HTTP GET request.
    # If the content-type of response is some kind of HTML/XML, return the text content, otherwise return None.
    try:
        with closing(get(url, stream=True)) as resp:
            if is_good_response(resp):
                return resp.content
            else:
                return None
    except RequestException as e:
        log_error('Error during requests to {0} : {1}'.format(url, str(e)))
        return None


def pull_the_new_pleasanton_listings(base_url):
    response = simple_get(base_url)
    if response is not None:
        html = BeautifulSoup(response, 'html.parser')
        many_datas = set()
        for ul in html.select('div.mdl-card__supporting-text h2.mdl-card__title-text'):  # 12/12 addresses
            for info in ul.text.split('n'):
                if len(info) > 0:
                    many_datas.add(info.strip())
        pulled_listings = list(many_datas)
        return pulled_listings
    # Raise an exception if we failed to get any data from the url
    raise Exception('Error retrieving new_listings_on_base_page_to_scrape at {}'.format(base_url))


def test_000(existing_results):
    results = []
    in_existing_results_count: int = 0
    the_pull = pull_the_new_pleasanton_listings('https://goo.gl/WJmmut')
    for listing in the_pull:
        if listing not in results:
            if listing not in existing_results:
                results.append(listing)
            elif listing in existing_results:
                in_existing_results_count += 1
        elif listing in results:
            print('existing in results (possible double listing?)')
        else:
            print('we got to else.. f.')
    if len(results) >= 1:
        print('preexisting listings:', in_existing_results_count)
        return results
    elif len(results) == 0:
        print('preexisting listings:', in_existing_results_count)
        return 'no new results'
    else:
        print('len(results): != 0 , < 1')
        return 'we got to else.. f.'


'''from here we say
if results are none; end.
else;
go find the new listing (formatted url ?perhaps?)
pull the listing info
put it into formatted facebook post
login and post (post asap to test rand times)
&& have this auto-run every:
    15 min during peak times
    75 min during trough times
        15 min during all times at first
            store results seperately
            update email/brief every hour'''
# results log
# listings log
# logs in general ?separate file? ? imported?

# current 'listings log'
from_test_000 = ['4326 CAMPINIA PL, PLEASANTON, CA 94566', '6248 ROSLIN CT, PLEASANTON, CA 94588',
'3537 GULFSTREAM ST, PLEASANTON, CA 94588', '3053 FERNDALE COURT, PLEASANTON, CA 94588',
'7826 LA QUINTA CT, PLEASANTON, CA 94588', '3834 PINOT CT, PLEASANTON, CA 94566',
'2345 E RUBY HILL DR, PLEASANTON, CA 94566', '2113 ARROYO CT #1, PLEASANTON, CA 94588',
'6913 CORTE MATEO, PLEASANTON, CA 94566', '3902 MOUNT MCKINLEY COURT, PLEASANTON, CA 94588',
'29 COLBY CT, PLEASANTON, CA 94566']

print(test_000(from_test_000))
then = time.time()
print('execution:', then - now, 'seconds')
"""


# def get_info(url):
#     response = simple_get(url)
#     if response is not None:
#         html = BeautifulSoup(response, 'html.parser')
#         somed = set()
#         for ul in html.select('ul.family li'):
#             for info in ul.text.split('\n'):
#                 if len(info) > 0:
#                     somed.add(info.strip())
#         if len(somed) < 1:
#             raise Exception('ERROR : NO DATA ; get_info{}'.format(url))
#         else:
#             return list(somed)
#     raise Exception('Error retrieving INFO at {}'.format(url))  # Raise an exception if failed to get response


# print(get_info('https://winstonrobson.bhhsdrysdale.com/single-family/mls/81736758/3973-w-las-positas-blvd-pleasanton-ca-94588'))
