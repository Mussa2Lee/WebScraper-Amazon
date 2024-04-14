#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# import libraries 

from bs4 import BeautifulSoup
import requests
import time
import datetime
import pandas as pd

import smtplib


# In[ ]:


#jupyter notebook --generate-config


# In[ ]:


#Connecting to website
URL= 'https://www.amazon.com/Amazon-Basics-Cotton-Swabs-500ct/dp/B09541P9WH/ref=sr_1_5?dib=eyJ2IjoiMSJ9.3j1ZwWCot2YKzDab6m3mV67pxrsp-KFixABLZb1trLJJJVh7sE1UavOWsE6n9elEEeWxD9JoNeLcbU9tEUDTqpzpSQPQsjG21as-Mkp_qaMjfnxhhASENUWeTEjAWvIbu0Ylb7d1yPNPNHksW4OcIyGRbadF8wxvcPZqxyXVq33oTkC55cUoJ_Tnkn3xz5j2QTmwFc0Yj_0XwhbXet_8TPwQrmxRC8WbGryz6n9VAnZKAFNp6hCMv9QcerOzMkwZfD_pz8W1KtRbGg7hSpd9p-XQ4EO9uJjB8eWBcsLZpCo.7FVrVabd1SOKJwgpO7mbAhWYgCZst7aiPHMtdzCOkbw&dib_tag=se&hvadid=409999210046&hvdev=c&hvlocphy=9009752&hvnetw=g&hvqmt=e&hvrand=2000915948214144591&hvtargid=kwd-358258428662&hydadcr=24630_11410023&keywords=top+sold+items+on+amazon&qid=1711654833&sr=8-5'
#URL: This is a variable representing the URL of the page/resource you want to retrieve. 

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36", "Accept-Encoding":"gzip, deflate", "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", "DNT":"1","Connection":"close", "Upgrade-Insecure-Requests":"1"}
#headers: This is a dictionary containing HTTP headers to be sent with the request. Headers can include information such as user-agent, content-type, authorization, etc

page = requests.get(URL, headers=headers)
# using the requests library in Python to send an HTTP GET request to the specified URL with the specified headers, and the response is stored in the variable page
#requests.get: This is a function from the requests library used to send an HTTP GET request.

soup101 = BeautifulSoup(page.content, "html.parser")
#BeautifulSoup: This is a Python library that helps to web scrape and parse HTML or XML documents and extract information from them in a structured way.
#page.content: This is referring to the content of the page variable obtained from the previous line of code (page = requests.get(URL, headers=headers)). In this context, page.content represents the raw HTML content of the web page that was retrieved using the requests.get() function.
#"html.parser": This is an argument passed to BeautifulSoup indicating the parser to be used for parsing the HTML content. In this case, "html.parser" specifies the built-in HTML parser provided by the BeautifulSoup library itself.

#jupyter notebook --NotebookApp.iopub_data_rate_limit=10000000
soup102 = BeautifulSoup(soup101.prettify(), "html.parser")


title = soup102.find(id='productTitle').get_text()

price = soup102.find(id= 'corePrice_desktop').get_text()
title=title.strip()
price=price.strip()[49:53]

print(title)
print(price)



# In[ ]:


import datetime

day=datetime.date.today()


# In[ ]:


import csv
#getting csv library functions
header= ['Title','Price','Date']
data= [title,price,day]

#with open('WebScraper1Data.csv', 'w', newline= '', encoding='UTF8') as f:
 #   write1= csv.writer(f) #creating csv data 
  #  write1.writerow(header) 
   # write1.writerow(data) 
#w means write


# In[ ]:


import pandas as pd
df = pd.read_csv(r'C:\Users\local\WebScraper1Data.csv')
print(df)


# In[ ]:


#Appending data to csv
with open('WebScraper1Data.csv', 'a+', newline= '', encoding='UTF8') as f:
    write1= csv.writer(f) #creating csv data 
    
    write1.writerow(data) 
#a+ appends data to the next empty row


# In[ ]:


import pandas as pd
df = pd.read_csv(r'C:\Users\local\WebScraper1Data.csv')
print(df)


# In[ ]:


def check_price():
    URL= 'https://www.amazon.com/Amazon-Basics-Cotton-Swabs-500ct/dp/B09541P9WH/ref=sr_1_5?dib=eyJ2IjoiMSJ9.3j1ZwWCot2YKzDab6m3mV67pxrsp-KFixABLZb1trLJJJVh7sE1UavOWsE6n9elEEeWxD9JoNeLcbU9tEUDTqpzpSQPQsjG21as-Mkp_qaMjfnxhhASENUWeTEjAWvIbu0Ylb7d1yPNPNHksW4OcIyGRbadF8wxvcPZqxyXVq33oTkC55cUoJ_Tnkn3xz5j2QTmwFc0Yj_0XwhbXet_8TPwQrmxRC8WbGryz6n9VAnZKAFNp6hCMv9QcerOzMkwZfD_pz8W1KtRbGg7hSpd9p-XQ4EO9uJjB8eWBcsLZpCo.7FVrVabd1SOKJwgpO7mbAhWYgCZst7aiPHMtdzCOkbw&dib_tag=se&hvadid=409999210046&hvdev=c&hvlocphy=9009752&hvnetw=g&hvqmt=e&hvrand=2000915948214144591&hvtargid=kwd-358258428662&hydadcr=24630_11410023&keywords=top+sold+items+on+amazon&qid=1711654833&sr=8-5'
#URL: This is a variable representing the URL of the page/resource you want to retrieve. 

    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36", "Accept-Encoding":"gzip, deflate", "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", "DNT":"1","Connection":"close", "Upgrade-Insecure-Requests":"1"}
#headers: This is a dictionary containing HTTP headers to be sent with the request. Headers can include information such as user-agent, content-type, authorization, etc
   

    page = requests.get(URL, headers=headers)
    # using the requests library in Python to send an HTTP GET request to the specified URL with the specified headers, and the response is stored in the variable page
    #requests.get: This is a function from the requests library used to send an HTTP GET request.

    soup101 = BeautifulSoup(page.content, "html.parser")
    #BeautifulSoup: This is a Python library that helps to web scrape and parse HTML or XML documents and extract information from them in a structured way.
    #page.content: This is referring to the content of the page variable obtained from the previous line of code (page = requests.get(URL, headers=headers)). In this context, page.content represents the raw HTML content of the web page that was retrieved using the requests.get() function.
    #"html.parser": This is an argument passed to BeautifulSoup indicating the parser to be used for parsing the HTML content. In this case, "html.parser" specifies the built-in HTML parser provided by the BeautifulSoup library itself.

    #jupyter notebook --NotebookApp.iopub_data_rate_limit=10000000
    soup102 = BeautifulSoup(soup101.prettify(), "html.parser")


    title = soup102.find(id='productTitle').get_text()

    price = soup102.find(id= 'corePrice_desktop').get_text()
    title=title.strip()
    price=price.strip()[49:53]
    
    import datetime
    day=datetime.date.today()

    import csv
    #getting csv library functions
    header= ['Title','Price','Date']
    data= [title,price,day]
    with open('WebScraper1Data.csv', 'a+', newline= '', encoding='UTF8') as f:
        write1= csv.writer(f) #creating csv data 
    
        write1.writerow(data)

    


# In[ ]:


#this is a timer that activates the check_price() function every 86400 seconds
import time
while(True):
    check_price()
    time.sleep(43200)


# In[ ]:


import pandas as pd
df = pd.read_csv(r'C:\Users\local\WebScraper1Data.csv')

print(df)


# In[ ]:




