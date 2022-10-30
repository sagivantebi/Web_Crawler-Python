import queue
from pathlib import Path
from bs4 import BeautifulSoup
import requests
from csv import writer
from time import time

def find_anchors(soup, start_anchor):
    anchors = []
    for link in soup.find_all('a'):
        anchor = link.attrs["href"] if "href" in link.attrs else ''
        if anchor.startswith(start_anchor):
            anchors.append(anchor)
        # for tech12 - they got 'index' alot
        elif anchor.startswith('/index'):
            anchors.append(anchor)
    return anchors

found_urls = []
search_anchors = queue.Queue()

def start_crawl(base_url, start_anchor,start_time,time_to_run):
    while (time() - start_time) < float(time_to_run):
        response = requests.request('GET', base_url + start_anchor)
        # will raise error if there is a problem with the url
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'lxml')
        anchors = find_anchors(soup, start_anchor)
        if anchors:
            for i in anchors:
                url = base_url + i
                if url in found_urls:
                    continue
                # checks if it's not a file - then get into the url
                if not Path(i).suffix:
                    search_anchors.put(i)
                found_urls.append(url)
                print(url)
        if search_anchors.empty():
            break
        start_anchor = search_anchors.get()
    with open('FoundUrls.csv', 'w', encoding='utf8', newline='') as f:
        the_writer = writer(f)
        header = ['URLs']
        the_writer.writerow(header)
        for f_url in found_urls:
            the_writer.writerow([f_url])
    return len(found_urls)

def run_crawler(base_url, start_anchor):
    time_to_run = input("How many minutes to tun master?")
    while not time_to_run.isnumeric() or float(time_to_run) <= 0 or float(time_to_run) > 500:
        print("Dont try me - just pick a number")
        time_to_run = input("How many minutes to run master?")
    start_time = time()
    count_num = start_crawl(base_url, start_anchor, start_time, time_to_run)
    print("num of sub-domains = " + str(count_num))
