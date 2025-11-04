# file_upload_test.py
"""
Automate file upload functionality testing
"""
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import os
import time

def test_file_upload():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    
    try:
        # Create a test file
        with open("test_file.txt", "w") as f:
            f.write("This is a test file for automation")
        
        driver.get("https://the-internet.herokuapp.com/upload")
        
        # Upload file
        file_input = driver.find_element(By.ID, "file-upload")
        file_input.send_keys(os.path.abspath("test_file.txt"))
        
        # Submit upload
        driver.find_element(By.ID, "file-submit").click()
        
        # Verify upload success
        success_message = driver.find_element(By.TAG_NAME, "h3").text
        if "File Uploaded!" in success_message:
            print("Verified File upload test passed!")
        else:
            print("Not Verified File upload test failed")
            
    except Exception as e:
        print(f"Error: {e}")
    finally:
        # Cleanup
        if os.path.exists("test_file.txt"):
            os.remove("test_file.txt")
        time.sleep(2)
        driver.quit()

if __name__ == "__main__":
    test_file_upload()
