import re
import requests
import youtube_transcript_api
from youtube_transcript_api._errors import TranscriptsDisabled


def get_videos_info(ids: list, key: str) -> list:

    session = requests.Session()

    id_chunks = [ids[i:i + 50] for i in range(0, len(ids), 50)]
    part = 'contentDetails,id,liveStreamingDetails,localizations,player,recordingDetails,snippet,statistics,status,' \
           'topicDetails'
    max_results = 50
    result = []

    for index, id_chunk in enumerate(id_chunks, start=1):
        video_ids = ','.join(id_chunk)
        response = session.get(f'https://www.googleapis.com/youtube/v3/videos?key={key}&part={part}'
                               f'&maxResults={max_results}&id={video_ids}')
        result.append(response.json()['items'])

    return result


def get_video_comments(video_id: str, key: str) \
        -> list:
    response = None

    session = requests.Session()

    part = 'id,replies,snippet'
    max_results = 100
    result = []
    page_token = ''
    result.append({'videoId': video_id, 'items': []})
    while True:

        response = session.get(f'https://www.googleapis.com/youtube/v3/commentThreads?key={key}&part={part}'
                               f'&maxResults={max_results}&videoId={video_id}&page_token={page_token}')
        try:
            response.raise_for_status()
        except requests.exceptions.HTTPError as e:
            return []
        data = response.json()

        for item in data.get('items', []):
            result[0]['items'].append(item)

        if 'nextPageToken' in data:
            page_token = data['nextPageToken']
        else:
            break

    return result


def get_video_transcription(video_id: str) -> list:

    result = []

    try:
        transcript_list = youtube_transcript_api.YouTubeTranscriptApi.list_transcripts(video_id)
        transcript_list = re.findall('- [a-z]\w+-*[A-z]*', str(transcript_list))
        languages = [element.split('- ')[1] for element in transcript_list]

        transcription = ''
        for element in youtube_transcript_api.YouTubeTranscriptApi. \
                get_transcript(video_id, languages=languages):
            transcription += element['text'] + ' '

        result.append({'videoId': video_id, 'transcription': transcription})

    except TranscriptsDisabled:
        pass

    return result
