"""
This script creates authorId sequence and affiliation sequence ordered by date.
"""
import sys
sys.path.append('..')
from utils.directories import *
from utils.pkl_io import open_pkl_file, save_pkl_file
import time

if __name__ == '__main__':
    paperIds = open_pkl_file(directory_dataset_description, 'paperIds')
    authorId_sequence = []  # (authorId, date)
    affId_sequence = []  # (affId, date)

    num = 0
    for filename in os.listdir(directory_mag_data):
        paper_entities = open_pkl_file(directory_mag_data, filename[0:-4])
        for paper_entity in paper_entities:
            num += 1
            if num % 1000 == 0:
                print(num, time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
            paperId = paper_entity['Id']
            if paperId not in paperIds:
                continue
            date = paper_entity['D']
            authors = paper_entity['AA']
            for author in authors:
                authorId = author['AuId']
                affId = author['AfId']
                authorId_sequence.append((authorId, date))
                affId_sequence.append((affId, date))

    authorId_sequence.sort(key=lambda t: t[1])
    affId_sequence.sort(key=lambda t: t[1])

    save_pkl_file(directory_urn_model, 'ordered_authorId_sequence', authorId_sequence)
    save_pkl_file(directory_urn_model, 'ordered_affId_sequence', authorId_sequence)

