import requests


def get_articles_info(dois: list) -> list:

    session = requests.Session()
    dois_chunks = [dois[i:i + 10] for i in range(0, len(dois), 10)]

    result = []

    for index, dois_chunk in enumerate(dois_chunks, start=1):
        link = f'https://api.openaire.eu/search/researchProducts?format=json&doi={",".join(dois_chunk)}'
        try:
            response = session.get(link)
            response.raise_for_status()
            result += response.json()['response']['results']['result']

        except requests.exceptions.RequestException:
            pass

    return result


def get_articles_citations(dois: list) -> list:
    session = requests.Session()
    result = []

    for index, doi in enumerate(dois, start=1):
        link = f'https://opencitations.net/index/api/v1/citations/{doi}'
        try:
            response = session.get(link)
            response.raise_for_status()
            result.append({'doi': doi, 'citations': response.json()})
        except requests.exceptions.RequestException:
            pass

    return result
