# from _pile (21 Feb 2019)
# def listing_images_links(numbers, psl):  # generates links to desired images for listing (based on requested image numbers)
#     bd = rere(on_site_search_links(psl))
#     mls_num = ''.join((list(bd)).pop(1)).replace('MLS #', '')
#     image_links = []
#     for number in numbers:
#         image_links.append(bimage_url + mls_num + '_' + number + '.jpg')
#     return image_links

    
# def save_listing_images():  # numbers, psl, response
#     from urllib.request import Request, urlopen
#     import urllib
#     import urllib.request

#     class AppURLopener(urllib.request.FancyURLopener):
#         version = "Mozilla/5.0"

#     opener = AppURLopener()
#     response = opener.open('http://httpbin.org/user-agent')
    # req = Request('https://winstonrobson.bhhsdrysdale.com/img/mls/MLSPhotos/EBRRES/40851771_2.jpg', headers={'User-Agent': 'Mozilla/5.0'})
    # webpage = urlopen(req).read()
    # urllib.Request.urlretrieve("https://winstonrobson.bhhsdrysdale.com/img/mls/MLSPhotos/EBRRES/40851771_2.jpg", "web-images/local-filename.jpg")
    
    # import os
    # img_lnks = listing_images_links(numbers, psl)
    # print(img_lnks)
    # if response is not None:
        # for image in img_lnks:
            # print(image)
    #  class="image-container owl-lazy" 
    # data-src="/img/mls/MLSPhotos/EBRRES/40846844_1.jpg?mw=641&mh=564">\r\n
            # html = BeautifulSoup(response, hdotp)
            # image_tags = []
            # for image in html.select('owl-lazy'):
            #     image_tags.append(image)  # image['src']
            # print(image_tags)   
    #     os.makedirs('web-images', exist_ok=True)
    #     count = 0
    #     for image in image_tags:
    #         count += 1
    #         q = basically_a_con(image, False)
    #         file = os.open(str(('web-images/' + str(count) + image[image.rfind('.'):]), 'wb'))
    #         file.write(q)
    #         file.close()
            # somed = set()
            # for ul in html.select('img'):
            #     for info in ul.text.split('\n'):
            #         if len(info) > 0: 
            #             somed.add(info.strip(prc))
            # if len(somed) < 1:
            #     return 'ERROR : NO DATA --get_price{}'.format(response)
            # else:
            #     return list(somed)
        # raise Exception('Error retrieving IMG at {}'.format(response))  # Raise an exception if failed to get response


# from new_listing_log import pleasanton_log
# print(listing_images_links('123', pleasanton_log))
# save_listing_images('12', pleasanton_log, basically_a_con('https://winstonrobson.bhhsdrysdale.com/ebr/40851771/'))
# save_listing_images()


# def read():
#     f = open("temp.txt", 'r')
#     file_contents = f.read() 
#     print(file_contents) 
#     f.close()


# # read()

# OFFLINE MODE
# print(formated_h4s('Pleasanton', ['2 Beds', '2 Baths', '1,000 SqFt', '$799,000']))



# x = get_beds_baths_sqft_price(gen_link_of_interest(psl))

# def listing_images(numbers):
#     # https://winstonrobson.bhhsdrysdale.com/img/mls/MLSPhotos/EBRRES/40849202_1.jpg
#     mls_num = (list(x).pop(1)).replace('MLS #', '')
#     image_links = []
#     for number in numbers:
#         image_links.append(bimage_url + mls_num + '_' + number + '.jpg')
#     for link in image_links:            
#         re = simple(link)
#         if re is not None:
#             html = BeautifulSoup(re, hp)
#             somed = set()
#             for ul in html.select('img'):
#                 for info in ul.text.split('\n'):
#                     if len(info) > 0:
#                         somed.add(info.strip())
#             if len(somed) < 1:
#                 raise Exception(f'ERROR : NO DATA ; get_baths at {link}'
#             else:
#                 return list(somed)
#         raise Exception(f'Error retrieving BATHS at {link}'



# def bbsp(eurl):  # bbsp : beds baths sqft price
#     from multiprocessing import Pool
#     pool = Pool()
#     t1 = beds(eurl)
#     t2 = baths(eurl)
#     t3 = sqft(eurl)
#     t4 = price(eurl)
#     ga = pool.map(t1, t2, t3, t4)  # CURRENT ISSUE (multi threading)
#     # ga = beds(eurl), baths(eurl), sqft(eurl), price(eurl)
#     return ga


# from new_listing_scrape (21 Feb 2019)
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
