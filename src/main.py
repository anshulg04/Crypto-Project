from extract import extractData
from transform import transformData
from load import loadData

def main():
    df = extractData()
    transformed_df = transformData(df)
    loadData(transformed_df)

if __name__ == '__main__':
    main()
    