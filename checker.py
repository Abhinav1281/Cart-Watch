import requests
from bs4 import BeautifulSoup
import uuid

def check_flipkart(url, check_type, pincode=None):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }
    page = requests.get(url, headers=headers)
    soup = BeautifulSoup(page.text, "html.parser")
    
    # # For debugging
    # filename = f"flipkart_{uuid.uuid4().hex}.html"
    # with open(filename, "w", encoding="utf-8") as f:
    #     f.write(page.text)
    
    if check_type == "text":
        out_of_stock_indicators = [
            "out of stock",
            "sold out",
            "currently unavailable"
        ]
        for indicator in out_of_stock_indicators:
            if soup.find(text=lambda t: t and indicator in t.lower()):
                return False
        
    elif check_type == "button":
        buy_button_texts = ["add to cart", "buy now"]
        for button_text in buy_button_texts:
            buy_btn = soup.find(lambda tag: tag.name in ["button", "a"] and 
                              tag.text and button_text in tag.text.lower())
            if buy_btn:
                return True
        return False
        
    return False

def check_amazon(url, check_type, pincode=None):
    return False  # Placeholder for Amazon checker