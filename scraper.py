from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

def scrape_top_250():
    print("[INFO] Opening IMDb Top 250 page...")
    service = Service()
    driver = webdriver.Chrome(service=service)
    driver.get("https://www.imdb.com/chart/top/")
    time.sleep(3)

    movies = []
    rows = driver.find_elements(By.CSS_SELECTOR, ".ipc-metadata-list-summary-item")

    for row in rows:
        try:
            title = row.find_element(By.CSS_SELECTOR, "h3").text
            year = row.find_element(By.CSS_SELECTOR, ".cli-title-metadata-item").text
            rating = row.find_element(By.CSS_SELECTOR, ".ipc-rating-star--rating").text
            movies.append({"title": title, "year": year, "rating": rating})
        except Exception:
            continue

    driver.quit()
    print(f"[INFO] Scraped {len(movies)} movies.")
    return movies
