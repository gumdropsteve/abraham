from time import sleep
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from _pile import googl, f, google_base, gid, long_link_box, toast, short_link_button, gpb, google_sign_in_page, gidb, feeling_box2, fbhome, feeling_box, facebook_log_box, feeling_button, fid, check_in_box, facebook_pass_box, fw, status_box, check_in_button


def post_now():  # seperate for now
    '''
    clicks facebook 'post' button
    '''
    sleep(1.5)
    moves('#composerPostButton', 'css', 'click')  # facebook post button, sometimes has popup after, currently unhedged


# driver
from selenium import webdriver  # want this coming in as late as possible 
options = webdriver.FirefoxOptions()  # (seems to) initiate(s) webdriver.Firefox() once referenced 
options.set_preference("dom.push.enabled", False)  # blocks popups 
driver = webdriver.Firefox(options=options)  # adjusts default


def moves(select_path, css_select_or_xpath, what_to_do, *keys_to_send):  # easier than typing out the whole thing every single time
    '''
    input) select_path
        path to element of interest
    input) css_select_or_xpath
        type of path
        options: xpath, css_selector
    input) what_to_do
        action of interaction between selenium and element
        options: 'click' (click), 'send keys' (send keys), 'sk enter' (send keys + u'\ue007')
    input) *keys_to_send
        required argument if what_to_do == 'send keys' or 'sk enter'
    
    1) determines element type {css_select_or_xpath}
    2) locates element by select_path
    3) determines what_to_do
        3.b) if 'click', clicks; elif 'send keys', sends keys; elif 'sk enter', sends keys + return
        3.c) if 'send keys', sleeps 1.5 seconds; elif 'sk enter', sleeps 2 seconds

    '''
    # long typed & noted for clairity, don't want this breaking
    if css_select_or_xpath == 'css':
        if what_to_do == 'click':
            driver.find_element_by_css_selector(select_path).click()
        elif what_to_do == 'send keys':
            driver.find_element_by_css_selector(select_path).send_keys(keys_to_send)  # sends faster than types
            sleep(1.5)  # time for typing to finish
        elif what_to_do == 'sk enter':
            driver.find_element_by_css_selector(select_path).send_keys(keys_to_send, u'\ue007')
            sleep(2)  
        else:
            raise Exception(f(css_select_or_xpath))
    elif css_select_or_xpath == 'xpath':
        if what_to_do == 'click':
            driver.find_element_by_xpath(select_path).click()  # != wait after, load waits built into related functions
        elif what_to_do == 'send keys':
            driver.find_element_by_xpath(select_path).send_keys(keys_to_send)
            sleep(1.5)
        elif what_to_do == 'sk enter':
            driver.find_element_by_xpath(select_path).send_keys(keys_to_send, u'\ue007')
            sleep(2)  # sk enter usually involves loading, hedge range(1-2)s 
        else:
            raise Exception(f(css_select_or_xpath))
    else:
        raise Exception(f(css_select_or_xpath))


def reach_for_keyboard(some_keys):  # who gone stop me, huh?
    '''
    used in instances where selenium cannot focus element

    input) some_keys
        keys to send
    
    1) builds action chain
    2) executies action chain (.preform())
    3) sleeps 1.5 seconds for keys to type (load and appear on GUI)
    '''
    a = ActionChains(driver)  # build base
    a.send_keys(some_keys)  # set variable
    a.perform()  # execute
    sleep(1.5)  # time for sent keys to process & type


def paste_it(): 
    '''
    pastes whatever is copied
    '''
    a = ActionChains(driver)
    a.send_keys(Keys.COMMAND + 'v')  
    a.perform()
    sleep(1.5)  # time for sent keys to process & type
    # old : key_down(Keys.COMMAND).send_keys("v").key_up(Keys.COMMAND).perform()


def good_get(gettable_url):  # takes sleep responsibility
    driver.get(gettable_url)
    sleep(2)  # built in element load time


def get_on_google():
    '''
    signs into google
    '''
    good_get(google_sign_in_page)  # can present various loading issues
    moves(gidb, 'css', 'sk enter', gid)
    moves(gpb, 'xpath', 'sk enter', toast)
    good_get(google_base)


def shorten_(link):  # shorten_link
    '''
    input) link
        link to be shortened

    1) loads google link shortening site
    2) repeats step 1 because the site returns a 404 on first load (yes, every time)
    3) locates input box for link
    4) clicks button to shorten link
    '''
    good_get(googl)  # Shorten link
    good_get(googl)
    moves(long_link_box, 'xpath', 'sk enter', link)
    moves(short_link_button, 'xpath', 'click')


def get_on_facebook():
    '''
    logs into facebook
    '''
    good_get(fbhome)
    moves(facebook_log_box, 'css', 'send keys', fid)
    moves(facebook_pass_box, 'css', 'sk enter', fw)


def check_in(location):
    '''
    input) location 
        location of status

    1) clicks 'check in' button
    2) sends location to now open 'check in' box then enters (selecting top location result)
    '''
    moves(check_in_button, 'css', 'click')  # check in
    moves(check_in_box, 'xpath', 'sk enter', location)


def feeling_or_activity(general, specific):
    '''
    input) general
        type of feeling or activity
    input) specific
        feeling or activity 

    1) clicks 'feeling/activity' button
    2) sends general to now open 'feeling/activity' box then enters (opening 'feeling/activity' box #2)
    3) sends specific to now open 'feeling/activity' box #2 
    '''
    moves(feeling_button, 'xpath', 'click')  # feeling/activity
    moves(feeling_box, 'xpath', 'sk enter', general)
    moves(feeling_box2, 'xpath', 'sk enter', specific)


def add_hash(tags):
    '''
    input) tags
        relevant hashtags for facebook post
    
    1) sends tags status box (which must be open and selected)
    '''
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
    
