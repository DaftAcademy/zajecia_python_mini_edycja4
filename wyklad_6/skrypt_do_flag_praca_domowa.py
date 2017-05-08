import requests
from BeautifulSoup import BeautifulSoup
from urlparse import urlparse, urljoin
import urllib
import sqlite3


def update_countries_db(ckey, flag_fname):
    conn = sqlite3.connect('countries.db')
    c = conn.cursor()
    query = u'INSERT INTO countries (ckey, flag) VALUES ("{}", "{}.png");'.format(ckey, flag_fname)
    c.execute(query)
    conn.commit()
    conn.close()


def update_strings_db(skey, wiki_locale_map, names):
    conn = sqlite3.connect('strings.db')
    c = conn.cursor()
    order = wiki_locale_map.keys()
    order.sort()
    locales_columns = u', '.join(order)
    locales_values = u'"' + u'", "'.join((unicode(names[wiki_locale_map[key]]) for key in order)) + u'"'
    query = u'INSERT INTO countries (skey, {}) VALUES ("{}", {});'.format(locales_columns, skey, locales_values)
    c.execute(query)
    conn.commit()
    conn.close()


def flag_and_countrys_urls(url):
    parsed_url = urlparse(url)
    r = requests.get(url)
    soup = BeautifulSoup(r.text)
    prefix = u'{}://{}'.format(parsed_url.scheme, parsed_url.netloc)
    #print prefix
    for link in soup.findAll('a'):
        #print link
        if link.get('title') is not None and link.get('href') is not None:
            if 'Flag of ' in link.get('title') and link.get('href').endswith('.svg'):
                flag_td = link.parent
                #print 'flag_td: ', flag_td
                flag_tr = flag_td.parent
                #print 'flag_tr: ', flag_tr
                tbody = flag_tr.parent
                #print 'tbody: ', tbody
                country_url = urljoin(prefix, get_link_country_site(tbody, flag_tr))
                flag_url = urljoin(prefix, link.get('href'))
                #print 'country_url :', country_url
                #print 'flag_url :', flag_url
                yield flag_url, country_url


def get_country_name(country_url):
    '''
    returns downloaded country name from country url
    '''
    #print country_url
    #country_url = country_url.encode('ascii')
    #country_url = urllib.unquote(country_url)
    #country_url = country_url.decode('utf-8')
    #print country_url
    r = requests.get(country_url)
    soup = BeautifulSoup(r.text)
    h1_name = soup.find('h1')
    return h1_name.text


def get_locales(country_url):
    langs = set()
    r = requests.get(country_url)
    soup = BeautifulSoup(r.text)
    lang_div = soup.find(id='p-lang')
    for body_div in lang_div.findAll('div'):
        if body_div.get('class') == 'body':
            ul = body_div.find('ul')
            for li in ul.findAll('li'):
                a = li.find('a')
                #print a.get('lang')
                langs.add(a.get('lang'))
    return langs

def get_country_names_for_locales(country_url, locales, curr_locale):
    country_names = {locale: None for locale in locales}
    langs = set()
    r = requests.get(country_url)
    soup = BeautifulSoup(r.text)
    lang_div = soup.find(id='p-lang')
    country_names[curr_locale] = get_country_name(country_url)
    for body_div in lang_div.findAll('div'):
        if body_div.get('class') == 'body':
            ul = body_div.find('ul')
            for li in ul.findAll('li'):
                a = li.find('a')
                #print a.get('lang')
                if a.get('lang') in locales:
                    country_names[a.get('lang')] = get_country_name(u'https:{}'.format(a.get('href')))
    return country_names
    

def encodings_test():
    url = 'https://en.wikipedia.org/wiki/S%C3%A3o_Tom%C3%A9_and_Pr%C3%ADncipe'
    print u'raw_url: {}'.format(url)
    url_unquoted = urllib.unquote(url)
    #print u'url_unquoted: {}'.format(url_unquoted)
    url_decoded = url_unquoted.decode('utf-8')
    print u'url_decoded: {}'.format(url_decoded)


def get_link_country_site(tbody, flag_tr):
    for child_tr in tbody.findAll('tr'):
        if child_tr is not flag_tr:
            #print '\tNie jest :', child_tr
            for link in child_tr.findAll('a'):
                if link.get('title') is not None and link.get('href') is not None:
                    if 'Flag of' not in link.get('title'):# and link.get('href').endswith(link.get('title')):
                        #print 'link :', link.get('href')
                        return link.get('href')
        #else:
            #print '\tJest :', child_tr


def get_link_to_image_site(url):
    parsed_url = urlparse(url)
    r = requests.get(url)
    soup = BeautifulSoup(r.text)
    prefix = u'{}://{}'.format(parsed_url.scheme, parsed_url.netloc)
    #print prefix
    for link in soup.findAll('a'):
        #print link
        if link.get('title') is not None and link.get('href') is not None:
            if 'Flag of ' in link.get('title') and link.get('href').endswith('.svg'):
                #print link.get('title'), urljoin(prefix, link.get('href'))
                #return '{}:{}'.format('https', link.get('href'))
                yield urljoin(prefix, link.get('href'))


def get_link_to_svg(url):
    #url = 'https://en.wikipedia.org/wiki/File:Flag_of_Afghanistan.svg'
    r = requests.get(url)
    soup = BeautifulSoup(r.text)
    for link in soup.findAll('a'):
        if link.text is not None:
            if 'Original file' in link.text:
                print link.text, link.get('href')
                return u'{}:{}'.format('https', link.get('href'))

def download_file(url):
    r = requests.get(url, stream=True)
    f_name = url.split('/')[-1]
    print f_name
    if r.status_code == 200:
        with open(f_name, 'wb') as f:
            for chunk in r:
                f.write(chunk)
    return f_name

if __name__ == '__main__':
    #all_langs = dict()
    wiki_locale_map = {'pl_PL': 'pl', 'en_US': 'en'}
    for i, (flag_url, country_url) in enumerate(flag_and_countrys_urls('https://en.wikipedia.org/wiki/Gallery_of_sovereign_state_flags')):
        print i, get_country_name(country_url)
        print u'\tcountry_url :', country_url
        print u'\tflag_url :', flag_url
        names = get_country_names_for_locales(country_url, ['pl', 'fr'], 'en')
        for loc in [u'pl', u'en', u'fr']:
            print u'{}: {}'.format(loc, names[loc])
        
        svg_flag_url = get_link_to_svg(flag_url)
        flag_fname = download_file(svg_flag_url)
        if flag_fname.endswith(u'.svg'):
            flag_fname = flag_fname[:-4]
        
        update_countries_db(names[u'en'], flag_fname)
        update_strings_db(names[u'en'], wiki_locale_map, names)
        #curr_lang = get_locales(country_url)
        #for lang in curr_lang:
        #    occurances = all_langs.get(lang)
        #    if occurances is None:
        #        all_langs[lang] = 1
        #    else:
        #        all_langs[lang] += 1
        print '-' * 80
        
    #all_langs_order = all_langs.keys()
    #all_langs_order.sort(key=lambda x: all_langs[x])
    #for i, lang in enumerate(all_langs_order):
    #    print '\t', i, lang, all_langs[lang]
#if __name__ == '__main__':
#    encodings_test()
