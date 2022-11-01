from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
def maps_setup(driver, wait: int = 10) -> None: 
    try: 
        # chose the route calculator option
        choose_route = WebDriverWait(driver, wait).until(
              EC.element_to_be_clickable((By.XPATH, '//*[@id="hArJGc"]/img'))
          )
        choose_route.click()
        
        # chose public transport
        transport  = WebDriverWait(driver, wait).until(
                EC.element_to_be_clickable((By.XPATH, '//*[@id="omnibox-directions"]/div/div[2]/div/div/div/div[3]/button'))
            )
        transport.click()
        
    except: 
        raise Error("Maps setup did not work out as planned")
        driver.close()
