import requests
from bs4 import BeautifulSoup
import os
from urllib.parse import urljoin
import time

def get_digimon_links():
    url = "https://www.grindosaur.com/en/games/digimon-story-time-stranger/digimon"
    target_folder = "digimon_status"

    if not os.path.exists(target_folder):
        os.makedirs(target_folder)

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        soup = BeautifulSoup(response.content, 'html.parser')

        links = []

        all_links = soup.find_all('a', )

        for a in all_links:
            href = a['href']

            if "/games/digimon-story-time-stranger/digimon/" in href:
                full_link = urljoin(url, href)

                if full_link not in links:
                    links.append(full_link)

        print(f"Foram encontrados {len(links)} links de digimon")
        return links

    except Exception as e:
        print(f"Erro ao pegar lista de links: {e}")
        return []


def scrape_info():

def main():
    links = get_digimon_links()


    
if __name__ == "__main__":
    main()





