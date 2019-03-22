import sys
sys.path.append('..')
from utils.directories import *
from utils.pkl_io import open_pkl_file, save_pkl_file
from utils.excel_io import save_xlsx_file_single_sheet

if __name__ == '__main__':
    authorId_sequence = open_pkl_file(directory_urn_model, 'authorId_sequence')
    affId_sequence = open_pkl_file(directory_urn_model, 'affId_sequence')
    authorIds = set()
    affIds = set()
    authornum_affnum = []
    for i in range(len(authorId_sequence)):
        authorIds.add(authorId_sequence[i])
        affIds.add(affIds[i])
        authornum_affnum.append([len(authorIds), len(affIds)])
    save_pkl_file(directory_urn_model, 'authornum_affnum')
    save_xlsx_file_single_sheet(directory_urn_model, 'authornum_affnum')
