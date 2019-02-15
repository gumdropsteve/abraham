from time import sleep
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from _pile import googl, google_base, gid, long_link_box, toast, short_link_button, gpb, google_sign_in_page, gidb, feeling_box2, fbhome, feeling_box, facebook_log_box, feeling_button, fid, check_in_box, facebook_pass_box, fw, status_box, check_in_button


def post_now():  # seperate for now
        sleep(1.5)
        moves('#composerPostButton', 'css', 'click')  # facebook post button, sometimes has popup after, currently unhedged


# driver
from selenium import webdriver  # want this coming in as late as possible 
options = webdriver.FirefoxOptions()  # (seems to) initiate(s) webdriver.Firefox() once referenced 
options.set_preference("dom.push.enabled", False)  # blocks popups 
driver = webdriver.Firefox(options=options)  # adjusts default


def moves(select_path, css_select_or_xpath, what_to_do, *k):  # easier than typing out the whole thing every single time
    # long typed & noted for clairity, don't want this breaking
    if css_select_or_xpath == 'css':
        if what_to_do == 'click':
            # sleep(1.5)  # hedge load time (element load time >= get time), suggusted range(1, 2)
            driver.find_element_by_css_selector(select_path).click()
        elif what_to_do == 'send keys':
            # sleep(1.5)
            driver.find_element_by_css_selector(select_path).send_keys(k)  # sends faster than types
            sleep(1.5)  # time for typing to finish
        elif what_to_do == 'sk enter':
            # sleep(1.5)
            driver.find_element_by_css_selector(select_path).send_keys(k, u'\ue007')
            sleep(2)  # sk enter usually involves loading, hedge range(0.5 , 1.5)s 
        else:
            raise Exception("{} is not yet an option (: 'click' , 'send keys' , 'sk enter')".format(css_select_or_xpath))
    elif css_select_or_xpath == 'xpath':
        if what_to_do == 'click':
            # sleep(1.5)
            driver.find_element_by_xpath(select_path).click()  # != wait after, load waits built into related functions
        elif what_to_do == 'send keys':
            # sleep(1.5)
            driver.find_element_by_xpath(select_path).send_keys(k)
            sleep(1.5)
        elif what_to_do == 'sk enter':
            # sleep(1.5)
            driver.find_element_by_xpath(select_path).send_keys(k, u'\ue007')
            sleep(2)
        else:
            raise Exception("{} is not yet an option (: 'click' , 'send keys' , 'sk enter')".format(css_select_or_xpath))
    else:
        raise Exception("{} unavailable at time, please use 'css' (for css_selector) or 'xpath'".format(css_select_or_xpath))


def reach_for_keyboard(some_keys):  # who gone stop me, huh?
    a = ActionChains(driver)  # build base
    a.send_keys(some_keys)  # set variable
    a.perform()  # execute
    sleep(1.5)  # time for sent keys to process & type


def paste_it(): 
    a = ActionChains(driver)
    a.send_keys(Keys.COMMAND + 'v')  
    a.perform()
    sleep(1.5)  # time for sent keys to process & type
    # old : key_down(Keys.COMMAND).send_keys("v").key_up(Keys.COMMAND).perform()


def good_get(gettable_url):  # takes sleep responsibility
    driver.get(gettable_url)
    sleep(2)  # built in element load time


def get_on_google():
    good_get(google_sign_in_page)  # can present various loading issues
    moves(gidb, 'css', 'sk enter', gid)
    moves(gpb, 'xpath', 'sk enter', toast)
    good_get(google_base)


def shorten_(link):  # shorten_link
    good_get(googl)  # Shorten link
    good_get(googl)
    moves(long_link_box, 'xpath', 'sk enter', link)
    moves(short_link_button, 'xpath', 'click')


def get_on_facebook():
    good_get(fbhome)
    moves(facebook_log_box, 'css', 'send keys', fid)
    moves(facebook_pass_box, 'css', 'sk enter', fw)


def check_in(location):
    moves(check_in_button, 'css', 'click')  # check in
    moves(check_in_box, 'xpath', 'sk enter', location)


def feeling_or_activity(general, specific):
    moves(feeling_button, 'xpath', 'click')  # feeling/activity
    moves(feeling_box, 'xpath', 'sk enter', general)
    moves(feeling_box2, 'xpath', 'sk enter', specific)


def add_hash(tags):
    reach_for_keyboard(tags)  # hashtags


def post_to_page(page, location, feeling, feeling2, status, hashtags, paste_link):  
    # coming soon: post_type, schedule, blame
    # need options to auto-set
    # need less inputs, preset definitions?
    good_get(page)
    moves(status_box, 'css', 'click')  # open status box
    reach_for_keyboard(status)  # send status (not intractable with send_keys)
    if paste_link == 'yes':
        paste_it()  # link to listing
    else:
        pass  
    add_hash(hashtags)  # hashtags
    check_in(location)
    feeling_or_activity(feeling, feeling2)
    


# def wewoo(p, loc, f, f2, k, h, *link):
#     get_on_facebook()
#     post_to_page(p, loc, f, f2, k, h, *link)
#     sleep(7)  # time to review / inspect errors 
#     driver.close()  # need to end for rerun on mac (apparently)



# import os  # test to differentiate os (keys: control v. command) 
# print(os.ttyname)
