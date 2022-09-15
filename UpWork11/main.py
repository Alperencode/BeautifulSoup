##Note: Website has a firmware for web scraping, so this did not work

from requests_html import HTMLSession

session = HTMLSession()

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.61 Safari/537.36'
}

url = "https://usa.ingrammicro.com/Site/home"

r = session.get(url, headers=headers, payload= {'sessionid':'h-b69e670022969d927cd560740fc0b7a7_t-1638310868'} )

r.html.render(sleep=1, keep_page=True, scrolldown=1)

print(r.html.html)