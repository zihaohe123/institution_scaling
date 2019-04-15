import os


def make_dir(path):
    if os.path.exists(path):
        return
    os.mkdir(path)


def prepare_dir(path):
    files = os.listdir(path)
    if not files:
        with open(os.path.join(path, '123.txt'), 'w') as f:
            f.write('')
    if len(files) == 1:
        return
    if len(files) >= 2:
        if '123.txt' in files:
            os.remove(os.path.join(path, '123.txt'))


directory_root = ('/data/libo/hezihao/institutions_scaling/',
                  "C:/Users/hezh/Documents/OneDrive/2018USC-ISI/institution_scaling")[0]

field_of_study = ('physics', 'computer_science', 'mathematics', 'sociology')[1]


directory_data = os.path.join(directory_root, 'data', field_of_study)
directory_papers = os.path.join(directory_data, 'papers')
directory_mag_data = os.path.join(directory_data, 'mag_data')
directory_institutions = os.path.join(directory_data, 'institutions')

directory_results = os.path.join(directory_root, 'results', field_of_study)
directory_dataset_description = os.path.join(directory_results, 'dataset_description')
directory_scaling_with_institution_size = os.path.join(directory_results, 'scaling_with_institution_size')
directory_scaling_with_collaborations = os.path.join(directory_results, 'scaling_with_collaborations')
directory_urn_model = os.path.join(directory_results, 'urn_model')
directory_collab_of_institutions = os.path.join(directory_dataset_description, 'collab_of_institutions')
directory_institution_description = os.path.join(directory_dataset_description, 'institution_description')

directories = [directory_data, directory_papers, directory_mag_data, directory_institutions,
               directory_results, directory_dataset_description,
               directory_scaling_with_institution_size, directory_scaling_with_collaborations,
               directory_urn_model, directory_collab_of_institutions, directory_institution_description]

if __name__ == '__main__':
    for directory in directories:
        make_dir(directory)
        prepare_dir(directory)
