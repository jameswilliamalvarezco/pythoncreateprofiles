import pandas as pd

def convert_csv_to_json(csv_file_path, json_file_path):
    df = pd.read_csv(csv_file_path)
    df.to_json(json_file_path, orient='records', indent=2, force_ascii=False)

if __name__ == '__main__':
    convert_csv_to_json('profiles1.csv', 'data.json')
