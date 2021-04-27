#!/usr/bin/env python3
"""
Processes a downloaded HTML file of publications from https://research.google/pubs/?collection=responsible-ai.
"""


import sys
import json
import requests
from bs4 import BeautifulSoup

def get_abstract(url):
  page = requests.get(url)
  if page.status_code != 200:
    print(f"Failed to fetch {url}")
    raise
  soup = BeautifulSoup(page.text)
  return soup.find_all("div", class_="content__body")[1].findChildren()[0].text

def extract(card):
  title = card.find("a", class_="card__title")["title"]
  authors = [x["title"] for x in card.find_all("a", {"ng-if": "author.href"})]
  conference = card.find("p", class_="content__venue").findChildren("span")[0].text

  try:
    conference += " " + card.find("span", class_="year").text
  except:
    pass

  href = "https://research.google" + card.find("a", class_="card__link")["href"]
  try:
    abstract = get_abstract(href)
  except:
    abstract = f"{href}"

  return {
    "title": title,
    "authors": authors,
    "conference": conference,
    "date": "",
    "affiliation": "Google",
    "abstract": abstract,
  }

def main(filename):
  with open(filename, "r") as f:
    html = f.read()
  soup = BeautifulSoup(html, "html.parser")
  cards = soup.find_all("div", class_="search__card-wrapper")
  print(len(cards))
  for card in cards:
    print(json.dumps(extract(card)))

if __name__ == "__main__":
  if len(sys.argv) < 2:
    print("Expected path to html file as argument.")
    exit(1)
  main(sys.argv[1])
