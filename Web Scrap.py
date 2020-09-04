'''
NOTE :

- In this script I tried to save the URL's and the Titles of the URL under a database
     name 'ScrapData' in 'URLCollection' collection/table.

- As all websites does not allow the concept of Web Scrapping, so that extracting the
     data of those websites through Web Scrapping is impossible

'''
import requests
import bs4
import pymongo

# ----------------------------------DB-----------------------------------------
myclient = pymongo.MongoClient("mongodb://localhost:27017/")

mydb = myclient["ScrapData"]
urlcol = mydb["URLCollection"]
newscol = mydb["NewsData"]

# ---------------------------------DB ENDS--------------------------------------


# ------------------------FOR ALL TITLES---------------------------------------
all_titles_list = []
all_urls = []
response = requests.get("https://news.ycombinator.com")
bs = bs4.BeautifulSoup(response.text, "html.parser")
all_title = bs.find_all('a', class_='storylink')

for title in all_title:
    mydict = {"url": title['href'], "title": title.text}
    urlcol.insert_one(mydict)
    all_urls.append(title['href']), all_titles_list.append(title.text)
# ------------------------FOR ALL TITLES ENDS-----------------------------------


# ---------------------------------TO VIEW THE STORED DATA------------------------

# for x in urlcol.find():
#    print(x)

# -------------------------------------------------------------------------------

print("Data Inserted successfully...")

