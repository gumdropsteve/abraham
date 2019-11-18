import os
from requests import get
from bs4 import BeautifulSoup
from contextlib import closing
from requests.exceptions import RequestException
from _pile import tol, lmilsst, stts, addresses, prc, bdz, bths, stdsze, bsearch_url, base_url, hdotp, npsl


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
        raise Exception(f'Error during requests to {dom} : {e}')


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


def comps(existing_results, city_short_link):
    '''
    input) previously seen listngs {existing_results} for city of interest
    input) link to city of interest listings sorted by newness {city_short_link}

    1) pulls most recent new listings from city_short_link (usualy 12, range 10-13)
        based on results of searching that city, gridview, sorting for newest results
    2) compares the addresses of those listings to the previously seen listings (log) for that city

    output) new listings in that city 
        which are in the first page of new listings 
        and are not existing_results (log) for that city 
    '''
    results = []  # short term log for first encounter listings
    in_existing_results_count: int = 0  # specified int, not sure if any different from just x = 0, doubt it is
    for listing in pull_the_new_pleasanton_listings(city_short_link):  # for data in datas
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
        raise Exception(f'No New Listings in Pleasanton {city_short_link}')
    else:
        raise Exception('F')


def on_site_search_link(seen_listings, city_short_link):
    '''
    1) runs comps() on seen_listings for city of interest (news = results)
    2) takes the full address of any newly seen listing
    3) converts it to url one would land on as result of searching that full address (on site)

    inputs: 
    > seen_listings (csv)
        >> previously seen listing log
    > city_short_link (str)
        >> link for comps()

    output: 
    > urls (list)
        >> url(s) of on site searches of the exact addresses seen in news
    '''
    # set output list
    urls = []  
    # list of strings
    news = comps(seen_listings, city_short_link)
    # go through each property
    for property in news:
        # write the link that would result from searching it and add to output list
        urls.append(bsearch_url + property.lower().replace(' ', ';'))
    # list of strings (urls)
    return urls


def rere(os_search_links):  # all around utility of sorts
    '''
    area for improvement) processing multiple new listings 
    area for improvement) multithreading 

    # overview) reevaluates listings, 
    #     acts as gate keeper determining if listing meets minimum criteria,
    #     returns useful information if listing is green lit 
    #     information is used to further pull listing details and pictures 

    input) on_site_search_links {os_search_links}

    1) pulls listing type 
        - currently appears to be unused
        - should have it double check that listing is 'Single Family'
        - listing can be 'Single Family', 'Lot/Land', 'Commercial', 'Mobile Home', 
            'Residential Income', 'Condo/Townhome', 'Farm/Ranch'
    2) pulls listing status
        - checks listing is still 'active'
        - listing can be 'Active', 'Pending', 'Contingent', 
            'Pending (Do Not Show)', 'Coming Soon', 'Sold'
    3) pulls listing mls number 
        - used to generate listing specific link
    
    output) cleaned type_of_listing, mls number of listing, listing status  
    '''
    if len(os_search_links) == 1:
        x = (str(os_search_links).replace('[', '').replace("'", "").replace(']', ''))
        r = basically_a_con(str(x))
        if r is not None:  # if response
            html = BeautifulSoup(r, hdotp)
            t_o_l = set()  # type_of_listing
            for ul in html.select(tol):  # type_listing
                for info in ul.text.split('\n'):
                    if len(info) > 0:
                        t_o_l.add(info.strip())
            clean_type_of_listing = ''.join(t_o_l)  # clean_type
            mlsnum = set()  # mls_number_of_listing
            for ul in html.select(lmilsst):  # mls of listing
                for info in ul.text.split('\n'):
                    if len(info) > 0:
                        mlsnum.add(info.strip())
            mls_number_of_listing = ''.join(mlsnum)  # clean_mls
            sol = set()
            for ul in html.select(stts):  # status of listing
                for info in ul.text.split('\n'):  # 
                    if len(info) > 0:
                        sol.add(info.strip())
            check_listing_status = ''.join(sol)  # check_status
            return [clean_type_of_listing, mls_number_of_listing, check_listing_status]
        raise Exception(f're_inform_re_evaluate {os_search_links} response == {r}') # failed get
    elif len(os_search_links) > 1:  # if multiple unseen new listings 
        # raise Exception(f'More than one new listing {os_search_links}')
        multiple_new_listings = []
        for link in os_search_links:
            # x = (str(link).replace('[', '').replace("'", "").replace(']', ''))
            # x = (str(os_search_links).replace("'", ""))
            r = basically_a_con(link)
            if r is not None:  # if response
                html = BeautifulSoup(r, hdotp)
                t_o_l = set()  # type_of_listing
                for ul in html.select(tol):  # type_listing
                    for info in ul.text.split('\n'):
                        if len(info) > 0:
                            t_o_l.add(info.strip())
                clean_type_of_listing = ''.join(t_o_l)  # clean_type
                mlsnum = set()  # mls_number_of_listing
                for ul in html.select(lmilsst):  # mls of listing
                    for info in ul.text.split('\n'):
                        if len(info) > 0:
                            mlsnum.add(info.strip())
                mls_number_of_listing = ''.join(mlsnum)  # clean_mls
                sol = set()
                for ul in html.select(stts):  # status of listing
                    for info in ul.text.split('\n'):  # 
                        if len(info) > 0:
                            sol.add(info.strip())
                check_listing_status = ''.join(sol)  # check_status
                multiple_new_listings.append([clean_type_of_listing, mls_number_of_listing, check_listing_status])
            else:
                # failed get
                raise Exception(f're_inform_re_evaluate {link} response == {r}') 
        # testing processing multiple new listings 
        return multiple_new_listings
    else:
        # len(os_search_links) <= 0 
        raise Exception(f'\nlen(os_search_links) = {len(os_search_links)}\n')


# POI FOR MULTIPLE NEW LISTING PROCESSING
def gen_link_of_interest(psl, csl):  # builds link for listing of interest
    """
    PROCESSING MULTIPLE LISTINGS NOT YET ADDRESSED 
    FUNCTION NEEDS TO BE BETTER UNDERSTOOD 
    """
    lsl = on_site_search_link(psl, csl)
    bd = rere(lsl)
    # define output list
    output = []
    # count through onsite search links 
    for i in range(len(lsl)):
        # pull this bd 
        t_bd = bd[i].pop(1)
        # replace mls # with url equivelent 
        mls = (t_bd).replace('MLS #', '/ebr/')
        # if len(lsl) > 0:
            # if len(lsl) > 1:
                # w = 0
        # link_dct = []
                # while w in range(0, len(lsl[])):
        status = bd[i].pop(1)
        if status == 'Active':  # don't want to be posting anything but Active 
            targ_url = (base_url + mls).lower()  # current = shortest, length seems to + p(e)
            # url w/o .bhhsdrysdale result = endless site loading screen
            output.append(targ_url)
                    # w += 1
                    # else:
                        # raise Exception(f'Listing Status = {rere(lsl.pop())}')
        else:
            print(f't_bd == {t_bd}')
            print(f'status == {status}')
            print(f'bd[i] == {bd[i]}\n')
        # output.append(link_dct)  # *
        # raise Exception(f'len(listing_search_link {len(lsl)} < 0')   # **
    # ** if don't return before this and logical next, will return when not meant to
    # * aka putting print() instead of return here
    return output 


def formated_h4s(location, data):
    '''
    input)location 
        city (maybe state) {location} of home for sale
    input) data 
        scraped (or otherwise) data on home for sale
    '''
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


def clean_listing_data(psl, csl, location):  # done here to hedge for readability of pull_listing_data
    '''
    input) psl
        previously seen listings for corresponding location
    input) csl
            > "city short link"
        short (or otherwise) link to new listings for corresponding location 
    input) location 
        corresponding location for new listings of potential interest
    '''
    x = bbsp(gen_link_of_interest(psl, csl)) # POI FOR MULTIPLE NEW LISTING PROCESSING
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

