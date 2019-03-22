import sys
sys.path.append('..')
from utils.directories import *
from utils.pkl_io import open_pkl_file, save_pkl_file
from utils.entity_io import open_paper

authorIds = set()
paperId_date = open_pkl_file(directory_dataset_description, 'paperId_date')

for paperId in paperId_date:
    paper = open_paper(paperId)
    for author in paper.authors:
        authorId = author.authorId
        affId = author.affId
        if authorId in authorIds:
            continue


