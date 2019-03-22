"""
This script screens the original paper entities
"""

import sys
sys.path.append('..')
import time
from utils.directories import *
from utils.pkl_io import open_pkl_file, save_pkl_file


def is_valid_paper(paper_entity):
    # the maximum teamsize of each paper is 25
    # each paper should contain the complete information of the authors and their affiliations
    if 'AA' not in paper_entity:
        return False
    authors = paper_entity['AA']
    if len(authors) > 25:
        return False
    for author in authors:
        if 'DAuN' not in author:
            return False
        if 'AuId' not in author:
            return False
        if 'DAfN' not in author:
            return False
        if 'AfId' not in author:
            return False
    return True


if __name__ == '__main__':
    valid_paperIds = set()
    num = 0
    for filename in os.listdir(directory_mag_data):
        paper_entities = open_pkl_file(directory_mag_data, filename[0:-4])
        for paper_entity in paper_entities:
            num += 1
            if num % 1000 == 0:
                print(num, time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
            if not is_valid_paper(paper_entity):
                continue
            valid_paperIds.add(paper_entity['Id'])
    save_pkl_file(directory_dataset_description, 'paperIds', valid_paperIds)
