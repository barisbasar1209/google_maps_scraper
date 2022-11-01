from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import sqlite3

## in this function the bot actually executes all the searching action and gathers the data

## plan : 
#   1. take as an input the list of stations
#   2. loop through all the stations, searching for the required travelling time from a to b by underground
#   3. if there is no time for the underground provided by gmaps, assume it's 1 Minute
#   4. store the data in a sqlite database
    # 4.1. one table per city 
    # 4.2. db should be able to safe the already known stations of a city 
    # 4.3. man sollte neue stationen einfügen können
    # 4.4. table has one coloumn per station and also one row per station
    # 4.5. rows and columns are only stored by index 

## extras to do : 
#   make the option available to make the bot search for the stations
#   option to set timefrimes 
#   option to set the date or dates

def gather_data(stations: list, city: str, driver, wait: int = 10) -> dict: 
    db = {}

    # unclear how to force python to read in each line as a variable, not as a list
    for startlst in stations:
        start = startlst[0]
        # insert start
        start_inp = WebDriverWait(driver, wait).until(
                    EC.presence_of_element_located((By.XPATH, '//*[@id="sb_ifc51"]/input'))
                ) 
        start_inp.clear()
        start_inp.send_keys(f"Ubahn {start} {city}")
        db[start] = []

        for destlst in stations: 
            # skip if destination is same as start 
            dest = destlst[0] 
            if dest == start: 
                continue

            # insert destination
            dest_inp = driver.find_element(By.XPATH, '//*[@id="sb_ifc52"]/input')
            dest_inp.clear()
            dest_inp.send_keys(f"Ubahn {dest} {city}")
            dest_inp.send_keys(Keys.RETURN)
            
            # get the duration of travel
            try: 
                duration = WebDriverWait(driver, wait).until(
                            EC.presence_of_element_located((By.XPATH, '//*[@id="section-directions-trip-0"]/div[1]/div[2]/div[1]/div'))
                        )
                durstr = duration.text
                durint = [int(x) for x in durstr.split() if x.isdigit()][0]

            # if there was no time for underground connection check whether or not there is one for route by walk 
            except selenium.common.exceptions.TimeoutException: 
                # if true assume that the duration is only 1 minute
                try: 
                    duration = WebDriverWait(driver, wait).until(
                                EC.presence_of_element_located((By.XPATH, '//*[@id="section-directions-trip-0"]/div[1]/div[3]/div[1]/div[1]'))
                            )
                    durint = 1
                # else something else must've gone wrong
                except: 
                    durint = -1  

            ## storing the durations in the database should work best in here 
            # add duration in the dict db 
            db[start].append(durint)
    return db

        
            











