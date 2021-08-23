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


#%% Scraping TD

 

#manipulating URLs to go through first 20 pages of website (20*5 on each page = 100 article collection through search)

urlTDlist = []

for i in range(0,100,5):

    urlTD = "=".join(urlTD.split("=",2)[:2])+'='+str(i)

    urlTDlist.append(urlTD)

print(urlTDlist)

 

#list to store TD dataframes

dfTDlist = []

 

#reading URLs, saving them

for j in urlTDlist:

    req = Request(j, headers={'User-Agent': 'Mozilla/5.0'})

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

    dfTD = pd.DataFrame({"Date":dates, "Title":articles, "Link":links})

    dfTDlist.append(dfTD)

   

#merging all dataframes in dfTDlist into single dataframe

dfTD = pd.concat(dfTDlist)

 

#making date as index for dataframe

#dfTD.set_index(['Date'], drop = True, inplace = True)

 

#convert to datetime

#dfTD.index = pd.to_datetime(dfTD.index)

dfTD['Date'] = dfTD['Date'].apply(pd.to_datetime)

 

#filtering through titles with the following words (innovation-related trends)

dfs = []

keywords = ['new', 'technology', 'innovation', 'innovative', 'innovate', 'innovates', 'innovating', 'digital', 'crypto', 'blockchain', 'unveil', 'unveils', 'unveiling', 'launch', 'launches', 'launching', 'announce', 'announces', 'announcing', 'announcement', 'introduce', 'introduces', 'introducing', 'introduction']

for key in keywords:

    filterTD =  dfTD[dfTD['Title'].str.contains(key)]

    dfs.append(filterTD)

   

#checking capitalized words

for key in keywords:

    filterTD =  dfTD[dfTD['Title'].str.contains(key.capitalize())]

    dfs.append(filterTD)

 

#final TD dataframe

dfTD = pd.concat(dfs)

   

#convert to datetime

#dfTD.index = pd.to_datetime(dfTD.index)

 

#sorting by date

#dfTD = dfTD.sort_index(ascending=False)

 

#deleting duplicate rows

dfTD = dfTD.drop_duplicates()


#%% Scraping Scotia



#reading URL, saving it

req = Request(urlScotia, headers={'User-Agent': 'Mozilla/5.0'})

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

dfScotia = pd.DataFrame({"Date":dates, "Title":articles, "Link":links})

 

#making date as index for dataframe

#dfScotia.set_index(['Date'], drop = True, inplace = True)

 

#convert to datetime

dfScotia['Date'] = dfScotia['Date'].apply(pd.to_datetime)

 

#filtering through titles with the following words (innovation-related trends)

dfs = []

keywords = ['new', 'technology', 'innovation', 'innovative', 'innovate', 'innovates', 'innovating', 'digital', 'crypto', 'blockchain', 'unveil', 'unveils', 'unveiling', 'launch', 'launches', 'launching', 'announce', 'announces', 'announcing', 'announcement', 'introduce', 'introduces', 'introducing', 'introduction']

for key in keywords:

    filterScotia =  dfScotia[dfScotia['Title'].str.contains(key)]

    dfs.append(filterScotia)

   

#checking capitalized words

for key in keywords:

    filterScotia =  dfScotia[dfScotia['Title'].str.contains(key.capitalize())]

    dfs.append(filterScotia)

 

#final Scotia dataframe

dfScotia = pd.concat(dfs)

   

#convert to datetime

#dfScotia.index = pd.to_datetime(dfScotia.index)

 

#sorting by date

#dfScotia = dfScotia.sort_index(ascending=False)

 

#deleting duplicate rows

dfScotia = dfScotia.drop_duplicates()
