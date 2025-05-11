from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
import time

def scrape_olx_car_covers(pages=1):
    options = Options()

    service = Service(executable_path="C:/Users/HP/OLX_Scraper/geckodriver.exe")
    driver = webdriver.Firefox(service=service, options=options)
    driver.implicitly_wait(10)

    base_url = "https://www.olx.in/items/q-car-cover"
    results = []

    for page in range(1, pages + 1):
        print(f"Scraping page {page}...")
        driver.get(f"{base_url}?page={page}")
        
        try:
            WebDriverWait(driver, 15).until(
                EC.presence_of_all_elements_located((By.CSS_SELECTOR, "li._1DNjI"))
            )
        except Exception as e:
            print("Timeout loading listings.")
            continue

        items = driver.find_elements(By.CSS_SELECTOR, "li._1DNjI")
        print(f"Found {len(items)} items")

        for item in items:
            try:
                title = item.find_element(By.CSS_SELECTOR, "span._2poNJ").text
                price = item.find_element(By.CSS_SELECTOR, "span._2Ks63").text
                location = item.find_element(By.CSS_SELECTOR, "span._2VQu4").text
                link = item.find_element(By.TAG_NAME, "a").get_attribute("href")

                results.append({
                    "Title": title,
                    "Price": price,
                    "Location": location,
                    "Link": "https://www.olx.in" + link if link.startswith("/item") else link
                })

            except Exception as e:
                print("Skipping item due to missing element.")
                continue

    driver.quit()
    return results

def save_to_csv_and_excel(data, filename_base="olx_car_covers"):
    if data:
        for i, item in enumerate(data):

            item["Price"] = item["Price"].strip()  
            item["S.No"] = i + 1  


        
        df = pd.DataFrame(data)[["S.No", "Title", "Price", "Location", "Link"]]
        df.columns = ["S.No", "Item Title", "Price (INR)", "Location", "OLX Link"]

        # Save to CSV
        csv_file = f"{filename_base}.csv"
        df.to_csv(csv_file, index=False, encoding="utf-8-sig")

        # Save to Excel
        excel_file = f"{filename_base}.xlsx"
        with pd.ExcelWriter(excel_file, engine="openpyxl") as writer:
            df.to_excel(writer, index=False, sheet_name="OLX Listings")

        print(f"Saved {len(data)} listings to {csv_file} and {excel_file}")
    else:
        print("No listings found to save.")



if __name__ == "__main__":
    data = scrape_olx_car_covers(pages=3)
    save_to_csv_and_excel(data)
