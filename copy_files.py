from filter_md import copy_markdown_files
from filter_data import copy_data_files
import os

# Define collections to process
collections = ['_posts', '_publications', '_courses', '_datasets', '_events', '_software']
files = ['team.csv', 'mentions.yaml']

# Process markdown files in collections
for collection in collections:
    src = os.path.join('temp-remote', collection)
    if os.path.exists(src):
        copy_markdown_files(src, collection)

# Process data files in _data
src_data = os.path.join('temp-remote', '_data')
if os.path.exists(src_data):
    copy_data_files(src_data, '_data', files)
