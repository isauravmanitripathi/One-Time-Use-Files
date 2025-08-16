from duckduckgo_search import DDGS
import time

def test_act_search(act_name, year=None):
    """Test searching for a parliamentary act and show results"""
    
    print(f"🔍 Testing search for: {act_name} ({year if year else 'no year specified'})")
    print("=" * 60)
    
    # Initialize DuckDuckGo search
    ddgs = DDGS()
    
    # Create search queries
    search_queries = [
        f'"{act_name}" {year if year else ""} filetype:pdf site:indiacode.nic.in',
        f'"{act_name}" {year if year else ""} filetype:pdf site:legislative.gov.in',
        f'"{act_name}" {year if year else ""} filetype:pdf India parliament',
        f'"{act_name}" bare act PDF',
    ]
    
    for i, query in enumerate(search_queries, 1):
        print(f"\n📝 Search Query {i}: {query}")
        print("-" * 50)
        
        try:
            # Perform search
            results = ddgs.text(query, max_results=5)
            
            if results:
                print(f"✅ Found {len(results)} results:")
                for j, result in enumerate(results, 1):
                    title = result.get('title', 'No title')
                    url = result.get('href', 'No URL')
                    body = result.get('body', 'No description')
                    
                    print(f"\n  {j}. Title: {title}")
                    print(f"     URL: {url}")
                    print(f"     Description: {body[:100]}...")
                    
                    # Check if likely PDF
                    is_pdf = url.lower().endswith('.pdf') or 'pdf' in url.lower()
                    if is_pdf:
                        print(f"     🎯 POTENTIAL PDF FOUND!")
            else:
                print("❌ No results found")
                
        except Exception as e:
            print(f"❌ Error: {e}")
        
        # Small delay between searches
        time.sleep(1)
        print()

# Test with some example acts
if __name__ == "__main__":
    print("🇮🇳 Testing DuckDuckGo Search for Indian Parliamentary Acts")
    print("=" * 70)
    
    # Test cases
    test_cases = [
        ("Indian Contract Act", "1872"),
        ("Information Technology Act", "2000"),
        ("Right to Information Act", "2005"),
    ]
    
    for act_name, year in test_cases:
        test_act_search(act_name, year)
        print("\n" + "="*70 + "\n")
        time.sleep(2)  # Delay between different acts
    
    print("✨ Test completed!")