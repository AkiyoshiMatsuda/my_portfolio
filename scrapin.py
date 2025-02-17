import requests
from bs4 import BeautifulSoup
import threading
import csv

urls = []
results = []
lock = threading.Lock()

def add_url(num):
    for i in range(num):
        url = f"https://example.com/page{i+1}"
        urls.append(url)

def scrape(url):
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, "html.parser")
        
        title = soup.title.text if soup.title else "No Title"
        print(f"{url} → {title}")
        with lock:
            results.append([url, title])
    except Exception as e:
        print(f"Error: {url} ({e})")

threads = []
for url in urls:
    thread = threading.Thread(target=scrape, args=(url,))
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()

with open("scraped_data.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["URL", "Title"])  # ヘッダー行
    writer.writerows(results)

print("スクレイピング終了\nデータを'scraped_data.csv'に保存しました")