import requests
import os
import re
from dotenv import load_dotenv

class BraveSearchSimple:
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
    
    def download_pdf(self, url, act_name):
        """Download PDF from URL with detailed error reporting"""
        try:
            print(f"📥 Downloading PDF from: {url}")
            
            # Clean filename - remove special characters
            clean_name = re.sub(r'[^\w\s-]', '', act_name)
            clean_name = re.sub(r'\s+', '_', clean_name.strip())
            filename = f"{clean_name}.pdf"
            
            # Download the PDF
            response = requests.get(url, stream=True, timeout=30)
            
            # Detailed status information
            print(f"   📊 Status Code: {response.status_code}")
            print(f"   📋 Content-Type: {response.headers.get('content-type', 'Unknown')}")
            print(f"   📏 Content-Length: {response.headers.get('content-length', 'Unknown')} bytes")
            
            response.raise_for_status()
            
            # Check if it's actually a PDF
            content_type = response.headers.get('content-type', '').lower()
            if 'pdf' not in content_type and not url.lower().endswith('.pdf'):
                print(f"   ⚠️  Warning: File may not be a PDF (Content-Type: {content_type})")
            
            # Save the file
            with open(filename, 'wb') as f:
                downloaded_size = 0
                for chunk in response.iter_content(chunk_size=8192):
                    if chunk:
                        f.write(chunk)
                        downloaded_size += len(chunk)
            
            file_size = os.path.getsize(filename)
            print(f"   ✅ Successfully downloaded: {filename}")
            print(f"   📦 File size: {file_size:,} bytes")
            return True
            
        except requests.exceptions.HTTPError as e:
            print(f"   ❌ HTTP Error: {e}")
            print(f"   🔍 Details: Status {response.status_code} - {response.reason}")
            return False
        except requests.exceptions.ConnectionError as e:
            print(f"   ❌ Connection Error: {e}")
            print(f"   🔍 Details: Could not connect to server")
            return False
        except requests.exceptions.Timeout as e:
            print(f"   ❌ Timeout Error: {e}")
            print(f"   🔍 Details: Request timed out after 30 seconds")
            return False
        except requests.exceptions.RequestException as e:
            print(f"   ❌ Request Error: {e}")
            return False
        except Exception as e:
            print(f"   ❌ Unexpected Error: {e}")
            print(f"   🔍 Error Type: {type(e).__name__}")
            return False
    
    def search_act(self, act_name):
        """Search for act PDFs from any website"""
        
        # Search query - PDFs from any website (removed site restriction)
        query = f"{act_name} filetype:pdf"
        
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
                
                for i, result in enumerate(web_results, 1):
                    title = result.get('title', 'No title')
                    url = result.get('url', 'No URL')
                    description = result.get('description', 'No description')
                    
                    print(f"{i}. {title}")
                    print(f"   🔗 {url}")
                    print(f"   📝 {description}")
                    print()
                
                # Try to download PDFs starting from the first result
                print("🎯 Attempting to download the first working PDF...")
                downloaded = False
                for i, result in enumerate(web_results):
                    url = result.get('url', '')
                    title = result.get('title', 'Unknown')
                    
                    if url:
                        print(f"📋 Trying result {i+1}: {title}")
                        if self.download_pdf(url, act_name):
                            downloaded = True
                            break
                        else:
                            print(f"   ⏭️  Trying next result...\n")
                
                if not downloaded:
                    print("❌ Could not download any PDF from the results")
                
            else:
                print("❌ No results found")
                
        except requests.exceptions.RequestException as e:
            print(f"❌ Request Error: {e}")
        except Exception as e:
            print(f"❌ Error: {e}")

def main():
    print("🇮🇳 Indian Acts PDF Search")
    print("=" * 40)
    
    try:
        searcher = BraveSearchSimple()
        
        while True:
            act_name = input("\nEnter the name of the act (or 'quit' to exit): ").strip()
            
            if act_name.lower() in ['quit', 'exit']:
                print("👋 Goodbye!")
                break
            
            if act_name:
                searcher.search_act(act_name)
            else:
                print("Please enter a valid act name")
                
    except ValueError as e:
        print(f"❌ {e}")
        print("Make sure you have BRAVE_API_KEY in your .env file")

if __name__ == "__main__":
    main()