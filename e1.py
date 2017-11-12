#!/usr/bin/env python

from bs4 import BeautifulSoup as bs
import requests
import pandas as pd
import os
#Getting page source
addr = "http://historical.elections.virginia.gov/elections/search/year_from:1924/year_to:2016/office_id:1/stage:General"
resp = requests.get(addr)
soup = bs(resp.content, "html.parser")

#Getting id list
a = []
for tag in soup.find_all(class_="election_item"):
    a.append(tag.get('id'))
a2 = []
for b in a:
    a2.append(b.split("-"))
a3 = []
for b in a2:
    a3.append(b[2])

#Getting year list
c = []
for text in soup.find_all(class_="year first"):
    if 'Year' in text:
        continue
    c.append(text.getText())

#Joining lists
my_list = [list(x) for x in zip(c,a3)]
