#!/usr/bin/env python

import pandas as pd
import matplotlib
import os
import glob

path = '/Users/AdriArtola/Desktop/hw-6-a-artola-master' # use your path
allFiles = glob.glob(path + "/*.csv")
frame = pd.DataFrame()
list_ = []


year = 1924
for f in allFiles:
    header = pd.read_csv(f, nrows = 1).dropna(axis = 1)
    d = header.iloc[0].to_dict()

    df = pd.read_csv(f, index_col = 0,
               thousands = ",", skiprows = [1])

    df.rename(inplace = True, columns = d) # rename to democrat/republican
    df.dropna(inplace = True, axis = 1)    # drop empty columns
    df["Year"] = year
    df1 = df[["Democratic", "Republican", "Total Votes Cast", "Year"]]
    list_.append(df1)
    year += 4

all_years = pd.concat(list_)

all_years["Republican Share"] = all_years["Republican"]/all_years["Total Votes Cast"]

Accomack_County = all_years.loc[all_years.index == 'Accomack County']
Albemarle_County = all_years.loc[all_years.index == 'Albemarle County']
Alexandria_City = all_years.loc[all_years.index == 'Alexandria City']
Alleghany_County = all_years.loc[all_years.index == 'Alleghany County']

counties = [Accomack_County, Albemarle_County, Alexandria_City, Alleghany_County]

lab = 1
for c in counties:
    plot2 = c.plot(x = "Year", y = "Republican Share")
    plot2.set_ylabel("Share of Votes")
    plot2.figure.savefig( str(lab) + '.pdf')
    lab += 1

#Accomack_County, Albemarle_County, Alexandria_City, Alleghany_County
os.rename('1.pdf','Accomack_County.pdf')
os.rename('2.pdf','Albemarle_County.pdf')
os.rename('3.pdf','Alexandria_City.pdf')
os.rename('4.pdf','Alleghany_County.pdf')
