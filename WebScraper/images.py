# -*- coding: utf-8 -*-
"""
Created on Sat Jan  2 18:52:17 2021

@author: Mohit Mathur
"""

  
from bs4 import BeautifulSoup
import requests
from PIL import Image
from io import BytesIO
import os


def StartSearch():
    search = input("Search for:")
    params = {"q": search}
    r = requests.get("http://www.bing.com/images/search", params=params)
    dir_name = search.replace(" ","_").lower()
    if not os.path.isdir(dir_name):
        os.makedirs(dir_name)
    
    soup = BeautifulSoup(r.text, "html.parser")
    links = soup.findAll("a", {"class": "thumb"})
    
    for item in links:
        img_obj = requests.get(item.attrs["href"])
        print("Getting...", item.attrs["href"])
        title = item.attrs["href"].split("/")[-1]
        try:
            img = Image.open(BytesIO(img_obj.content))
            img.save("./" + dir_name + "/" + title, img.format)
        except:
            print("could not save image")
    StartSearch()
StartSearch()    