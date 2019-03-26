import sys
sys.path.append('..')
from utils.entity_io import open_affiliation, open_pkl_file
from utils.directories import *
import pandas as pd


if __name__ == '__main__':
    affIds = open_pkl_file(directory_dataset_description, 'affIds')
    length = len(affIds)
    num = 0
    for affId in affIds:
        num += 1
        print('{}/{}'.format(num, length))
        data = []
        affiliation = open_affiliation(affId)
        years = list(affiliation.year_size.keys())
        years.sort()
        for year in years:
            size = affiliation.year_size[year]
            internal_collab = affiliation.year_internal_collab[year]
            external_collab = affiliation.year_internal_collab[year]
            cumul_size = affiliation.year_cumul_size[year]
            cumul_internal_collab = affiliation.year_cumul_internal_collab[year]
            cumul_external_indiv_collab = affiliation.year_cumul_external_indiv_collab[year]
            data.append([year, size, internal_collab, external_collab, cumul_size, cumul_internal_collab, cumul_external_indiv_collab])
        df = pd.DataFrame(data, columns={'year', 'size', '#internal_collab', '#external_collab',
                                         'cumul_size', '#cumul_internal_collab', '#cumul_external_collab'})
        path = os.path.join(directory_collab_of_institutions, '{}.csv'.format(affId))
        df.to_csv(path, index=False)
