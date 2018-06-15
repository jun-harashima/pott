import os
import yaml
from pott.paper import Paper


class Yaml:

    DOT_DIR = os.environ['HOME'] + '/.pott'
    YAML_FILE = os.environ['HOME'] + '/.pott/paper.yaml'

    def __init__(self):
        if not os.path.isdir(self.DOT_DIR):
            os.mkdir(self.DOT_DIR)

        if not os.path.isfile(self.YAML_FILE):
            with open(self.YAML_FILE, 'w') as file:
                yaml.dump({}, file, default_flow_style=False)

    def update(self, paper):
        dict = self._load_in_dictionary_form()
        with open(self.YAML_FILE, 'w') as file:
            dict[paper.id] = {
                'url': paper.url,
                'title': paper.title,
                'authors': paper.authors,
                'year': paper.year,
            }
            yaml.dump(dict, file, default_flow_style=False)

    def load(self):
        paper_by_id = {}
        for key, value in self._load_in_dictionary_form().items():
            paper_by_id[key] = Paper(value['url'], value['title'],
                                     value['authors'], value['year'])
        return paper_by_id

    def _load_in_dictionary_form(self):
        with open(self.YAML_FILE, 'r') as file:
            return yaml.load(file)

    def have(self, paper):
        return paper.id in self.load()
