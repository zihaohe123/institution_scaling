import sys
sys.path.append('..')
from utils.institution_scaling import *

if __name__ == "__main__":
    # average impact one-author vs. average internal collaborations
    cross_and_within_institution_scaling('avg_internal_collab', 'avg_impact_oneauthor',
                                         directory_scaling_with_collaborations,
                                         '01_avg_impact_oneauthor-avg_internal_collab')

    # average impact two-author vs. average internal collaborations
    cross_and_within_institution_scaling('avg_internal_collab', 'avg_impact_twoauthor',
                                         directory_scaling_with_collaborations,
                                         '02_avg_impact_twoauthor-avg_internal_collab')

    # average impact three2six-author vs. average internal collaborations
    cross_and_within_institution_scaling('avg_internal_collab', 'avg_impact_three2sixauthor',
                                         directory_scaling_with_collaborations,
                                         '03_avg_impact_three2sixauthor-avg_internal_collab')

    # average impact one-atuhor vs. average external individual collaborations
    cross_and_within_institution_scaling('avg_external_indiv_collab', 'avg_impact_oneauthor',
                                         directory_scaling_with_collaborations,
                                         '04_avg_impact_oneauthor-avg_external_indiv_collab')

    # average impact two-author vs. average external individual collaborations
    cross_and_within_institution_scaling('avg_external_indiv_collab', 'avg_impact_twoauthor',
                                         directory_scaling_with_collaborations,
                                         '05_avg_impact_twoauthor-avg_external_indiv_collab')

    # average impact three-author vs. average external individual collaborations
    cross_and_within_institution_scaling('avg_external_indiv_collab', 'avg_impact_three2sixauthor',
                                         directory_scaling_with_collaborations,
                                         '06_avg_impact_threeauthor-avg_external_indiv_collab')
