import sys
sys.path.append('..')
from utils.entity_io import open_affiliation, open_pkl_file
from utils.directories import *
import pandas as pd
import numpy as np


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
        years.sort(reverse=True)
        for year in years:
            size = affiliation.year_size[year]
            internal_collab = affiliation.year_internal_collab[year]
            external_collab = affiliation.year_external_indiv_collab[year]
            production = affiliation.year_production[year]
            productivity = affiliation.year_productivity[year]
            avg_impact = affiliation.year_avg_impact[year] if year in affiliation.year_avg_impact else 0
            avg_impact_oneauthor = affiliation.year_avg_impact_oneauthor[year] if year in affiliation.year_avg_impact_oneauthor else 0
            avg_impact_twoauthor = affiliation.year_avg_impact_twoauthor[year] if year in affiliation.year_avg_impact_twoauthor else 0
            avg_impact_three2sixauthor = affiliation.year_avg_impact_three2sixauthor[year] if year in affiliation.year_avg_impact_three2sixauthor else 0
            avg_teamsize = affiliation.year_avg_teamsize[year]
            avg_internal_teamsize = affiliation.year_avg_internal_teamsize[year]
            cumul_size = affiliation.year_cumul_size[year]
            cumul_internal_collab = affiliation.year_cumul_internal_collab[year]
            cumul_external_indiv_collab = affiliation.year_cumul_external_indiv_collab[year]
            cumul_production = affiliation.year_cumul_production[year]
            cumul_productivity = affiliation.year_cumul_productivity[year]
            data.append([year, size, internal_collab, external_collab, production, productivity,
                         avg_impact, avg_impact_oneauthor, avg_impact_twoauthor, avg_impact_three2sixauthor,
                         avg_teamsize, avg_internal_teamsize,
                         cumul_size, cumul_internal_collab, cumul_external_indiv_collab,
                         cumul_production, cumul_productivity])
        df = pd.DataFrame(data, columns=['year', 'size', '#internal_collab', '#external_collab', 'production', 'productivity',
                                         'avg_impact', 'avg_impact_oneauthor', 'avg_impact_twoauthor', 'avg_impact_three2sixauthor',
                                         'teamsize', 'internal_teamsize',
                                         'cumul_size', '#cumul_internal_collab', '#cumul_external_collab',
                                         'cumul_production', 'cumul_productivity'])
        path = os.path.join(directory_institution_description, '{}.csv'.format(affId))
        df.to_csv(path, index=False)
