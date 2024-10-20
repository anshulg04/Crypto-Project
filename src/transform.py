import pandas as pd
from datetime import datetime


def transformData(data_to_tform):
    df = pd.json_normalize(data_to_tform,'data')
    df.drop(columns={'marketCapUsd','volumeUsd24Hr','vwap24Hr','supply',
                     'maxSupply','explorer'},inplace=True)
    #df['id'] = df['id'].astype(int)
    df['rank'] = df['rank'].astype(int)
    df['priceUsd'] = df['priceUsd'].astype(float)
    df['changePercent24Hr'] = df['changePercent24Hr'].astype(float)
    df['priceUsd'] = df['priceUsd'].round(2)
    df['changePercent24Hr'] = df['changePercent24Hr'].round(2)
    df['ModifiedDate'] = datetime.today()
    return df