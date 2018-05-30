FIRST_PROMPT = 'Select paper IDs to download [0-9,]: '
SECOND_PROMPT = 'Select available paper IDs [0-9,]: '


def get_requested_ids(papers):
    available_ids = [str(id) for id, paper in enumerate(papers)
                     if paper.url is not None and paper.authors != []]
    requested_ids = [id for id in input(FIRST_PROMPT).split(',')]
    while not set(requested_ids).issubset(set(available_ids)):
        requested_ids = [id for id in input(SECOND_PROMPT).split(',')]
    return [int(id) for id in requested_ids]
