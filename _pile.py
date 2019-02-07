import time
ph4s_fb = 'https://facebook.com/pleasantonhome'
pleasantonhomesforsale_hash = '#RealEstate #Residential #ResidentialRealEstate #PleasantonHomesForSale #Pleasanton #California #CaliforniaRealEstate #TriValley #SFBayArea #BayAreaRealEstate #PleasantonCA #HomesForSale #NewListing #SanFranciscoBayArea #HomeForSale #OpenHouse #OpenHouses'


def formated_h4s(location, data):
    header = 'New/Listing/in', '/', location, '!'
    # footer = 'More info: '
    # footer = '\n \n More info:'
    x = '\n- '.join(data)  # pleasanton(pleasanton_log)
    y = '- ', x
    z = ''.join(y)
    a = '\n', z
    b = ''.join(a)
    c = ''.join(header).replace(' ', '').replace('/', ' '), b
    d = '\n'.join(c)
    e = str(d)  # + ' ' + '\n' + '-'  # + 'k'
    # e = d, '', footer
    # f = '\n'.join(e)
    return d  # + footer
    # return e  


def youtube_money(q, hashtags):
    from new_listing_scrape import comps
    from new_listing_log import pleasanton_log  # optimized for minimum to 'check' (general/generic approach)

    p = comps(pleasanton_log)
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
    from new_listing_scrape import pleasanton, gen_link_of_interest
    from the_facebook_part import get_on_facebook, post_to_page, shorten_, moves, post_now, get_on_google
    from new_listing_log import pleasanton_log
    get_on_facebook()
    get_on_google()
    shorten_(gen_link_of_interest(pleasanton_log))
    lower_tags = '\n \n' + hashtags
    ph_foot = '\n \n More info:'
    post_to_page(page=ph4s_fb, location='pleasanton, california', feeling='look', feeling2='home re', status=formated_h4s('Pleasanton', pleasanton()), hashtags=lower_tags, paste_link='yes', footer=ph_foot)
    # time.sleep(1000)
    # post_now()


# google 
google_sign_in_page = 'https://accounts.google.com/signin'
google_identity_box = '#identifierId'
google_id = 'warobson'
google_pass_box = '//*[@id="password"]/div[1]/div/div[1]/input'
google_word = 'winikillyou110897'
long_link_box = '/html/body/div[2]/div[1]/div/div[1]/input'
short_link_button = '//*[contains(@id, "modal-copy-")]'
googl = 'https://goo.gl/'  # link shortener  # glitchier than a bitch
google_base = 'https://google.com'

# facebook
fbhome = 'https://www.facebook.com/login'
facebook_log_box = '#email'
facebook_id = 'wrobson@email.uark.edu'
facebook_pass_box = '#pass'
facebook_word = 'W4rfArE2+$&@G0OdPa$SW%rD'
status_box = '._1mf'
check_in_button = 'tr._51mx:nth-child(2) > td:nth-child(1)'  # '/html/body/div[1]/div[3]/div[1]/div/div/div[2]/div[2]/div[2]/div/div[2]/div[2]/div/div[1]/div/div[2]/div/div[1]/div[1]/div/div[2]/div[1]/div/div/div/div[2]/div/div[2]/div[2]/div/table/tbody/tr[2]/td[2]/span/a/div/div'
check_in_box = '/html/body/div[1]/div[3]/div[1]/div/div/div[2]/div[2]/div[2]/div/div[2]/div[2]/div/div[1]/div/div[2]/' \
               'div/div[1]/div[1]/div/div[2]/div[1]/div/div/div/div[2]/div/div[2]/div[1]/div/table/tbody/tr/td[2]/spa' \
               'n/span/label/input'
feeling_button = '/html/body/div[1]/div[3]/div[1]/div/div/div[2]/div[2]/div[2]/div/div[2]/div[2]/div/div[1]/div/div[' \
                  '2]/div/div[1]/div[1]/div/div[2]/div[1]/div/div/div/div[2]/div/div[2]/div[2]/div/table/tbody/tr[2]/' \
                  'td[1]/span/a/div/div'
feeling_box = '/html/body/div[1]/div[3]/div[1]/div/div/div[2]/div[2]/div[2]/div/div[2]/div[2]/div/div[1]/div/div[2]/d' \
              'iv/div[1]/div[1]/div/div[2]/div[1]/div/div/div/div[2]/div/div[2]/div[1]/div/div/span/span/label/input'
feeling_box2 = '/html/body/div[1]/div[3]/div[1]/div/div/div[2]/div[2]/div[2]/div/div[2]/div[2]/div/div[1]/div/div[2]/' \
               'div/div[1]/div[1]/div/div[2]/div[1]/div/div/div/div[2]/div/div[2]/div[1]/div/table/tbody/tr/td[2]/spa' \
               'n/span/label/input'


gid = google_id
toast = google_word
gpb = google_pass_box
gidb = google_identity_box 
fid = facebook_id 
fw = facebook_word 

