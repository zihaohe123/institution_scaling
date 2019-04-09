import os

directory_root = '/data/libo/hezihao/institutions_scaling/'


directory_data = os.path.join(directory_root, 'data')
directory_papers = os.path.join(directory_data, 'papers')
directory_mag_data = os.path.join(directory_data, 'mag_data')
directory_institutions = os.path.join(directory_data, 'institutions')

directory_results = os.path.join(directory_root, 'results')
directory_dataset_description = os.path.join(directory_results, 'dataset_description')
directory_scaling_with_institution_size = os.path.join(directory_results, 'scaling_with_institution_size')
directory_scaling_with_collaborations = os.path.join(directory_results, 'scaling_with_collaborations')
directory_urn_model = os.path.join(directory_results, 'urn_model')
directory_collab_of_institutions = os.path.join(directory_dataset_description, 'collab_of_institutions')
directory_institution_description = os.path.join(directory_dataset_description, 'institution_description')
