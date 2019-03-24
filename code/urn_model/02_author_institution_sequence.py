"""
This script creates (author, institution) sequence and each (author, institution) can appear only once.
"""
import sys
sys.path.append('..')
from utils.directories import *
from utils.pkl_io import open_pkl_file, save_pkl_file
import time

if __name__ == '__main__':
    authorId_sequence = open_pkl_file(directory_urn_model, 'ordered_authorId_sequence')
    affId_sequence = open_pkl_file(directory_urn_model, 'ordered_affId_sequence')
    authorId_affId_sequence = []  # (authorId, affId)

    num = 0
    for i in range(len(authorId_sequence)):
        num += 1
        if num % 1000 == 0:
            print(num, time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
        authorId = authorId_sequence[i][0]
        affId = affId_sequence[i][0]
        if (authorId, affId) not in authorId_affId_sequence:
            authorId_affId_sequence.append((authorId, affId))

    save_pkl_file(directory_urn_model, 'authorId_affId_sequence', authorId_affId_sequence)
