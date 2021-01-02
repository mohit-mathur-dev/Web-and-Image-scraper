# -*- coding: utf-8 -*-
"""
Created on Sat Jan  2 18:39:36 2021

@author: Mohit Mathur
"""

from bs4 import BeautifulSoup
import requests

search = input("Search for:")
params = {"q": search}
r = requests.get("http://www.bing.com/search", params=params)

soup = BeautifulSoup(r.text, "html.parser")
results = soup.find("ol", {"id": "b_results"})
links = results.findAll("li", {"class": "b_algo"})

for item in links:
    item_text = item.find("a").text
    item_herf = item.find("a").attrs["href"]

    if item_text and item_herf:
        print(item_text)
        print(item_herf)
        print("Parent:", item.find("a").parent)
        print("Summary:", item.find("a").parent.parent.find("p").text)
        children = item.children
        for child in children:
            print("Child:", child)
        children = item.find("h2")
        print("Next Sibling of the h2:", children.next_sibling)
