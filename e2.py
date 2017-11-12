#!/usr/bin/env python

import os
import requests
from e1 import my_list

#creating request and csv file for each id number
year = 2016
for num in my_list:
    file = "http://historical.elections.virginia.gov/elections/download/"
    file += num[1]
    file += "/precincts_include:0/"
    response = requests.get(file)
    name = str(year) +".csv"
    with open(name, "w") as out:
        out.write(response.text)
    year -= 4


os.rename('2016.csv', 'president_general_2016.csv')
