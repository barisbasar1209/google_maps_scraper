from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By

def driver_setup(PATH: str) -> webdriver: 

    # setting up the driver
    url = 'https://www.google.com/maps'
    try: 
        driver = webdriver.Chrome(PATH)
    except: 
        raise Exception ("No chromedriver found in this location. Check for the location by using the 'whereis chromedriver' command")

    driver.get(url)
    current_url = driver.current_url

    # if cookie consent page pops up, accept it
    if (url == current_url):
        pass

    elif (url != current_url and "consent" in current_url.lower()):  
        accept = WebDriverWait(driver, 15).until(
                    EC.element_to_be_clickable(
                        (By.XPATH, '//*[@id="yDmH0d"]/c-wiz/div/div/div/div[2]/div[1]/div[3]/div[1]/div[1]/form[2]/div/div/button/span')
                    )
                )
        accept.click()
    
    else:
        raise Exception ('Unexpected redirection occured. The current url is not the provided one, neither a cookies consent page.')
        driver.close()

    driver.maximize_window()
    return driver    

     
