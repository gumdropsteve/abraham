from new_listing_scrape import bbsp, gen_link_of_interest, clean_listing_data
from _pile import pleasantonhomesforsale_hash, psl_pleasanton, new_pleasanton_short_link


# # bbsp(gen_link_of_interest(psl_pleasanton))
# q = gen_link_of_interest(psl_pleasanton)
# print(q)  # https://winstonrobson.bhhsdrysdale.com/ebr/ml81738898
# w = q  # 'https://winstonrobson.bhhsdrysdale.com/ebr/ml81738898'
# print(bbsp(w))


def pleasanton(locaion='Pleasanton'):  # test_005 : plugin : head scrape @ facebook updater, assist scrape @ Abraham
    return clean_listing_data(psl_pleasanton, locaion)  # NEED TO WORK ON DOUBLE PULL


def look_and_see(q, hashtags):
    from new_listing_scrape import comps
    p = comps(psl_pleasanton, new_pleasanton_short_link)
    if p:
        if q == 'c':  # c : check
            if len(p) == 1:
                print('new listing:', p)
                j = input('want to post? (yes/no) ')  # allows check to post
                if j == 'yes':
                    pleasantonhome(pleasantonhomesforsale_hash)  # rerun style 
                elif j == 'no':
                    return('ok, maybe later, see you next time')  
                else:
                    raise Exception('invalid argument')
            elif len(p) > 1:
                print('\n', 'multiple new listings:', '\n', p)
                return ' if you would like to post one of the listings, please temporarily add the others to the refrenced log \n'
            else:  # f (unseen outside of user/syntax error)
                raise Exception('f', len(p))
        elif q == 'y':  # y : yes, post
            pleasantonhome(pleasantonhomesforsale_hash)
        else:
            raise Exception('invalid argument')
    else:
        raise Exception('f')


def pleasantonhome(hashtags):
    from _pile import ph4s_fb
    from new_listing_scrape import gen_link_of_interest
    from the_facebook_part import get_on_facebook, post_to_page, shorten_, moves, post_now, get_on_google
    get_on_facebook()
    get_on_google()
    shorten_(gen_link_of_interest(psl_pleasanton))
    x = pleasanton(locaion='Pleasanton')
    lower_tags = '\n \n -- \n' + hashtags
    post_to_page(page=ph4s_fb, location='pleasanton, california', feeling='look', feeling2='home re', status=x, hashtags=lower_tags, paste_link='yes')  # status=formated_h4s('Pleasanton', pleasanton())
    # time.sleep(1000)
    # post_now()


def run():    
    x = input('\n which would you like to run? \n a: print(look_and_see("c", "")) \n b: print(pleasanton(locaion="Pleasanton")) \n please input a or b \n')
    
    if x == 'a':
        return look_and_see('c', '')
    elif x == 'b':
        return pleasanton(locaion='Pleasanton') 
    else:
        return 'argument invalid'


print(run())



# ONLY REAL ISSUE : NEED TO SAVE SHORTENED LINK, NOT COPY IT
# possible xpaths to short link goo.gl
# //*[@id="modal-copy-eBwzGX"]   /html/body/div[9]/div/div[2]/span   /html/body/div[9]/div/div[2]
# possible css-selectors to short link goo.gl
# #text   span.short-url   div.content:nth-child(2)
'''
CURRENT ERRORS:
 - posting before sending location, feeling, feeling2
 - entering '\n' incorrectly 
     - 'More info:' and '$x,xxx,xxx' recieving interference
     - final line ending as:
        - '$x,xxx,xxx shortened_link More info:' 
            - posting shortly after this, no noticable interaction w/ location or feeling until after posted
AREAS FOR IMPROVEMENT:
 - running in background  
 - runtime 
 - only scraping once
 - automation (schedueling)
 - recording analytics
 - schedueling posts
'''

