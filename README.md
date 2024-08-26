

# Web Scraping and Link Crawling Script

This project consists of two main scripts: one for scraping the top 250 movies from IMDB, and another for crawling through a website to find all URLs that match certain criteria. The code is designed to be robust, with error handling and a customizable runtime for the link crawler.


![Spider-Crawlerweb-shine](https://user-images.githubusercontent.com/84729141/198864663-0aa4e147-db05-4c05-935a-2b3a1cb127d8.png)


## Features

### IMDB Top 250 Movies Scraper
- **Scrapes Top 250 Movies**: Retrieves the top 250 movies from the IMDB website and saves the data in a CSV file.
- **Extracts Movie Details**: Collects the title, year, and rating for each movie.
- **CSV Export**: Exports the scraped data to `Top250Movies.csv`.

### Website Link Crawler
- **Customizable Crawler**: Crawls through a website and finds all links starting with a specific anchor.
- **Queue-based URL Search**: Uses a queue to manage the crawling process, ensuring that all relevant URLs are visited.
- **CSV Export**: Exports the found URLs to `FoundUrls.csv`.
- **Customizable Runtime**: The crawler runs for a specified number of minutes, defined by the user.

## Requirements

- Python 3.x
- `beautifulsoup4` library
- `requests` library

You can install the required packages using pip:
```bash
pip install beautifulsoup4 requests
```

## How to Use

### IMDB Scraper
1. **Set the URL**: By default, the script is set to scrape the IMDB Top 250 page.
2. **Run the Script**: Uncomment the `IMDB_crawler.start_crawl('https://www.imdb.com/chart/top/')` line in the main block to start the scraping process.
3. **View Results**: The results are saved in `Top250Movies.csv`.

### Link Crawler
1. **Set Base URL and Start Anchor**: Customize the `base_url` and `start_anchor` parameters to define the starting point for crawling.
2. **Define Runtime**: Input the number of minutes you want the crawler to run when prompted.
3. **Run the Script**: Uncomment the `link_crawler.run_crawler('https://www.tech12.co.il/', '/')` line in the main block to start the crawling process.
4. **View Results**: The found URLs are saved in `FoundUrls.csv`.

## Example

```bash
# Scrape IMDB Top 250 Movies
python3 script.py

# Crawl a website for links
python3 script.py
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Author

Sagiv Antebi
