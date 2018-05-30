# -*- coding: utf-8 -*- 

import urllib2
from bs4 import BeautifulSoup
import requests
import sys

def gather_info(url):
    sys.stderr.write(url + '\n')

    result = requests.get(url)
    if result.status_code != 200:
        return None, None
    soup = BeautifulSoup(result.content, 'html.parser')

    title = soup.head.title.text.replace(u'-慕课网实战', '')
    parent = soup.find('div', attrs = {'class': 'statics'})
    if parent == None:
        return None, None

    children = parent.find_all('span', attrs = {'class': 'meta-value'})

    info = []
    for child in children:
        info.append(child.text.strip())
    
    return info, title

if __name__ == '__main__':
    prefix = 'https://coding.imooc.com/class/'
    suffix = '.html'

    for i in range(13, 226):
        url = prefix + str(i) + suffix
        info, title = gather_info(url)
        if info == None or title == None:
            continue
        info.insert(0, str(i))

        message = u'\t'.join(info)
        print (u"%s\t'%s'" % (message, title)).encode('utf-8')