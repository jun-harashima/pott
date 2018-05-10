import os
import yaml


class Yaml:

    YAML_FILE = os.environ['HOME'] + '/.pott/paper.yaml'

    def __init__(self):
        if not os.path.isfile(self.YAML_FILE):
            with open(self.YAML_FILE, 'w') as file:
                yaml.dump({}, file, default_flow_style=False)

    def update(self, paper):
        paper_by_id = self.load()
        with open(self.YAML_FILE, 'w') as file:
            paper_by_id[paper.id] = {
                'url': paper.url,
                'title': paper.title,
                'authors': paper.authors,
                'year': paper.year,
            }
            yaml.dump(paper_by_id, file, default_flow_style=False)

    def load(self):
        with open(self.YAML_FILE, 'r') as file:
            return yaml.load(file)
