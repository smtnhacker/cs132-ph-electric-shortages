import pandas as pd
from os import listdir
from os.path import isfile, join

mypath = "raw_scrapes/"
rawfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
files = [f.split('.')[0] for f in rawfiles]

df = pd.DataFrame(columns=['ID', 'Name', 'Type', 'Region', 'Text'])

next_id = 1
for file_name in files:
    name, type, region = file_name.split('_')

    name = name.upper()
    type = type.lower()
    region = region.lower()

    directory = f"raw_scrapes/{file_name}.txt"
    with open(directory, 'r') as file:
        for line in file:
            new_row = pd.Series({"ID": f"{next_id}",
                        "Name": name,
                        "Type": type,
                        "Region": region,
                        "Text": line})
            df = pd.concat([df, new_row.to_frame().T], ignore_index=True)
            next_id += 1

df.to_csv('scrapes.csv', index=False) 
