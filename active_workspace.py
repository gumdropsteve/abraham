def formated_h4s(location, data):
    header = 'New/Listing/in', '/', location, '!'
    footer = 'More info: \n'
    # footer = '\n \n More info:'
    x = '\n> '.join(data)  # pleasanton(pleasanton_log)
    y = '> ', x
    z = ''.join(y)
    a = '\n', z
    b = ''.join(a)
    c = ''.join(header).replace(' ', '').replace('/', ' '), b
    d = '\n'.join(c)
    e = str(d)  # + ' ' + '\n' + '-'  # + 'k'
    e = d, '', footer
    f = '\n'.join(e)
    # return d  # + footer
    return f  

print(formated_h4s('Pleasanton', ['2 Beds', '2 Baths', '1,000 SqFt', '$799,000']))



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


