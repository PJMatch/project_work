import pandas as pd

CSV_FILE_NAME = 'non_commitable.csv'

def proces_data():
   df = pd.read_csv(CSV_FILE_NAME, sep=';') 

   time_summary = df.groupby('kto')['czas'].sum().reset_index()
   return time_summary

if __name__ == "__main__":
    try:
        results = proces_data()
        print('Wyniki:')
        print(results)
    except FileNotFoundError:
        print(f'Cannot finde file {CSV_FILE_NAME}')
