import sys
sys.path.append('..')
from utils.directories import *
from utils.pkl_io import open_pkl_file, save_pkl_file
from urn_model.shuffle import *

if __name__ == '__main__':
    affId_sequence = open_pkl_file(directory_urn_model, 'affId_sequence')
    shuffled_affId_sequence = randomize_globally(affId_sequence)
    original_mean_entropy = record_mean_entropy(affId_sequence)
    shuffled_mean_entropy = record_mean_entropy(shuffled_affId_sequence)
