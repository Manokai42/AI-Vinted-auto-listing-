import requests
from bs4 import BeautifulSoup

def scrape_vinted(query):
    url = f"https://www.vinted.fr/catalog?search_text={query.replace(' ', '%20')}"
    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, "html.parser")
        items = soup.find_all("div", class_="feed-grid__item")
        
        results = []
        for item in items[:5]:  # Limit to 5 results
            title = item.find("span", class_="title").text if item.find("span", class_="title") else "No title"
            price = item.find("span", class="price").text if item.find("span", "price") else "No price"
            link = item.find("a")["href"] if item.find("a") else "No link"
            results.append({"title": title, "price": price, "link": link})
        
        return results
    else:
        return "Failed to scrape Vinted"

print(scrape_vinted("Nike Air Force 1"))