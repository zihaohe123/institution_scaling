# import sys
# sys.path.append('..')
from utils.linear_regression import linear_regression
from utils.excel_io import save_xlsx_file_multi_sheets
from utils.pkl_io import save_pkl_file, open_pkl_file
from utils.entity_io import open_affiliation
from utils.directories import *
import numpy as np


def cross_institution_scaling(property_x, property_y, filepath, filename):
    affIds = open_pkl_file(directory_dataset_description, 'affIds')
    year_x_y = {}
    for affId in affIds:
        affiliation = open_affiliation(affId)
        X = affiliation.propertyname_property[property_x]
        Y = affiliation.propertyname_property[property_y]

        for year in Y:
            x = X[year]
            if x < 2:
                continue    # eliminate the biased data
            y = Y[year]
            if y == 0:
                continue
            if year not in year_x_y:
                year_x_y[year] = []
            year_x_y[year].append([x, y])

    # do the log-log linear regression for each year
    years = list(year_x_y.keys())
    years.sort(reverse=True)
    year_alpha_and_R2 = [['year', 'alpha', 'R2']]
    year_alpha_and_R2_dict = {}
    for year in years:
        slope, R2, p_value, intercept, std_err = linear_regression(year_x_y[year])
        year_alpha_and_R2.append([year, slope, R2])
        year_alpha_and_R2_dict[year] = [slope, R2]

    # output the results to a xlsx file
    data = [year_alpha_and_R2]
    sheet_names = ['exponent_and_R2_in_each_year']
    for year in years:
        data.append(year_x_y[year])
        sheet_names.append(str(year))

    save_xlsx_file_multi_sheets(filepath, filename, data, sheet_names)
    save_pkl_file(filepath, filename, year_alpha_and_R2_dict)


def within_institution_scaling(property_x, property_y, filepath, filename):

    affIds = open_pkl_file(directory_dataset_description, 'affIds')
    affId_x_y = {}
    affId_affname = []

    for affId in affIds:
        affiliation = open_affiliation(affId)
        sizes = np.array(list(affiliation.year_size.values()))
        if sizes.max() - sizes.min() < 50:
            continue
        X = affiliation.propertyname_property[property_x]
        Y = affiliation.propertyname_property[property_y]

        x_y_year = []
        for year in Y:
            x = X[year]
            if x < 2:
                continue
            y = Y[year]
            if y == 0:
                continue
            x_y_year.append([x, y, year])

        affId_x_y[affId] = x_y_year
        affId_affname.append([affId, affiliation.aff_name])

    affId_affname.sort(key=lambda t: t[1])

    affId_alpha_and_R2 = [['affiliation', 'exponent', 'R2']]
    affId_alpha_and_R2_dict = {}

    # do the log-log linear regression for each institution
    valid_affIds = []
    for affId in affId_x_y:
        slope, R2, p_value, intercept, std_err = linear_regression(affId_x_y[affId])
        if np.isnan(slope):
            continue
        valid_affIds.append(affId)
        affiliation = open_affiliation(affId)
        aff_name = affiliation.aff_name
        affId_alpha_and_R2.append([aff_name, slope, R2])
        affId_alpha_and_R2_dict[aff_name] = (slope, R2)

    # save the data
    data = [affId_alpha_and_R2]
    sheet_names = ['alpha_and_R2_in_each_institute']
    for affId in valid_affIds:
        data.append(affId_x_y[affId])
        affiliation = open_affiliation(affId)
        aff_name = affiliation.aff_name
        sheet_names.append(aff_name[:min(29, len(aff_name))])

    save_xlsx_file_multi_sheets(filepath, filename, data, sheet_names)
    save_pkl_file(filepath, filename, affId_alpha_and_R2_dict)


def cross_and_within_institution_scaling(property_x, property_y, filepath, filename):
    cross_institution_scaling(property_x, property_y, filepath, filename+'_cross')
    within_institution_scaling(property_x, property_y, filepath, filename+'_within')
