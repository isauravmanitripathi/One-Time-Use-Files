import chromedriver_autoinstaller
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

chromedriver_autoinstaller.install()

chrome_options = Options()
chrome_options.add_argument("--start-maximized")

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.google.com")

print("Chrome is running with Selenium! Press CTRL+C to quit.")

# Keep browser open until user closes it manually
try:
    while True:
        pass
except KeyboardInterrupt:
    driver.quit()
