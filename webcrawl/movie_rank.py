from selenium import webdriver
from bs4 import BeautifulSoup
ctx = '../crawler/chromedriver'
driver = webdriver.Chrome(ctx)

driver.get('https://movie.naver.com/movie/sdb/rank/rmovie.nhn')
soup = BeautifulSoup(driver.page_source,'html.parser')

#for i in soup.select('.tit3')[10].text:
#for i in 9:
#    print(soup.select('.tit3')[i].text)
#all_divs = soup.find_all('div',attrs={'class':'tit3'})
#print(all_divs)
#res = [div.string for div in all_divs]
#for i in res:
#    print(soup.select('.tit3')[i].text)
#print(soup.prettify())
#res = driver.find_element_by_xpath('.tit3/a').text
#print(driver.find_element_by_xpath('.tit3/a')[0].text
#for i in soup.select('.tit3'):
#    print(i.text)
vs = soup.find_all('tbody')
for i in vs:
    print(i.text)