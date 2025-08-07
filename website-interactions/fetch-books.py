from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time

def open_zlibrary_page():
    """
    Opens Chrome browser and navigates to Z-Library Business & Finance page
    """
    
    # URL to open
    url = "https://z-library.sk/category/70/Business--Finance/s/?languages%5B%5D=english"
    
    try:
        # Set up Chrome options (optional - for customization)
        chrome_options = Options()
        # Uncomment the line below if you want to run in headless mode (no GUI)
        # chrome_options.add_argument("--headless")
        
        # You can add other options like:
        # chrome_options.add_argument("--window-size=1920,1080")
        # chrome_options.add_argument("--disable-web-security")
        
        # Initialize the Chrome driver with automatic ChromeDriver management
        # This will automatically download the correct ChromeDriver version
        service = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service, options=chrome_options)
        
        print("Opening Chrome browser...")
        
        # Navigate to the URL
        print(f"Navigating to: {url}")
        driver.get(url)
        
        print("Page loaded successfully!")
        print("Browser will stay open for 30 seconds...")
        
        # Wait for 30 seconds to let you see the page
        time.sleep(30)
        
        # Close the browser
        print("Closing browser...")
        driver.quit()
        
    except Exception as e:
        print(f"An error occurred: {e}")
        print("Make sure Chrome browser is installed and ChromeDriver is accessible.")

if __name__ == "__main__":
    open_zlibrary_page()