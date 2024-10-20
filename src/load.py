from sqlalchemy import create_engine
import configparser

config = configparser.ConfigParser()
config.read('config.ini')
def loadData(dataFrame):
    conn = config['database']['connection_string']
    engine = create_engine(conn)
    df1 = dataFrame.to_sql('LoadData',engine,index=False,if_exists='replace')

    if df1 is True:
        print("Data Loaded successfully !!")