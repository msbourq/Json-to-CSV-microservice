import json
import pandas as pd
from pathlib import Path
import time


while True:
    path = Path('data.json')
    if path.stat().st_size != 0:
        with open('data.json') as json_file:
            item_data = json.load(json_file)
        data = item_data['search_results']
        final_data = []
        for item in data:
            name = item['name']
            price = item['price']
            website = item['website']
            items = [name, price, website]
            final_data.append(items)
        labels = ['Name', 'Price', 'Website']
        df = pd.DataFrame.from_records(final_data, columns=labels)
        df.to_csv('search_results.csv', index=False)
        df = pd.read_csv('search_results.csv',index_col=0)
        df.to_csv('search_results.csv')
        file = open('data.json', 'w')
    else:
        print('Error')
        time.sleep(5)



