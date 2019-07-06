import sys
sys.path.append('..')
from utils.institution_scaling import *

if __name__ == '__main__':

    # internal collaborations vs. institution size
    cross_and_within_institution_scaling('size', 'internal_collab', directory_scaling_with_institution_size, '01_internal_collab')

    # external institutional collaborations vs. institution size
    cross_and_within_institution_scaling('size', 'external_inst_collab', directory_scaling_with_institution_size, '02_external_inst_collab')

    # external individual collaborations vs. institution size
    cross_and_within_institution_scaling('size', 'external_indiv_collab', directory_scaling_with_institution_size, '03_external_indiv_collab')

    # individual collaborations vs. institution size
    cross_and_within_institution_scaling('size', 'indiv_collab', directory_scaling_with_institution_size, '04_indiv_collab')

    # average teamsize vs. institution size
    cross_and_within_institution_scaling('size', 'avg_teamsize', directory_scaling_with_institution_size, '05_avg_teamsize')

    # average internal teamsize vs. institution size
    cross_and_within_institution_scaling('size', 'avg_internal_teamsize', directory_scaling_with_institution_size, '06_avg_internal_teamsize')

    # average external teamsize vs. institution size
    cross_and_within_institution_scaling('size', 'avg_external_teamsize', directory_scaling_with_institution_size, '07_avg_external_teamsize')

    # production vs. institution size
    cross_and_within_institution_scaling('size', 'production', directory_scaling_with_institution_size, '08_production')

    # productivity vs. institution size
    cross_and_within_institution_scaling('size', 'productivity', directory_scaling_with_institution_size, '09_productivity')

    # impact vs. institution size
    cross_and_within_institution_scaling('size', 'avg_impact', directory_scaling_with_institution_size, '10_impact')

    # impact one-author vs. institution size
    cross_and_within_institution_scaling('size', 'avg_impact_oneauthor', directory_scaling_with_institution_size, '11_impact_oneauthor')

    # impact two-author vs. institution size
    cross_and_within_institution_scaling('size', 'avg_impact_twoauthor', directory_scaling_with_institution_size, '12_impact_two_author')

    # impact three2six-author vs. institution size
    cross_and_within_institution_scaling('size', 'avg_impact_three2sizeauthor', directory_scaling_with_institution_size, '13_impact_three2size_author')
