from matplotlib import pyplot as plt

def visualize_overall_average(data: dict, stations: list) -> None: 
    avg = lambda s, l : s/l 
    left = [int(x) for x in range(1, len(stations)+1)] 
    height = [] 
    tick_label = [str(station) for station in stations]
    for station in data: 
        crrlst = data[station]
        a = avg(sum(crrlst), len(crrlst))
        height.append(a)
    
    plt.bar(left, height, tick_label = tick_label, width = 0.8, color = ['blue', 'black'])
    plt.xlabel('Stations')
    plt.ylabel('AVG-Duration')
    plt.title('AVG Station to Station Travel Durations U-Bahn Munich')
    plt.show()

def visualize_specific_station(data: dict, stations: list, start: int) -> None: 
    left = [int(x) for x in range(1, len(stations))]
    height = []
    name_start = stations[start][0]
    del stations[start]
    tick_label = [station[0] for station in stations]
    crrlst = data[name_start]
    for duration in crrlst: 
        height.append(duration)

    plt.bar(left, height, tick_label = tick_label, width = 0.8, color = ['blue', 'black'])
    plt.xlabel('Destinations')
    plt.ylabel('Total Duration')
    plt.title(f"Total Station-To-Station Travel Time from {name_start}")
    plt.show()

