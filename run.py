import os
from os import remove
import pandas as pd


dirname = os.path.dirname(__file__)
input_csv = os.path.join(dirname, 'companion.csv')
output_csv = os.path.join(dirname, 'companion_edited.csv')

def remove_quotes(input_csv, output_csv):
    '''
    Description: This script removes the quotes from csv files to allow for easier proessing.
    Input: input_file or any csv file with quotes in the rows.
           outout_file or the csv file where the editad data is transfred to
    Returns:
        - A csv file with the same data as the input file but without quotes
    '''
    df = pd.read_csv(input_csv)
    df = df.applymap(lambda x: x.replace("'", '')) 
    

    df.to_csv(output_csv)
    # pd.close_csv()
    return output_csv

def main():
    remove_quotes(input_csv, output_csv)

if __name__ == "__main__":
    main()
