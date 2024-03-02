import csv
import json
import os


def process_altmetric_input(input_path):
    dois, ids = [], []
    with open(input_path, 'r', encoding='UTF-8') as altmetric_output:
        reader = csv.reader(altmetric_output, delimiter=',')
        headers = next(reader)
        for row in reader:
            dois.append(row[headers.index('DOI')])
            ids.append(row[headers.index('Mention URL')].replace('https://www.youtube.com/watch?v=', ''))

    return ids, dois


def process_urls(input_path='', identifier=''):
    ids = []
    if input_path != '':
        # check the file extension
        if input_path.endswith('.csv'):
            with open(input_path, 'r', encoding='UTF-8') as input_file:
                reader = csv.reader(input_file, delimiter=',')
                headers = next(reader)
                for row in reader:
                    ids.append(row[headers.index('URL')].split('v=')[1].split('&')[0])
                return ids
        elif input_path.endswith('.txt'):
            with open(input_path, 'r', encoding='UTF-8') as input_file:
                for line in input_file:
                    ids.append(line.split('v=')[1].split('&')[0].replace('\n', ''))
                return ids
    elif identifier != '':
        ids.append(identifier.split('v=')[1].split('&')[0])
        return ids


def process_dois(input_path='', identifier=''):
    dois = []
    if input_path != '':
        with open(input_path, 'r', encoding='UTF-8') as input_file:
            reader = csv.reader(input_file, delimiter=',')
            headers = next(reader)
            for row in reader:
                dois.append(row[headers.index('DOI')])
            return dois
    elif identifier != '':
        dois.append(identifier)
        return dois


def get_past_output(output_path, mode):
    identifiers = []
    if mode == 'videos_info':
        if os.path.isfile(f'{output_path}/videos_info.json'):
            with open(f'{output_path}/videos_info.json', 'r') as f:
                data = json.load(f)
                identifiers = [video['id'] for video in data]
    elif mode == 'videos_comments':
        if os.path.isfile(f'{output_path}/videos_comments.json'):
            with open(f'{output_path}/videos_comments.json', 'r') as f:
                data = json.load(f)
                identifiers = [video['videoId'] for video in data]
    elif mode == 'videos_transcriptions':
        if os.path.isfile(f'{output_path}/videos_transcriptions.json'):
            with open(f'{output_path}/videos_transcriptions.json', 'r') as f:
                data = json.load(f)
                identifiers = [video['id'] for video in data]
    elif mode == 'articles_info':
        if os.path.isfile(f'{output_path}/articles_info.json'):
            with open(f'{output_path}/articles_info.json', 'r') as f:
                data = json.load(f)
                identifiers = [article['doi'] for article in data]

    return identifiers

def process_comments_file(input_path):
    comments = []
    with open(input_path, 'r', encoding='UTF-8') as input_file:
        json_data = json.load(input_file)
        for video in json_data:
            for item in video['items']:
                comments.append(item)
