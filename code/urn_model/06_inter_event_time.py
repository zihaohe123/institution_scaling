import sys
sys.path.append('..')
from utils.directories import *
from utils.pkl_io import open_pkl_file, save_pkl_file
from urn_model.model_occurrences_of_hires import *

if __name__ == '__main__':
    affId_sequence = open_pkl_file(directory_urn_model, 'affId_sequence')
    shuffled_affId_sequence = randomize_globally(affId_sequence)
    inter_event_time = inter_event_time_dist(affId_sequence)
    shuffle_inter_event_time = inter_event_time_dist(shuffled_affId_sequence)
