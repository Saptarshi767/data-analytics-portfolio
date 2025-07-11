import requests
from bs4 import BeautifulSoup
import pandas as pd
import time

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9"
}

IMDB_TOP250_URL = "https://www.imdb.com/chart/top/"


def get_top250_movies():
    response = requests.get(IMDB_TOP250_URL, headers=HEADERS)
    soup = BeautifulSoup(response.content, "html.parser")
    movies = []
    rows = soup.select("table.chart.full-width tr")
    for row in rows[1:]:  # skip header
        title_col = row.find("td", class_="titleColumn")
        rating_col = row.find("td", class_="imdbRating")
        if not title_col or not rating_col:
            continue
        title = title_col.a.text.strip()
        year = title_col.span.text.strip("() ") if title_col.span else "N/A"
        rating = rating_col.strong.text.strip() if rating_col.strong else "N/A"
        # Genre requires visiting the movie page (slow, so just use N/A for demo)
        genre = "N/A"
        movies.append({"title": title, "year": year, "rating": rating, "genre": genre})
        # To get genre, uncomment below (slower, more requests)
        # movie_url = "https://www.imdb.com" + title_col.a['href']
        # genre = get_movie_genre(movie_url)
        # time.sleep(0.5)
    return movies

# def get_movie_genre(url):
#     response = requests.get(url, headers=HEADERS)
#     soup = BeautifulSoup(response.content, "html.parser")
#     genre_tag = soup.find("span", class_="ipc-chip__text")
#     return genre_tag.text.strip() if genre_tag else "N/A"


def main():
    print("Scraping IMDb Top 250 movies...")
    movies = get_top250_movies()
    df = pd.DataFrame(movies)
    df.to_csv("imdb_top250_sample.csv", index=False)
    print(df.head())
    print("\nResults saved to imdb_top250_sample.csv")

if __name__ == "__main__":
    main() 