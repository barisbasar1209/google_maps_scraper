import csv
import gather_data 
import driver_setup
import maps_setup
import write_data
import visualize
# from time import time

def main():
    city = "München"
    file = open("station_lists/munich_underground.csv", "r")
    stations = list(csv.reader(file))
    file.close
    PATH = '/usr/local/bin/chromedriver'
    driver = driver_setup.driver_setup(PATH)
    wait = 20 
    maps_setup.maps_setup(driver, wait)
    
    data = gather_data.gather_data(stations, city, driver, wait)
    write_data.write_data(data, city)
    # visualize.visualize_overall_average(data, stations)
    visualize.visualize_specific_station(data, stations, 0)
if __name__ == '__main__':
    main()
