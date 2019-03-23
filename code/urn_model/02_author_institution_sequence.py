import sys
sys.path.append('..')
from utils.directories import *
from utils.pkl_io import open_pkl_file, save_pkl_file
from utils.entity_io import open_paper
import time

if __name__ == '__main__':
    paperIds = open_pkl_file(directory_dataset_description, 'paperIds')
    authorId_sequence = []
    affId_sequence = []

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

    new_authorId_sequence = []
    new_affId_sequence = []

    authorIds = set()
    affIds = set()

    for i in range(len(authorId_sequence)):
        authorId = authorId_sequence[i][0]
        if authorId not in authorIds:
            authorIds.add(authorId)
        new_authorId_sequence.append(authorId)
        affId = affId_sequence[i][0]
        new_affId_sequence.append(affId)

    save_pkl_file(directory_urn_model, 'authorId_sequence', new_authorId_sequence)
    save_pkl_file(directory_urn_model, 'affId_sequence', new_affId_sequence)
