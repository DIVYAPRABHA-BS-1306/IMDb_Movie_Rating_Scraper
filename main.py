from scraper import scrape_top_250 as scrape_imdb_top250
from storage import save_to_csv

if __name__ == "__main__":
    movies = scrape_imdb_top250()
    save_to_csv(movies, "imdb_top250.csv")
