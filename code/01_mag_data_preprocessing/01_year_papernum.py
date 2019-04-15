"""
This script calculates the number of papers in each year
by calling calHistogram method of MAKES and saves the result.
"""

import sys
sys.path.append('..')
from utils.microsoft_academic_makes import calcHistogram
from utils.pkl_io import *
from utils.excel_io import *
from utils.directories import *

year_papernum = {}
year_papernum_data = []
start_year = 1800
end_year = 2018

print()

for year in range(end_year, start_year-1, -1):
    papernum = calcHistogram(field_of_study.replace('_', ' '), year)
    if papernum == 0:
        continue
    year_papernum[year] = papernum
    year_papernum_data.append([year, papernum])
    print(year, papernum)

save_pkl_file(directory_dataset_description, 'year_papernum', year_papernum)
save_xlsx_file_single_sheet(directory_dataset_description, 'year_papernum', year_papernum_data)
