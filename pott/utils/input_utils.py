FIRST_PROMPT = 'Input paper IDs, quit or next: '
SECOND_PROMPT = 'Input available paper IDs, quit or next: '

QUIT_INPUTS = ['quit', 'q']
NEXT_INPUTS = ['next', 'n']
SPECIAL_INPUTS = QUIT_INPUTS + NEXT_INPUTS


def get_requested_ids(papers):
    available_ids = _get_available_ids(papers)
    requested_ids, special_input = _get_requested_ids(input(FIRST_PROMPT))
    while not set(requested_ids).issubset(set(available_ids)):
        requested_ids, special_input = _get_requested_ids(input(SECOND_PROMPT))
    return [int(id) for id in requested_ids], special_input


def _get_available_ids(papers):
    return [str(id) for id, paper in enumerate(papers)
            if paper.url is not None and paper.authors != []]


def _get_requested_ids(input):
    if input in SPECIAL_INPUTS:
        return [], input
    else:
        return [id for id in input.split(',')], None
