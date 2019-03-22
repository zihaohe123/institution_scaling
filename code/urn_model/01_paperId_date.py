import sys
sys.path.append('..')
from utils.directories import *
from utils.pkl_io import open_pkl_file, save_pkl_file
from utils.entity_io import open_paper

if __name__ == '__main__':
    paperIds = open_pkl_file(directory_dataset_description, 'paperIds')
    paperId_date = []
    length = len(paperIds)

    num = 0
    for paperId in paperIds:
        paper = open_paper(paperId)
        date = paper.date
        paperId_date.append([paperId, date])
        num += 1
        if num % 1000 == 0:
            print(num, length)

    paperId_date.sort(key=lambda x: x[1])
    save_pkl_file(directory_dataset_description, 'paperId_date', paperId_date)
