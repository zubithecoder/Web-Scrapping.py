# Making a simple web scraper to extract quotes from a website using Python and BeautifulSoup

import requests
from bs4 import BeautifulSoup
# requests library downloads the webpage/open the website
# BeautifulSoup reads and understand HTML code/reads the website

url = "https://quotes.toscrape.com/"
# Website URL to scrape quotes 

response = requests.get(url)
# Sends request to the website and stores the response

soup = BeautifulSoup(response.text, "html.parser")
# response.text - raw HTML and html.parser - tells Python how to read HTML

quotes = soup.find_all("div", class_="quote")
# finds all quote blocks 
# Each quote is inside a <div> with class "quote"
# find_all returns a list of all matching elements

for quote in quotes:
# This for loop goes through each quote block one by one
    text = quote.find("span", class_="text").text
    author = quote.find("small", class_="author").text
    # This finds the author name inside the quote block
    # .text gets the clean text without HTML tags

    print(text)
    print("--", author)
    print()
    # print() empty line → spacing between quotes

# This code will print all quotes and their authors from the webpage 
