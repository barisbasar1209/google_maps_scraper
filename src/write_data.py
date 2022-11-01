import json 

def write_data(data: dict, city: str) -> None: 
    with open('data_files/{city}_data.txt', 'w') as f: 
        f.write(json.dumps(data))

