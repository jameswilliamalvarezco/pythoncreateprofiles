import unittest
import pandas as pd
import json

class TestCSVToJSON(unittest.TestCase):
    def test_csv_columns(self):
        df = pd.read_csv('profiles1.csv')
        self.assertEqual(len(df.columns), 12)
    
    def test_csv_rows(self):
        df = pd.read_csv('profiles1.csv')
        self.assertGreater(len(df), 900)
    
    def test_json_properties(self):
        with open('data.json', encoding='utf-8') as f:
            data = json.load(f)
            sample = data[0]
            expected_keys = [
                'first_name', 'last_name', 'email', 'gender', 'city',
                'phone', 'birthdate', 'job_title', 'company', 'country',
                'username', 'password']
            for key in expected_keys:
                self.assertIn(key, sample)

    def test_json_rows(self):
        with open('data.json', encoding='utf-8') as f:
            data = json.load(f)
            self.assertGreater(len(data), 900)

if __name__ == '__main__':
    unittest.main()
