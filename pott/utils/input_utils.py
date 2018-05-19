import re

PROMPT = 'Select ID for papers to download [0-9,]: '


def get_user_input(papers):
    inputted_ids = input(PROMPT)
    while not _is_valid(inputted_ids):
        inputted_ids = input(PROMPT)
    return [int(id) for id in inputted_ids.split(',')]


def _is_valid(inputted_ids):
    if re.match(r'^[0-9,]+$', inputted_ids) is None:
        return False
    else:
        return True


def select(papers, inputted_ids):
    selected_papers = []
    for id in inputted_ids:
        if papers[id].url is not None and papers[id].authors != []:
            selected_papers.append(papers[id])
    return selected_papers
