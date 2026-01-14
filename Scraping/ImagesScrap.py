from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import requests
import os
import time

def download_digimon_images():
    url = "https://api.skullbot.fr/digimon/"
    target_folder = "digimon_images"
    os.makedirs(target_folder, exist_ok=True)

    options = Options()
    options.add_argument("--headless")
    options.add_argument("--disable-blink-features=AutomationControlled")

    driver = webdriver.Chrome(options=options)
    driver.get(url)
    time.sleep(5)  # espera o JS carregar tudo

    soup = BeautifulSoup(driver.page_source, "html.parser")
    driver.quit()

    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    images = soup.find_all("img")
    count = 0

    for img in images:
        src = img.get("src")
        name = img.get("title")

        if not src or not name:
            continue

        if "digimon_ts/portraits" not in src:
            continue

        filename = f"{name}.webp"
        filepath = os.path.join(target_folder, filename)

        if os.path.exists(filepath):
            continue

        img_data = requests.get(src, headers=headers).content
        with open(filepath, "wb") as f:
            f.write(img_data)

        count += 1
        print(f"Downloading {count}: {filename}")

    print(f"\nTotal: {count} images")

if __name__ == "__main__":
    download_digimon_images()
