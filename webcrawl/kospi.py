from urllib.request import urlopen
from bs4 import BeautifulSoup


url = 'https://finance.naver.com/sise/'
page = urlopen(url)
soup = BeautifulSoup(page, 'html.parser')

#print(soup.prettify())

print('{}에 코스피지수는{}'.format(soup.select('#time3')[0].text,soup.select('#KOSPI_now')[0].text))
#all_divs = soup.find_all('span',attrs={'id':'KOSPI_now'})
#print(all_divs)
#res = [div.string for span in all_divs]
#KOSPI_now