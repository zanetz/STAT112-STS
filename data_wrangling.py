import json
import pandas as pd
import numpy as np

import gzip
import os

def extract_all_contents_of_gz_files_to_common_folder(folder_path, common_folder_path):
    for file_name in os.listdir(folder_path):
        if file_name.endswith('.gz'):
            with gzip.open(os.path.join(folder_path, file_name), 'rb') as gz_file:
                with open(os.path.join(common_folder_path, file_name[:-3]), 'wb') as extracted_file:
                    extracted_file.write(gz_file.read())


def load_json_to_dataframe(file_path):
    with open(file_path) as f:
        data = json.load(f)
    df = pd.DataFrame(data)
    df = pd.concat([df.drop(['event'], axis=1), df['event'].apply(pd.Series)], axis=1)
    return df

def save_all_in_folder_to_csv(folder_path, csv_path):
    for file_name in os.listdir(folder_path):
        if file_name.endswith('.json'):
            df = load_json_to_dataframe(os.path.join(folder_path, file_name))
            df.to_csv(os.path.join(csv_path, file_name[:-5] + '.csv'), index=False)


def combine_csv_in_folder_to_one_csv(folder_path, csv_path):
    combined_csv = pd.concat([pd.read_csv(os.path.join(folder_path, f)) for f in os.listdir(folder_path)])
    combined_csv.to_csv(os.path.join(csv_path, 'combined_csv.csv'), index=False, encoding='utf-8-sig')


if __name__ == '__main__':

    folder_path = 'Monthly_2020_11/'
    common_folder_path = 'unzipped_files/'

    # extract_all_contents_of_gz_files_to_common_folder(folder_path, common_folder_path)

    csv_path = 'csv_file/'

    # save_all_in_folder_to_csv(common_folder_path, csv_path)

    # combine_csv_in_folder_to_one_csv(csv_path, "combined_csv/")