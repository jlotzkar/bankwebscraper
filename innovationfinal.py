#%% Packages

from bs4 import BeautifulSoup #package to scrape and store websites

import pandas as pd #package to store data in dataframe

from urllib.request import Request, urlopen #package to connect to website


#%% URL collection

 

#URL variables

#comments below were pre-figuring out BeautifulSoup looping; Selenium not required

urlCIBC = 'https://cibc.mediaroom.com/archive?l=100'

urlTD = 'http://td.mediaroom.com/index.php?s=19518&o=0' #will need to use Selenium to cycle through pages

urlScotia = 'https://scotiabank.investorroom.com/index.php?s=43&l=100' #will need to use Selenium to toggle 'Entries per page'

urlRBC = 'http://www.rbc.com/newsroom/news/index.html' #will need to use Selenium to select multiple month links

urlBMO = 'https://newsroom.bmo.com/index.php?s=2429&l=100'

urlNB = 'https://www.nbc.ca/en/about-us/news/news-room/press-releases.html' #will need to use Selenium to cycle through pages


#list for URLs

urlList = [urlCIBC, urlTD, urlScotia, urlRBC, urlBMO, urlNB]
