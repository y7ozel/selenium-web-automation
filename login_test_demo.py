# login_test_demo.py
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time

def test_login():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    wait = WebDriverWait(driver, 10)
    
    try:
        print("Starting login automation test...")
        
        # Open demo login page
        driver.get("https://the-internet.herokuapp.com/login")
        
        # Enter credentials
        username_field = wait.until(EC.presence_of_element_located((By.ID, "username")))
        username_field.send_keys("tomsmith")
        
        password_field = driver.find_element(By.ID, "password")
        password_field.send_keys("SuperSecretPassword!")
        
        # Click login button
        login_button = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
        login_button.click()
        
        # Verify login success
        success_message = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".flash.success")))
        
        if "You logged into a secure area!" in success_message.text:
            print("Verified Login test PASSED!")
        else:
            print("Not Verified Login test FAILED!")
            
    except Exception as e:
        print(f"Not Verified Test failed with error: {e}")
    finally:
        time.sleep(2)
        driver.quit()

if __name__ == "__main__":
    test_login()
