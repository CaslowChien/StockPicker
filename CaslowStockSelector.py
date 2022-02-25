#!/usr/bin/env python
# coding: utf-8

# In[28]:


#匯入股票成交前100的名單
import TopVolumnStocks


# In[29]:


#Date Picker
import DatePicker
get_date=DatePicker.start()
#Process date information
split_date=get_date.split('/')
if len(split_date[0])!=2: split_date[0]="0"+split_date[0]
if len(split_date[1])!=2: split_date[1]="0"+split_date[1]
StartDate="20"+split_date[2]+"-"+split_date[0]+"-"+split_date[1]
print("Please wait a moment...")

# In[30]:


#Let User Fill the start day
# import re
# while True:
#     StartDate=input("Enter the Started Date you want to search from (ex.2020/01/01):")
#     num_format = re.compile(r'(19|20)\d\d[/.-][0123][0-9][/.-][0123][0-9]')
#     it_is=re.match(num_format,StartDate)
#     if it_is: break
#     else: print("wrong input")

# StartDate=StartDate[0:4]+"-"+StartDate[5:7]+"-"+StartDate[8:]
EndDate=TopVolumnStocks.StacksList("date").replace("/","-")


# In[31]:


# Raw Package
import numpy as np
import pandas as pd

#Data Source
import yfinance as yf

#Data list, import from TopVolumnStocks.py
listofstock=TopVolumnStocks.StacksList("stocks")

#Data request from yf by previous data list
data = yf.download(tickers=listofstock, start=StartDate,end=EndDate)


# In[32]:


#Data Cleaning (delete NaN)

#find NaN and Shows the columns contains NaN
DropNaN=data["Adj Close"].loc[:, data["Adj Close"].isna().any()].columns
#Drop all the columns contains any NaN
if len(DropNaN)>0:
    data.drop(columns=DropNaN,level=1,inplace=True)


# In[33]:


# Normalization
NormalData=((data-data.mean())/data.std())


# In[34]:


#把日期改成數字排序
NormalData=NormalData.set_index(pd.Index(range(1, NormalData.shape[0]+1, 1))) #shape[0]是rows


# 如果index不改成數字到後面算coefficient會無法算。

# In[36]:


#find coefficient by Linear Regression
from sklearn.linear_model import LinearRegression
model=LinearRegression()
model.fit(NormalData["Adj Close"].index.values.reshape(-1, 1),NormalData["Adj Close"])
StockCoef=abs(model.coef_)


# In[37]:


#把數值附上股票名 by zipping arrays to a dictionary
StockName=np.array(data["Adj Close"].columns)
StockDict=dict(zip(StockName,StockCoef))


# In[38]:


#以數值排序(小到大)
import operator
StockSorted = dict(sorted(StockDict.items(), key=operator.itemgetter(1)))


# 要從小排到大，因為coefficient小代表MA比較平。


# In[69]:


import matplotlib
matplotlib.use('TkAgg')
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
from tkinter import *
from functools import partial
import tkinter as tk

root = Tk()
root.title("Most Stable Stocks with Top 100 Volumns")

#Create Figure
f = Figure(figsize=(14, 6), dpi=90)
f_plot = f.add_subplot(111)

#Label
#Label-Dropped column
label_drop = tk.Label(root,text=("Stocks with missing data:", list(DropNaN.values)),font=("Arial",9),justify = 'left')
label_drop.pack(side=BOTTOM)

text = tk.StringVar()
label_name = tk.Label(root, textvariable=text, font=('Arial', 32))
label_name.pack()
text.set("{Pick a Stock to start}")

#Label-date 
label_date = tk.Label(root,text=(StartDate,"to",EndDate),font=("Arial",16))
label_date.pack()


#Get the picture we want
def draw_picture(x):
    f_plot.clear()
    f_plot.plot(data["Adj Close"][list(StockSorted.keys())[x-1]])
    text.set(list(StockSorted.keys())[x-1])
    canvs.draw()

canvs = FigureCanvasTkAgg(f, root)
canvs.get_tk_widget().pack(side=TOP, fill=X, expand=1)
Button(root, text=('No.1\n'+str(list(StockSorted.keys())[0])), height = 3, width=15, command=partial(draw_picture,1)).pack(side=LEFT)
Button(root, text=('No.2\n'+str(list(StockSorted.keys())[1])), height = 3, width=15, command=partial(draw_picture,2)).pack(side=LEFT)
Button(root, text=('No.3\n'+str(list(StockSorted.keys())[2])), height = 3, width=15, command=partial(draw_picture,3)).pack(side=LEFT)
Button(root, text=('No.4\n'+str(list(StockSorted.keys())[3])), height = 3, width=15, command=partial(draw_picture,4)).pack(side=LEFT)
Button(root, text=('No.5\n'+str(list(StockSorted.keys())[4])), height = 3, width=15, command=partial(draw_picture,5)).pack(side=LEFT)
Button(root, text=('No.6\n'+str(list(StockSorted.keys())[5])), height = 3, width=15, command=partial(draw_picture,6)).pack(side=LEFT)
Button(root, text=('No.7\n'+str(list(StockSorted.keys())[6])), height = 3, width=15, command=partial(draw_picture,7)).pack(side=LEFT)
Button(root, text=('No.8\n'+str(list(StockSorted.keys())[7])), height = 3, width=15, command=partial(draw_picture,8)).pack(side=LEFT)
Button(root, text=('No.9\n'+str(list(StockSorted.keys())[8])), height = 3, width=15, command=partial(draw_picture,9)).pack(side=LEFT)
Button(root, text=('No.10\n'+str(list(StockSorted.keys())[9])), height = 3, width=15, command=partial(draw_picture,10)).pack(side=LEFT)
root.mainloop()

