import pandas as pd
import requests
import json
import csv
import urllib.parse

def getApiSteam (repeat, num_per_page, url = "https://store.steampowered.com/appreviews/1245620?json=1&language=english", cursor = None, data = []):
    if repeat == 0:
        return data
    else:
        repeat-=1
        if cursor == None:
            response = requests.get(f'{url}&num_per_page={num_per_page}')
            print(response.status_code)
            
            temp=json.loads(response.text)
            data.append(temp["reviews"])
            return getApiSteam(repeat, num_per_page, cursor = urllib.parse.quote(temp["cursor"]), data=data)
        else:
            response = requests.get(f'{url}&cursor={cursor}&num_per_page={num_per_page}')
            print(response.status_code)
            
            temp=json.loads(response.text)
            data.append(temp["reviews"])
            return getApiSteam(repeat, num_per_page, cursor = urllib.parse.quote(temp["cursor"]), data=data)
            
def main():
    # response = requests.get(f'https://store.steampowered.com/appreviews/1245620?json=1&language=english&num_per_page=1')
    # data = json.loads(response.text)
    # print(data)  
    data = getApiSteam(1, 5)  # When values are high it returns cut out value
    data = data[0]

    values = []
    headers = []
    for i in data:
        headers.append(i['recommendationid'])
        values.append(i['review'])


    df = pd.DataFrame(values)
    print(df)
    
main()