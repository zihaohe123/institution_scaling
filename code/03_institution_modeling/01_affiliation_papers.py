"""
This script records the affiliation and its published papers
"""

import sys
sys.path.append('..')
from utils.pkl_io import save_pkl_file, open_pkl_file
from utils.entity_io import open_paper
from utils.directories import *
import time

if __name__ == '__main__':
    paperIds = open_pkl_file(directory_dataset_description, 'paperIds')
    affId_paperIds = {}
    num = 0
    for paperId in paperIds:
        paper = open_paper(paperId)
        num += 1
        if num % 1000 == 0:
            print(num, '/', len(paperIds), ',', time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
        for author in paper.authors:
            affId = author.affId
            if affId not in affId_paperIds:
                affId_paperIds[affId] = []
            affId_paperIds[affId].append(paperId)

    save_pkl_file(directory_dataset_description, 'affId_paperIds', affId_paperIds)
    save_pkl_file(directory_dataset_description, 'affIds', list(affId_paperIds.keys()))
