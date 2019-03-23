import sys
sys.path.append('..')
from utils.directories import *
from utils.pkl_io import open_pkl_file, save_pkl_file
from urn_model.shuffle import *

if __name__ == '__main__':
    # affId_sequence = open_pkl_file(directory_urn_model, 'affId_sequence')
    # shuffled_affId_sequence = randomize_globally(affId_sequence)
    # original_mean_entropy = record_mean_entropy(affId_sequence)
    # shuffled_mean_entropy = record_mean_entropy(shuffled_affId_sequence)
    # print(original_mean_entropy['entropy_k'], original_mean_entropy['bins'])
    sequence = [1,2,3,4,5,6,7,8]
    record_mean_entropy(sequence)
