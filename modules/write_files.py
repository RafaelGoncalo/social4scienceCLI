import csv
import json
import os


def write_csv_file(output_path, data):
    with open(output_path, 'w', encoding='UTF-8') as output_file:
        writer = csv.writer(output_file, delimiter=',')
        writer.writerows(data)
    return 0


def write_temp_json_file(output, data):
    with open(output, 'w', encoding='UTF-8') as output_file:
        json.dump(data, output_file, indent=4)
    return 0


def write_json_file(input_path, output_path):
    folder = os.listdir(input_path)

    data = []
    # iterate over the files
    for file in folder:
        # open the file
        with open(f'{input_path}/{file}', 'r', encoding='UTF-8') as input_file:
            # load the data
            file_data = json.load(input_file)
            # append the data to the list
            data.append(file_data)

    # write the json file
    with open(f'{output_path}.json', 'w', encoding='UTF-8') as output_file:
        json.dump(data, output_file, indent=4)
