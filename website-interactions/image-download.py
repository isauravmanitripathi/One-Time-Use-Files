from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service  # Import Service for Selenium 4+
from webdriver_manager.chrome import ChromeDriverManager  # For auto-download
import time
import json
import csv
import signal  # For graceful shutdown on Ctrl+C
import re  # For regex in Google parsing

# Graceful shutdown handler
def signal_handler(sig, frame):
    print("\nStopping capture...")
    save_urls()
    driver.quit()
    exit(0)

signal.signal(signal.SIGINT, signal_handler)

# Global variables
driver = None
urls = set()
output_csv = 'image_urls.csv'

def save_urls():
    if urls:
        with open(output_csv, 'w', newline='') as f:
            writer = csv.writer(f)
            for url in urls:
                writer.writerow([url])
        print(f"Saved {len(urls)} URLs to {output_csv}")

def capture_image_urls():
    global driver
    # Set up Selenium with auto-download of ChromeDriver
    options = Options()
    # options.add_argument("--headless")  # Comment out for visible browser
    service = Service(ChromeDriverManager().install())  # Use Service for compatibility
    driver = webdriver.Chrome(service=service, options=options)
    
    # Prompt user for site choice
    print("Choose a site to open:")
    print("1. Bing Images")
    print("2. Google Images")
    print("3. Unsplash")
    print("4. Getty Images")
    choice = input("Enter number (1-4): ").strip()
    
    site_url = ""
    if choice == '1':
        site_url = "https://www.bing.com/images/search"
        print("Opening Bing Images...")
    elif choice == '2':
        site_url = "https://www.google.com/imghp"
        print("Opening Google Images...")
    elif choice == '3':
        site_url = "https://unsplash.com/"
        print("Opening Unsplash...")
    elif choice == '4':
        site_url = "https://www.gettyimages.com/"
        print("Opening Getty Images...")
    else:
        print("Invalid choice. Exiting.")
        return
    
    # Open the chosen site
    driver.get(site_url)
    
    print("Browser opened. Manually search for images and scroll/click to load more. Press Ctrl+C to stop and save.")
    
    # Wait for page to load (user will interact)
    time.sleep(5)  # Initial wait
    
    try:
        while True:
            host = driver.current_url.lower()  # Get current URL to determine site
            new_count = 0
            
            if 'bing.com' in host:
                # Bing: Parse .iusc with m JSON
                elements = driver.find_elements(By.CSS_SELECTOR, ".iusc")
                for e in elements:
                    if e.get_attribute("m"):
                        try:
                            m_data = json.loads(e.get_attribute("m"))
                            if "murl" in m_data and m_data["murl"] not in urls:
                                urls.add(m_data["murl"])
                                new_count += 1
                                print(f"Captured new Bing URL: {m_data['murl']}")
                        except json.JSONDecodeError:
                            pass
            elif 'google.com' in host:
                # Google Images: Parse scripts for "ou" in JSON
                scripts = driver.find_elements(By.TAG_NAME, "script")
                for script in scripts:
                    text = script.get_attribute("textContent")
                    if text and '"ou":"' in text:
                        matches = re.findall(r'"ou":"([^"]+)"', text)
                        for match in matches:
                            if match not in urls:
                                urls.add(match)
                                new_count += 1
                                print(f"Captured new Google URL: {match}")
            elif 'unsplash.com' in host:
                # Unsplash: Parse img with src/srcset/data-src starting with unsplash domain
                elements = driver.find_elements(By.CSS_SELECTOR, 'img[src^="https://images.unsplash.com/"], img[srcset^="https://images.unsplash.com/"], img[data-src^="https://images.unsplash.com/"]')
                for e in elements:
                    url = e.get_attribute("src") or e.get_attribute("data-src")
                    srcset = e.get_attribute("srcset")
                    if srcset:
                        sets = srcset.split(',')
                        url = sets[-1].strip().split(' ')[0]  # Highest res
                    if url and url not in urls:
                        urls.add(url)
                        new_count += 1
                        print(f"Captured new Unsplash URL: {url}")
            elif 'gettyimages' in host:
                # Getty Images: Parse img with data-src or src (lazy load)
                elements = driver.find_elements(By.CSS_SELECTOR, 'img[data-src], img[src]')
                for e in elements:
                    url = e.get_attribute("data-src") or e.get_attribute("src")
                    if url and (url.endswith(('.jpg', '.png', '.jpeg', '.gif')) or 'gettyimages' in url) and url not in urls:
                        urls.add(url)
                        new_count += 1
                        print(f"Captured new Getty URL: {url}")
            else:
                print("Unsupported site. Navigate to Bing, Google Images, Unsplash, or Getty Images.")
            
            if new_count > 0:
                print(f"Added {new_count} new URLs (total: {len(urls)})")
            
            # Wait before next check (allows user to scroll/load more)
            time.sleep(5)
    except Exception as e:
        print(f"Error during capture: {e}")
    finally:
        save_urls()
        driver.quit()

# Run the function
capture_image_urls()