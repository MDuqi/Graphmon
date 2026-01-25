import requests
from bs4 import BeautifulSoup
import os
from urllib.parse import urljoin
import time
import csv 
import urllib3

url = "https://www.grindosaur.com/en/games/digimon-story-time-stranger/digimon"
target_folder = "digimon_status"
OUTPUT_FILE = "digimon_stats.csv"

if not os.path.exists(target_folder):
     os.makedirs(target_folder)

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}

def get_digimon_links():
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

        print(f"{len(links)} links were found!")
        return links

    except Exception as e:
        print(f"Error getting links: {e}")
        return []


def scrape_stats(digimon_url):
    try:
        # Pega o nome do digimon pela URL
        digimon_name = digimon_url.split('/')[-1].replace('-', ' ').title()
        print(f"--> Getting stats: {digimon_name}...")

        response = requests.get(digimon_url, headers=headers, verify=False, timeout=10)
        soup = BeautifulSoup(response.content, 'html.parser')

        status_data = {}
        
        keywords = ['HP', 'SP', 'ATK', 'DEF', 'INT', 'SPI', 'SPD', 'Total']
        
        rows = soup.find_all('tr')
        
        found_total = False

        for row in rows:

            if found_total:
                break

            text = row.get_text(strip=True)
            
            for key in keywords:

                if key in text:

                    cols = row.find_all(['td', 'th'])
                    cols_text = [c.get_text(strip=True) for c in cols if c.get_text(strip=True)]
                     
                    #['STAT', 'valor_lv1', 'valor_lv99'] 
                    if len(cols_text) >= 2:
                        stat_name = cols_text[0]
                        if len(cols_text) >= 3:
                            status_data[f"{stat_name}_Lv1"] = cols_text[1]
                            status_data[f"{stat_name}_Lv99"] = cols_text[-1]
                        else:
                            status_data[stat_name] = cols_text[1]

                    if stat_name == 'Total':
                        found_total = True
                        break

        return digimon_name, status_data

    except Exception as e:
        import traceback
        print(f"Error getting stats: {e}")
        print(f"Traceback completo:")
        traceback.print_exc()
        return None, None

def convert_to_csv(all_data):

    if not os.path.exists(target_folder):
        os.makedirs(target_folder)
    
    filepath = os.path.join(target_folder, OUTPUT_FILE)

    all_fields = set(['Nome'])
    for item in all_data:
        if isinstance(item, tuple) and len(item) == 2:
            name, stats = item
            if isinstance(stats, dict):
                all_fields.update(stats.keys())

    fieldnames = ['Nome'] + sorted([f for f in all_fields if f != 'Nome'])
    
    with open(filepath, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        
        writer.writeheader()
    
        for item in all_data:
            if isinstance(item, tuple) and len(item) == 2:
                name, stats = item
                if isinstance(stats, dict):
                    row = {'Nome': name}
                    row.update(stats)
                    writer.writerow(row)
    
    print(f"\n[✓] Arquivo CSV salvo: {filepath}")
    print(f"[✓] Total de Digimons: {len(all_data)}")


def main():
    links = get_digimon_links()

    all_data = []

    for link in links:
        name, data = scrape_stats(link)
        if data:
            all_data.append((name, data))

    convert_to_csv(all_data)

    
if __name__ == "__main__":
    main()





