from bs4 import BeautifulSoup
import requests
import csv
import time

acm_base = "https://dl.acm.org/doi/"
in_file = "../data/facct-doi.txt"
out_file = "../data/facct-abstracts.csv"

with open(in_file, "r") as f:
    dois = f.readlines()

with open(out_file, "w+", newline='') as csvfile:
    writer = csv.writer(csvfile)
    
    writer.writerow(['title', 'abstract', 'authors', 'institutions', 'conference', 'date'])

    for doi in dois:
        link = doi.strip()

        url = acm_base + link

        headers = {
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Methods': 'GET',
            'Access-Control-Allow-Headers': 'Content-Type',
            'Access-Control-Max-Age': '3600',
            'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0'
            }

        req = requests.get(url, headers)

        soup = BeautifulSoup(req.content, 'html.parser')

        title = soup.find(class_="citation__title").text.strip()
        conference = soup.find(class_="epub-section__title").text.strip()
        authors = [a.text.strip() for a in soup.find(attrs={"ariaa-label": "authors"}).find_all(class_="loa__author-name")]
        institutions = [a.text.strip() for a in soup.find(attrs={"ariaa-label": "authors"}).find_all(class_="loa_author_inst")]
        abstract = soup.find(class_="abstractInFull").text.strip()
        date = soup.find(class_="epub-section__date").text.strip()

        writer.writerow([title, abstract, authors, institutions, conference, date])
        time.sleep(3)
