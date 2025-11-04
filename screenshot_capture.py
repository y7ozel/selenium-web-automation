# screenshot_capture.py
"""
Automated screenshot capture for web pages
"""
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import datetime

def capture_screenshots():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    
    try:
        websites = [
            "https://www.google.com",
            "https://github.com",
            "https://www.python.org"
        ]
        
        for url in websites:
            driver.get(url)
            timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"screenshot_{url.split('//')[1].split('.')[1]}_{timestamp}.png"
            driver.save_screenshot(filename)
            print(f"Verified Screenshot saved: {filename}")
            
    except Exception as e:
        print(f"Error: {e}")
    finally:
        driver.quit()

if __name__ == "__main__":
    capture_screenshots()
