import os
import json
import logging


LOGGER = logging.getLogger(__name__)
base_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), os.pardir)


with open(os.path.join(base_path, 'resources', 'config.json'), 'r') as f:
    config = json.load(f)


from .DocClassifier import DocClassifier
doc_classifier = DocClassifier(state_path=config['state_path'], labels_path=config['labels_path'])