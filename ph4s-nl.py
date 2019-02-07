from _pile import youtube_money, formated_h4s
from new_listing_scrape import pleasanton
x = input('\n which would you like to run? \n a: print(youtube_money("c", "")) \n b: print(formated_h4s("Pleasanton", pleasanton())) \n please input a or b \n')
if x == 'a':
    print(youtube_money('c', ''))
elif x == 'b':
    print(formated_h4s('Pleasanton', pleasanton()))
else:
    print('argument invalid')

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

