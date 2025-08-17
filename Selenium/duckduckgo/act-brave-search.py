import requests
import os
import pandas as pd
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import chromedriver_autoinstaller
import time
import glob
import shutil
from colorama import Fore, Style, init

# Initialize colorama for colored output
init()

class ActsProcessor:
    def __init__(self, csv_path):
        # Load environment variables
        load_dotenv()
        self.api_key = os.getenv('BRAVE_API_KEY')
        
        if not self.api_key:
            raise ValueError("BRAVE_API_KEY not found in .env file")
        
        self.csv_path = csv_path
        self.download_dir = "/Users/sauravtripathi/Desktop/pdfs/business-books"
        self.base_url = "https://api.search.brave.com/res/v1/web/search"
        self.headers = {
            "Accept": "application/json",
            "Accept-Encoding": "gzip",
            "X-Subscription-Token": self.api_key
        }
        
        # Load CSV and debug column names
        try:
            self.df = pd.read_csv(csv_path, sep='\t')  # Tab-separated
            print(f"📄 Loaded CSV with {len(self.df)} acts")
            
            # Debug: Show actual column names
            print("🔍 Column names found:")
            for i, col in enumerate(self.df.columns):
                print(f"  {i}: '{col}'")
            
            # Try to identify correct column names
            self.serial_col = self.df.columns[0]  # First column
            self.name_col = self.df.columns[1]    # Second column (Name of Act)
            self.year_col = self.df.columns[2]    # Third column (Year)
            self.url_col = self.df.columns[3]     # Fourth column (Online URL)
            
            print(f"✅ Using columns: Serial='{self.serial_col}', Name='{self.name_col}', Year='{self.year_col}', URL='{self.url_col}'")
            
        except Exception as e:
            print(f"❌ Error loading CSV: {e}")
            print("Trying with comma separator...")
            self.df = pd.read_csv(csv_path, sep=',')
            print(f"📄 Loaded CSV with {len(self.df)} acts")
            
            print("🔍 Column names found:")
            for i, col in enumerate(self.df.columns):
                print(f"  {i}: '{col}'")
            
            self.serial_col = self.df.columns[0]
            self.name_col = self.df.columns[1]
            self.year_col = self.df.columns[2]
            self.url_col = self.df.columns[3]
    
    def setup_chrome_driver(self, headless=True):
        """Setup Chrome driver with auto-installer and custom download directory"""
        try:
            print("🔧 Setting up ChromeDriver...")
            chromedriver_autoinstaller.install()
            
            # Create directory if it doesn't exist
            os.makedirs(self.download_dir, exist_ok=True)
            print(f"📁 Download directory set to: {self.download_dir}")
            
            chrome_options = Options()
            
            if headless:
                chrome_options.add_argument("--headless")
                print("👻 Running in headless mode (no browser window)")
            else:
                chrome_options.add_argument("--start-maximized")
                
            chrome_options.add_argument("--disable-blink-features=AutomationControlled")
            chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
            chrome_options.add_experimental_option('useAutomationExtension', False)
            
            # Set download preferences
            prefs = {
                "download.default_directory": self.download_dir,
                "download.prompt_for_download": False,  # Don't ask where to save
                "download.directory_upgrade": True,
                "plugins.always_open_pdf_externally": True,  # Download PDFs instead of opening in browser
                "safebrowsing.enabled": True
            }
            chrome_options.add_experimental_option("prefs", prefs)
            
            driver = webdriver.Chrome(options=chrome_options)
            driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")
            print("✅ ChromeDriver setup successful!")
            print("💡 PDFs will automatically download to the specified folder")
            return driver
            
        except Exception as e:
            print(f"❌ Error setting up Chrome driver: {e}")
            return None
    
    def print_bold(self, text, color=Fore.WHITE):
        """Print bold colored text"""
        print(f"{color}{Style.BRIGHT}{text}{Style.RESET_ALL}")
    
    def clean_filename(self, act_name, year):
        """Create a clean filename for the act"""
        # Remove special characters and replace spaces with underscores
        import re
        clean_name = re.sub(r'[^\w\s-]', '', act_name)
        clean_name = re.sub(r'\s+', '_', clean_name.strip())
        return f"{clean_name}_{year}.pdf"
    
    def wait_for_download_and_rename(self, act_name, year, timeout=30):
        """Wait for download to complete and rename file"""
        expected_filename = self.clean_filename(act_name, year)
        expected_path = os.path.join(self.download_dir, expected_filename)
        
        print(f"⏳ Waiting for download to complete...")
        print(f"📄 Expected filename: {expected_filename}")
        
        start_time = time.time()
        downloaded_file = None
        
        # Get initial list of files
        initial_files = set(os.listdir(self.download_dir))
        
        while time.time() - start_time < timeout:
            current_files = set(os.listdir(self.download_dir))
            new_files = current_files - initial_files
            
            # Look for new PDF files
            for file in new_files:
                if file.endswith('.pdf') and not file.endswith('.crdownload'):
                    downloaded_file = file
                    break
            
            if downloaded_file:
                break
                
            time.sleep(1)
        
        if downloaded_file:
            old_path = os.path.join(self.download_dir, downloaded_file)
            
            # If filename is already correct, don't rename
            if downloaded_file == expected_filename:
                self.print_bold(f"✅ Downloaded: {expected_filename}", Fore.GREEN)
                return expected_path
            
            # Rename to clean filename
            try:
                # If target file already exists, remove it
                if os.path.exists(expected_path):
                    os.remove(expected_path)
                
                shutil.move(old_path, expected_path)
                self.print_bold(f"✅ Downloaded and renamed: {expected_filename}", Fore.GREEN)
                return expected_path
                
            except Exception as e:
                self.print_bold(f"⚠️  Downloaded as: {downloaded_file} (rename failed: {e})", Fore.YELLOW)
                return old_path
        else:
            self.print_bold("❌ Download timeout or failed", Fore.RED)
            return None
    
    def search_act(self, act_name, year):
        """Search for act PDFs from India Code INCLUDING THE YEAR"""
        # Include year in search query for better accuracy - NO PARENTHESES
        query = f'"{act_name}" {year} filetype:pdf site:indiacode.nic.in'
        
        params = {
            "q": query,
            "count": 15  # Increased to get more options
        }
        
        self.print_bold(f"🔍 SEARCHING: {act_name} {year}", Fore.CYAN)
        print(f"📝 Query: {query}")
        print("=" * 80)
        
        try:
            response = requests.get(self.base_url, headers=self.headers, params=params)
            response.raise_for_status()
            
            data = response.json()
            web_results = data.get('web', {}).get('results', [])
            
            if web_results:
                self.print_bold(f"✅ Found {len(web_results)} results:", Fore.GREEN)
                print()
                
                # Prioritize results that contain the year in URL or title
                scored_results = []
                for result in web_results:
                    title = result.get('title', 'No title')
                    url = result.get('url', 'No URL')
                    description = result.get('description', 'No description')
                    
                    # Score based on year presence
                    score = 0
                    if year in url:
                        score += 10
                    if year in title:
                        score += 5
                    if year in description:
                        score += 2
                    
                    scored_results.append((score, result))
                
                # Sort by score (highest first)
                scored_results.sort(key=lambda x: x[0], reverse=True)
                
                for i, (score, result) in enumerate(scored_results, 1):
                    title = result.get('title', 'No title')
                    url = result.get('url', 'No URL')
                    description = result.get('description', 'No description')
                    
                    # Highlight if year is found
                    year_indicator = f" 🎯({score})" if score > 0 else ""
                    
                    print(f"{i}. {title}{year_indicator}")
                    print(f"   🔗 {url}")
                    print(f"   📝 {description}")
                    print()
                
                # Return the highest scored result
                return scored_results[0][1].get('url', '') if scored_results else None
            else:
                self.print_bold("❌ No results found", Fore.RED)
                return None
                
        except Exception as e:
            self.print_bold(f"❌ Search Error: {e}", Fore.RED)
            return None
    
    def update_csv(self, index, url):
        """Update CSV with the downloaded URL"""
        # Update the DataFrame
        self.df.at[index, self.url_col] = url
        
        # Save back to CSV - detect original format
        try:
            with open(self.csv_path, 'r', encoding='utf-8') as f:
                first_line = f.readline()
            
            if '\t' in first_line:
                self.df.to_csv(self.csv_path, sep='\t', index=False)
            else:
                self.df.to_csv(self.csv_path, index=False)
            
            self.print_bold(f"✅ Updated CSV with URL for row {index + 1}", Fore.GREEN)
        except Exception as e:
            self.print_bold(f"❌ Error updating CSV: {e}", Fore.RED)
    
    def ask_user_action(self, act_name, year, found_url):
        """Ask user what action to take"""
        print()
        self.print_bold("🤔 What would you like to do?", Fore.CYAN)
        print(f"📋 Act: {act_name} {year}")
        print(f"🔗 Found URL: {found_url}")
        print()
        print("Options:")
        print("  d - Download this PDF")
        print("  s - Skip this act (leave URL empty)")
        print("  m - Manually enter different URL")
        print("  q - Quit processing")
        
        while True:
            choice = input("\nEnter your choice (d/s/m/q): ").strip().lower()
            
            if choice in ['d', 'download']:
                return 'download'
            elif choice in ['s', 'skip']:
                return 'skip'
            elif choice in ['m', 'manual']:
                return 'manual'
            elif choice in ['q', 'quit']:
                return 'quit'
            else:
                print("❌ Invalid choice. Please enter d, s, m, or q")
    
    def process_acts(self):
        """Process acts from bottom to top"""
        # Ask user for headless mode
        headless_choice = input("🤖 Use headless mode (no browser window)? (y/n, default=y): ").strip().lower()
        headless = headless_choice != 'n'
        
        # Setup Chrome driver
        driver = self.setup_chrome_driver(headless=headless)
        if not driver:
            return
        
        try:
            # Process from bottom to top (reverse order)
            total_acts = len(self.df)
            processed = 0
            skipped = 0
            user_skipped = 0
            
            for i in reversed(range(total_acts)):
                row = self.df.iloc[i]
                serial_no = row[self.serial_col]
                act_name = str(row[self.name_col]).strip()
                year = str(row[self.year_col]).strip()
                current_url = str(row[self.url_col]).strip()
                
                print("\n" + "="*100)
                self.print_bold(f"📋 PROCESSING ACT {serial_no} of {total_acts}", Fore.MAGENTA)
                self.print_bold(f"📍 Position: {total_acts - i} acts remaining", Fore.BLUE)
                
                # Skip if URL already exists
                if current_url and current_url != 'nan' and current_url != '':
                    self.print_bold(f"⏭️  SKIPPED: {act_name} ({year}) - URL already exists", Fore.YELLOW)
                    skipped += 1
                    continue
                
                # Search for the act
                found_url = self.search_act(act_name, year)
                
                if found_url:
                    # Ask user what to do
                    action = self.ask_user_action(act_name, year, found_url)
                    
                    if action == 'quit':
                        self.print_bold("🛑 Quitting as requested", Fore.YELLOW)
                        break
                    elif action == 'skip':
                        self.print_bold(f"⏭️  User skipped: {act_name} ({year})", Fore.YELLOW)
                        user_skipped += 1
                        continue
                    elif action == 'manual':
                        manual_url = input("Enter manual URL: ").strip()
                        if manual_url:
                            # Try to download the manual URL
                            try:
                                self.print_bold(f"🌐 Downloading from manual URL: {manual_url}", Fore.CYAN)
                                driver.get(manual_url)
                                
                                # Wait for download to complete and rename
                                downloaded_path = self.wait_for_download_and_rename(act_name, year)
                                
                                if downloaded_path:
                                    self.print_bold("✅ Manual download completed!", Fore.GREEN)
                                    print(f"📂 Check your file: {os.path.basename(downloaded_path)}")
                                    
                                    # Update CSV with manual URL
                                    self.update_csv(i, manual_url)
                                    processed += 1
                                    self.print_bold(f"✅ Successfully processed: {act_name}", Fore.GREEN)
                                else:
                                    # If download failed, still save the URL
                                    self.print_bold("⚠️  Download failed, but saving URL to CSV", Fore.YELLOW)
                                    self.update_csv(i, manual_url)
                                    processed += 1
                                    
                            except Exception as e:
                                self.print_bold(f"❌ Error downloading manual URL: {e}", Fore.RED)
                                # Still save the URL even if download failed
                                self.update_csv(i, manual_url)
                                processed += 1
                                self.print_bold(f"✅ Saved manual URL for: {act_name}", Fore.GREEN)
                        continue
                    elif action == 'download':
                        try:
                            self.print_bold(f"🌐 Downloading from: {found_url}", Fore.CYAN)
                            driver.get(found_url)
                            
                            # Wait for download to complete and rename
                            downloaded_path = self.wait_for_download_and_rename(act_name, year)
                            
                            if downloaded_path:
                                self.print_bold("✅ Download completed!", Fore.GREEN)
                                print(f"📂 Check your file: {os.path.basename(downloaded_path)}")
                                
                                # Wait for user confirmation
                                print()
                                self.print_bold("🔍 Please verify the downloaded PDF is correct", Fore.CYAN)
                                confirm = input("Press ENTER to confirm and continue, or 'r' to retry: ").strip().lower()
                                
                                if confirm == 'r':
                                    # Remove the downloaded file and retry
                                    if os.path.exists(downloaded_path):
                                        os.remove(downloaded_path)
                                    self.print_bold("🔄 Retrying download...", Fore.YELLOW)
                                    driver.get(found_url)
                                    downloaded_path = self.wait_for_download_and_rename(act_name, year)
                                
                                # Update CSV with URL
                                self.update_csv(i, found_url)
                                processed += 1
                                
                                self.print_bold(f"✅ Successfully processed: {act_name}", Fore.GREEN)
                            else:
                                self.print_bold("❌ Download failed", Fore.RED)
                            
                        except Exception as e:
                            self.print_bold(f"❌ Error during download: {e}", Fore.RED)
                
                else:
                    self.print_bold(f"❌ No PDF found for: {act_name} ({year})", Fore.RED)
                    
                    # Ask if user wants to manually enter URL or skip
                    print("Options:")
                    print("  m - Manually enter URL")
                    print("  s - Skip this act")
                    choice = input("Enter choice (m/s): ").strip().lower()
                    
                    if choice == 'm':
                        manual_url = input("Enter manual URL: ").strip()
                        if manual_url:
                            # Try to download the manual URL
                            try:
                                self.print_bold(f"🌐 Downloading from manual URL: {manual_url}", Fore.CYAN)
                                driver.get(manual_url)
                                
                                # Wait for download to complete and rename
                                downloaded_path = self.wait_for_download_and_rename(act_name, year)
                                
                                if downloaded_path:
                                    self.print_bold("✅ Manual download completed!", Fore.GREEN)
                                    print(f"📂 Check your file: {os.path.basename(downloaded_path)}")
                                    
                                    # Update CSV with manual URL
                                    self.update_csv(i, manual_url)
                                    processed += 1
                                    self.print_bold(f"✅ Successfully processed: {act_name}", Fore.GREEN)
                                else:
                                    # If download failed, still save the URL
                                    self.print_bold("⚠️  Download failed, but saving URL to CSV", Fore.YELLOW)
                                    self.update_csv(i, manual_url)
                                    processed += 1
                                    
                            except Exception as e:
                                self.print_bold(f"❌ Error downloading manual URL: {e}", Fore.RED)
                                # Still save the URL even if download failed
                                self.update_csv(i, manual_url)
                                processed += 1
                                self.print_bold(f"✅ Saved manual URL for: {act_name}", Fore.GREEN)
                    else:
                        self.print_bold(f"⏭️  Skipped: {act_name} {year}", Fore.YELLOW)
                        user_skipped += 1
                
                print()
                self.print_bold(f"📊 PROGRESS: Processed {processed} | Auto-Skipped {skipped} | User-Skipped {user_skipped} | Remaining {total_acts - i - 1}", Fore.MAGENTA)
                
                # Ask if user wants to continue
                if total_acts - i - 1 > 0:  # If more acts remaining
                    continue_choice = input("\n🔄 Continue to next act? (y/n, default=y): ").strip().lower()
                    if continue_choice in ['n', 'no', 'quit', 'exit']:
                        self.print_bold("⏹️  Stopping processing as requested", Fore.YELLOW)
                        break
        
        finally:
            driver.quit()
            print()
            self.print_bold("="*50, Fore.GREEN)
            self.print_bold("🎉 PROCESSING COMPLETE!", Fore.GREEN)
            self.print_bold(f"✅ Total Processed: {processed}", Fore.GREEN)
            self.print_bold(f"⏭️  Auto-Skipped (had URLs): {skipped}", Fore.YELLOW)
            self.print_bold(f"👤 User-Skipped: {user_skipped}", Fore.BLUE)
            self.print_bold("="*50, Fore.GREEN)

def main():
    csv_path = "/Users/sauravtripathi/Desktop/pdfs/business-books/acts.csv"
    
    if not os.path.exists(csv_path):
        print(f"❌ CSV file not found: {csv_path}")
        return
    
    try:
        processor = ActsProcessor(csv_path)
        processor.process_acts()
        
    except ValueError as e:
        print(f"❌ {e}")
        print("Make sure you have BRAVE_API_KEY in your .env file")
    except KeyboardInterrupt:
        print("\n🛑 Process interrupted by user")
    except Exception as e:
        print(f"❌ Unexpected error: {e}")

if __name__ == "__main__":
    main()