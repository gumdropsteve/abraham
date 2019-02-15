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
        #  on bhhsdrysdale links the following is the response
        # urllib.error.HTTPError: HTTP Error 403: Forbidden: Access is denied.
        # if the image is stored at a link like the the following
        # https://mlslmedia.azureedge.net/property/MLSL/81738255/198c9194c26143d98629079e1d884460/2/1
        # the image is downloadable using download_these_ and download_web_image
        # solutions:
        #   make an if/then to download images for listings which store images at usable links
        #       would require if/then on facebook post to determine if have pictures for that specific listing/post
        #       could provide alternate link to use if these do not
        #           using mls number or address, some public listing site  
        request = urllib.request.Request(url)
        img = urllib.request.urlopen(request).read()
        with open ('test_' + x + '.jpg', 'wb') as f: f.write(img)  


# https://mlslmedia.azureedge.net/property/MLSL/81738255/198c9194c26143d98629079e1d884460/2/1
# https://winstonrobson.bhhsdrysdale.com/img/mls/MLSPhotos/EBRRES/40832731_1.jpg?mw=1000&mh=1000 

# sample_base_url = 'https://mlslmedia.azureedge.net/property/MLSL/40832731/198c9194c26143d98629079e1d884460/2/'
# download_web_image(sample_base_url + x)
# download_these_(['1','2'])
download_web_image('https://winstonrobson.bhhsdrysdale.com/img/mls/MLSPhotos/EBRRES/40832731_1.jpg?mw=1000&mh=1000')


def listing_images_links(numbers, psl):  # generates links to desired images for listing (based on requested image numbers)
    bd = rere(on_site_search_links(psl))
    mls_num = ''.join((list(bd)).pop(1)).replace('MLS #', '')
    image_links = []
    for number in numbers:
        image_links.append(bimage_url + mls_num + '_' + number + '.jpg')
    return image_links

    
def save_listing_images():  # numbers, psl, response
    from urllib.request import Request, urlopen
    import urllib
    import urllib.request

    class AppURLopener(urllib.request.FancyURLopener):
        version = "Mozilla/5.0"

    opener = AppURLopener()
    response = opener.open('http://httpbin.org/user-agent')
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


from new_listing_log import pleasanton_log
# print(listing_images_links('123', pleasanton_log))
# save_listing_images('12', pleasanton_log, basically_a_con('https://winstonrobson.bhhsdrysdale.com/ebr/40851771/'))
save_listing_images()


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


