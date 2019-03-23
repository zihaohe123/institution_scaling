import sys
sys.path.append('..')
from utils.directories import *
from utils.pkl_io import open_pkl_file, save_pkl_file
from utils.excel_io import save_xlsx_file_single_sheet

if __name__ == '__main__':
    authorId_sequence = open_pkl_file(directory_urn_model, 'authorId_sequence')
    affId_sequence = open_pkl_file(directory_urn_model, 'affId_sequence')
    affIds = set()
    authornum_affnum = []
    for i in range(len(authorId_sequence)):
        affIds.add(affId_sequence[i])
        authornum_affnum.append([i, len(affIds)])
    print(len(authornum_affnum))
    save_pkl_file(directory_urn_model, 'authornum_affnum', authornum_affnum)
    # save_xlsx_file_single_sheet(directory_urn_model, 'authornum_affnum', authornum_affnum)
