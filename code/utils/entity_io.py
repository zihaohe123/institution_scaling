from utils.pkl_io import *
from utils.directories import *


# open a paper entity
def open_paper(paperId):
    paper = open_pkl_file(directory_papers, paperId)
    return paper


# save a paper entity
def save_paper(paperId, paper):
    save_pkl_file(directory_papers, paperId, paper)


# open an affiliation entity
def open_affiliation(affId):
    affiliation = open_pkl_file(directory_institutions, affId)
    return affiliation


# save an affiliation entity
def save_affiliation(affId, affiliation):
    save_pkl_file(directory_institutions, affId, affiliation)
