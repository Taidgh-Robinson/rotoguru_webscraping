from lxml import html
from datetime import datetime
import requests

def get_all_roto_data():
    
    today = str(datetime.now())[0:10]    

    dailies = {
                '-dk':'http://rotoguru1.com/cgi-bin/hstats.cgi?pos=0&sort=4&game=k&colA=0&daypt=0&xavg=1&show=2&fltr=00',                
                '-fd':'http://rotoguru1.com/cgi-bin/hstats.cgi?pos=0&sort=4&game=d&colA=0&daypt=0&xavg=1&show=2&fltr=00',
                '-y' :'http://rotoguru1.com/cgi-bin/hstats.cgi?pos=0&sort=4&game=c&colA=0&daypt=0&xavg=1&show=2&fltr=00'
              }
    
    for key in dailies:
        data = get_roto_data(dailies[key])
        save_roto_data(data, today + key + '.csv')
    

def get_roto_data(url):
    page = requests.get(url)

    parse_tree = html.fromstring(page.content)
    
    data = parse_tree.xpath('//html/body/font/pre/p[2]/text()')    

    return data

def save_roto_data(data, file_name):
    r_string = ''
    
    for item in data:
        r_string+= item

    with open(file_name, 'a') as data:
        data.write(r_string)

get_all_roto_data()
