import sys
sys.path.append('..')
from utils.pkl_io import open_pkl_file, save_pkl_file
from utils.directories import directory_data


year_affIds = open_pkl_file(directory_data, 'year_affIds')
years = list(year_affIds.keys())
years.sort()

year_cul_affIds = {}
year_cul_affIds[years[0]] = year_affIds[years[0]]
for i in range(len(years)-1):
    year_cul_affIds[years[i+1]] = year_cul_affIds[years[i]].union(year_affIds[years[i+1]])

save_pkl_file(directory_data, 'year_cul_affIds', year_cul_affIds)
