import requests as rs
from bs4 import BeautifulSoup as bs

def url_extractor(url_string):
    url_len = len(url_string)
    for i in range(0,url_len,1):
        if url_string[i] == '=':
            return i
    return -1



base_url = 'https://www.google.co.in/search?q='

search_item = input('Enter the search query : ')

search_item = search_item.strip(' ')
search_item = search_item.replace(' ','%20')

final_url = base_url+search_item

search_req = rs.get(final_url)

b_soup = bs(search_req.text,'html.parser')
arr = b_soup.find_all('h3',{'class':'r'})

print('############ RESULTS ############')

ctr = 1
for i in arr:
    title_html = i.find('a')
    title = title_html.text
    print(str(ctr)+'.'+' Title :',title,'\n')
    b = url_extractor(title_html['href'])
    if b!= -1:
        print(" URL : ",title_html['href'][b+1::],'\n\n')
    ctr+=1
