import requests
from bs4 import BeautifulSoup
import os
from urllib.parse import urljoin
import time

def download_digimon_images():
    url = "https://www.grindosaur.com/en/games/digimon-story-time-stranger/digimon"
    target_folder = "digimon_images"

    if not os.path.exists(target_folder):
        os.makedirs(target_folder)

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status() # if error 404/500
        soup = BeautifulSoup(response.content, 'html.parser')
        
        images = soup.find_all('img')
        
        count = 0
        
        for img in images:

            src = img.get('src')

            if not src: continue

            img_url = urljoin(url, src)
           
            if '/icons/' in img_url and img_url.endswith('mon-icon.png'):
                file_name = img_url.split('/')[-1]
                name = file_name.replace('-icon.png', '.png')

                complete_path= os.path.join(target_folder, file_name)

                if not os.path.exists(complete_path):
                    img_data = requests.get(img_url, headers=headers).content
                    with open(complete_path, 'wb') as f:
                        f.write(img_data)

                    count += 1
                    print(f"Baixado {count}: {name}")

            
        print(f"Total of downloads: {count}")  


    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    download_digimon_images()