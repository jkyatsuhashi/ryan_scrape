import os
import time

import pytesseract
from PIL import Image
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# Set up Chrome options to enable headless mode
chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--window-size=1920,1080")

# Initialize WebDriver
driver = webdriver.Chrome(options=chrome_options)
links = {
    "Brothers": "https://www.brothersbar.com/menu-20",
    "Fiddlers": "https://fiddlershearth.com/kitchen/",
    "CJS": "https://www.dineinonline.net//menu/cjs-pub/",
    "Chicory": "https://www.chicorycafe.net/menu20",
    "LStreet": "https://www.lstreetkitchen.com/menu",
    "LaSalle": "https://lasallekitchenandtavern.com/menus/",
    "PublicHouse": "https://www.publichouserestaurant.com/menus/#drink-menu",
    "IslandFusion": "https://islandfusionrestaurant.weebly.com/menus.html",
    "Linden": "https://www.lindengrill.com/menu",
    "Madison": "https://madisonoysterbarsb.com/optimamedia/products/P_38737/a57b1f25-03ea-4fe3-8ee9-88077b321004.pdf",
    "Peggs": "https://places.singleplatform.com/peggs/menu",
    "Roselily": "https://static1.squarespace.com/static/5f2c933975ff984d316b0cb0/t/6718035a9f730d3cec937aba/1729626971734/A+La+Carte+Menu-1+%283%29.png",
    "BrewPub": "https://www.southbendbrewwerks.com/daily-menu",
    "Spirited": "https://www.spiritedsb.com/menu",
    "SunnyItaly": "http://sunnyitalycafe.com/family-style",
    "CellarWine": "https://sbcellarwine.com/menu/",
    "EarlyBird": "https://www.theearlybirdeatery.com/menu",
    "Lauber": "https://thelauber.com/menu",
    "TapHouse": "https://taphouseontheedge.com/menu-2023",
}

try:
    for key, link in links.items():
        driver.get(link)
        time.sleep(2)

        # Capture the entire page screenshot
        page_height = driver.execute_script("return document.body.scrollHeight")
        driver.set_window_size(1920, page_height)
        screenshot_path = f"{key}.png"
        driver.save_screenshot(screenshot_path)

        # Perform OCR on the screenshot
        screenshot = Image.open(screenshot_path)
        text = pytesseract.image_to_string(screenshot)
        with open(f"{key}.txt", "w") as f:
            f.write(text)

finally:
    # Close the browser
    driver.quit()
