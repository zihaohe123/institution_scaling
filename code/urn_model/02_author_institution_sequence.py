import sys
sys.path.append('..')
from utils.directories import *
from utils.pkl_io import open_pkl_file, save_pkl_file
from utils.entity_io import open_paper

if __name__ == '__main__':
    paperId_date = open_pkl_file(directory_dataset_description, 'paperId_date')
    authorId_sequence = []
    affId_sequence = []

    for paperId in paperId_date:
        paper = open_paper(paperId)
        for author in paper.authors:
            authorId = author.authorId
            affId = author.affId
            if authorId in authorId_sequence:
                continue
            authorId_sequence.append(authorId)
            affId_sequence.append(affId)

    save_pkl_file(directory_urn_model, 'affId_sequence', authorId_sequence)
    save_pkl_file(directory_urn_model, 'affId_sequence', affId_sequence)
