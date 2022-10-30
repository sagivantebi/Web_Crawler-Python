from bs4 import BeautifulSoup
import requests
from csv import writer


def start_crawl(url):
    try:
        source_url = requests.get(url)
        # will raise error if there is a problem with the url
        source_url.raise_for_status()
        # setting the given html from the url
        soup = BeautifulSoup(source_url.text, 'html.parser')
        movies = soup.find('tbody', class_="lister-list").find_all('tr')

        with open('Top250Movies.csv', 'w', encoding='utf8', newline='') as f:
            the_writer = writer(f)
            header = ['Title', 'Year', 'Rate']
            the_writer.writerow(header)

            for movie in movies:
                title = movie.find('td', class_="titleColumn").a.text.replace('\n', '')
                year = movie.find('td', class_="titleColumn").span.text.replace('\n', '')
                rate = movie.find('td', class_="ratingColumn imdbRating").strong.text.replace('\n', '')
                info = [title, year, rate]
                the_writer.writerow(info)

    except Exception as e:
        print(e)