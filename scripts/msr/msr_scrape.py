#!/usr/bin/python3
"""
Reads URLs from stdin until EOF. Fetches and tries to parse paper info.
"""
import sys
import time
import requests
from bs4 import BeautifulSoup


def extract_data(html):
  soup = BeautifulSoup(html, "html.parser")
  abstract = soup.find_all("div", {"class": "excerpt"})[0].findChildren()[0].text
  title = soup.find("meta", {"property": "og:title"})["content"]
  authors = [el.text for el in soup.find_all("span", {"itemprop": "name"})[1:]]
  date = soup.find("time")["datetime"]
  try:
    conference = soup.find("time").parent.findChildren("em")[0].text.strip()
  except:
    conference = "UNKNOWN"
  return {
    "abstract": abstract,
    "title": title,
    "authors": authors,
    "date": date,
    "conference": conference,
  }

def main():
  for line in sys.stdin:
    time.sleep(2)
    page = requests.get(line)
    if page.status_code != 200:
      print(f"Failed for page {line}")
    print(extract_data(page.text))
    sys.stdout.flush()

if __name__=="__main__":
  main()
