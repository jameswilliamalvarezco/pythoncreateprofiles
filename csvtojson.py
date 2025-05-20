import pandas as pd

def convert_csv_to_json():
    df = pd.read_csv('profiles1.csv')
    df.to_json('data.json', orient='records', indent=2, force_ascii=False)

if __name__ == '__main__':
    convert_csv_to_json()
