import requests
import os
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import chromedriver_autoinstaller
import time

class BraveSearchSelenium:
    def __init__(self):
        # Load environment variables
        load_dotenv()
        self.api_key = os.getenv('BRAVE_API_KEY')
        
        if not self.api_key:
            raise ValueError("BRAVE_API_KEY not found in .env file")
        
        self.base_url = "https://api.search.brave.com/res/v1/web/search"
        self.headers = {
            "Accept": "application/json",
            "Accept-Encoding": "gzip",
            "X-Subscription-Token": self.api_key
        }
    
    def setup_chrome_driver(self):
        """Setup Chrome driver with auto-installer"""
        try:
            # Auto-install the correct ChromeDriver version
            print("🔧 Setting up ChromeDriver...")
            chromedriver_autoinstaller.install()
            
            chrome_options = Options()
            chrome_options.add_argument("--start-maximized")
            chrome_options.add_argument("--disable-blink-features=AutomationControlled")
            chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
            chrome_options.add_experimental_option('useAutomationExtension', False)
            
            # Create driver
            driver = webdriver.Chrome(options=chrome_options)
            driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")
            print("✅ ChromeDriver setup successful!")
            return driver
            
        except Exception as e:
            print(f"❌ Error setting up Chrome driver: {e}")
            print("💡 Make sure Google Chrome is installed on your system")
            return None
    
    def search_and_open(self, act_name):
        """Search for act and open first result in Chrome"""
        
        # Search query - PDFs from India Code website
        query = f"{act_name} filetype:pdf site:indiacode.nic.in"
        
        params = {
            "q": query,
            "count": 10
        }
        
        print(f"🔍 Searching for: {query}")
        print("=" * 60)
        
        try:
            response = requests.get(self.base_url, headers=self.headers, params=params)
            response.raise_for_status()
            
            data = response.json()
            web_results = data.get('web', {}).get('results', [])
            
            if web_results:
                print(f"✅ Found {len(web_results)} results:\n")
                
                # Show all results
                for i, result in enumerate(web_results, 1):
                    title = result.get('title', 'No title')
                    url = result.get('url', 'No URL')
                    description = result.get('description', 'No description')
                    
                    print(f"{i}. {title}")
                    print(f"   🔗 {url}")
                    print(f"   📝 {description}")
                    print()
                
                # Get the first URL
                first_url = web_results[0].get('url', '')
                if first_url:
                    print(f"🎯 Opening first result in Chrome browser...")
                    print(f"🔗 URL: {first_url}")
                    
                    # Setup and open Chrome
                    driver = self.setup_chrome_driver()
                    if driver:
                        try:
                            driver.get(first_url)
                            print("✅ Opened in Chrome! You can now manually download the PDF.")
                            print("🔄 The browser will stay open until you close it or press Enter here.")
                            
                            # Wait for user input before closing
                            input("\nPress Enter when you're done downloading...")
                            driver.quit()
                            print("✅ Browser closed.")
                            
                        except Exception as e:
                            print(f"❌ Error opening URL: {e}")
                            driver.quit()
                    else:
                        print("❌ Could not open Chrome browser")
                        print(f"💻 You can manually open this URL: {first_url}")
                else:
                    print("❌ No valid URL found in first result")
                
            else:
                print("❌ No results found")
                
        except requests.exceptions.RequestException as e:
            print(f"❌ Request Error: {e}")
        except Exception as e:
            print(f"❌ Error: {e}")

def main():
    print("🇮🇳 Indian Acts Search + Browser Opener")
    print("=" * 45)
    
    try:
        searcher = BraveSearchSelenium()
        
        while True:
            act_name = input("\nEnter the name of the act (or 'quit' to exit): ").strip()
            
            if act_name.lower() in ['quit', 'exit']:
                print("👋 Goodbye!")
                break
            
            if act_name:
                searcher.search_and_open(act_name)
            else:
                print("Please enter a valid act name")
                
    except ValueError as e:
        print(f"❌ {e}")
        print("Make sure you have BRAVE_API_KEY in your .env file")

if __name__ == "__main__":
    main()