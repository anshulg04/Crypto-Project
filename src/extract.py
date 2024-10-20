import configparser
import requests
import pandas as pd

config = configparser.ConfigParser()
config.read('config.ini')

def extractData():
    api_link = config['api']['api_url']
    response = requests.get(api_link)
    response.raise_for_status()
    data = response.json()

    return data