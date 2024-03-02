import csv
import os
import json


def create_videos_table(videos_info_path, output_path, verbose=False):
    if not os.path.isfile(videos_info_path):
        print('Error: Invalid videos info file')

    with open(videos_info_path, 'r') as videos_info_file:
        videos_info = json.load(videos_info_file)
        rows = []
        for video in videos_info:
            url = f"https://www.youtube.com/watch?v={video.get('id', '')}"
            snippet = video.get('snippet', {})
            content_details = video.get('contentDetails', {})
            statistics = video.get('statistics', {})
            print()
            row = [
                url,
                snippet.get('channelId', ''),
                snippet.get('channelTitle', ''),
                snippet.get('title', ''),
                snippet.get('description', ''),
                snippet.get('publishedAt', ''),
                snippet.get('defaultAudioLanguage', 'unknown'),
                content_details.get('duration', ''),
                statistics.get('viewCount', ''),
                statistics.get('likeCount', ''),
                statistics.get('commentCount', '')
            ]
            rows.append(row)

    output_file = f'{output_path}/videos_table.csv'
    with open(output_file, 'w', encoding='UTF-8', newline='') as csv_file:
        writer = csv.writer(csv_file)
        header = [
            'URL', 'Channel ID', 'Channel Title', 'Video Title', 'Description', 'Publication Date',
            'Audio Language', 'Duration', 'View Count', 'Like Count', 'Comment Count'
        ]
        writer.writerow(header)
        writer.writerows(rows)

    if verbose:
        print('Videos table created successfully.')
        print()

    return 0
