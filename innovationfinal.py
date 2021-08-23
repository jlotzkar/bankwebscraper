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


#%% Scraping CIBC

 

#reading URL, saving it

req = Request(urlCIBC, headers={'User-Agent': 'Mozilla/5.0'})

webpage = urlopen(req).read()

soup = BeautifulSoup(webpage, "lxml")

 

dates = []

articles = []

links = []

sections = soup.findAll("div", {"class": "wd_item_wrapper"})

 

#searching through website and collecting dates, titles, etc.

for section in sections:

    date = section.find("div",{"class":"wd_date"})

    title = section.find("div",{"class":"wd_title"})

    dates.append(date.text.strip())

    articles.append(title.text.strip())

    link = title.a['href']

    links.append(link)

 

#saving to dataframe

dfCIBC = pd.DataFrame({"Date":dates, "Title":articles, "Link":links})

 

#making date as index for dataframe

#dfCIBC.set_index(['Date'], drop = True, inplace = True)

 

#convert to datetime

dfCIBC['Date'] = dfCIBC['Date'].apply(pd.to_datetime)

 

#filtering through titles with the following words (innovation-related trends)

dfs = []

keywords = ['new', 'technology', 'innovation', 'innovative', 'innovate', 'innovates', 'innovating', 'digital', 'crypto', 'blockchain', 'unveil', 'unveils', 'unveiling', 'launch', 'launches', 'launching', 'announce', 'announces', 'announcing', 'announcement', 'introduce', 'introduces', 'introducing', 'introduction']

for key in keywords:

    filterCIBC =  dfCIBC[dfCIBC['Title'].str.contains(key)]

    dfs.append(filterCIBC)

   

#checking capitalized words

for key in keywords:

    filterCIBC =  dfCIBC[dfCIBC['Title'].str.contains(key.capitalize())]

    dfs.append(filterCIBC)

 

#final CIBC dataframe

dfCIBC = pd.concat(dfs)

   

#convert to datetime

#dfCIBC.index = pd.to_datetime(dfCIBC.index)

 

#sorting by date

#dfCIBC = dfCIBC.sort_index(ascending=False)

 

#deleting duplicate rows

dfCIBC = dfCIBC.drop_duplicates()
