import re


def get_user_input(papers):
    user_input = input('Paper to download [0-9] or all: ')
    while not _is_valid_input(user_input, papers):
        user_input = input('Paper to download [0-9] or all: ')
    return user_input


def _is_valid_input(user_input, papers):
    if user_input == 'all':
        return True
    elif re.match(r'[0-9]', user_input) is None:
        return False
    elif papers[int(user_input)]['url'] is None:
        return False
    elif papers[int(user_input)]['authors'] == []:
        return False
    else:
        return True


def select(self, papers, user_input):
    if user_input == 'all':
        return [paper for paper in papers
                if not paper['url'] is None and not paper['authors'] == []]
    else:
        return [papers[int(user_input)]]
