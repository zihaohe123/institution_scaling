# import sys
# sys.path.append('..')
from utils.linear_regression import linear_regression
from utils.excel_io import save_xlsx_file_multi_sheets
from utils.pkl_io import save_pkl_file, open_pkl_file
from utils.entity_io import open_affiliation
from utils.directories import *
import numpy as np
from utils.plotting import line_plot, curve_plot, histogram_plot


def cross_institution_scaling(property_x, property_y, filepath, filename):
    fig_filepath = os.path.join(directory_figures, '{}_vs_{}'.format(property_y, property_x))
    make_dir(fig_filepath)
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
            year_x_y[year].append([np.asarray(x), np.asarray(y)])

    # do the log-log linear regression for each year
    years = list(year_x_y.keys())

    data0 = year_x_y[years[0]]
    # linear_regression_plot(get_column(data0, 0), get_column(data0, 1), filepath, filename)

    years.sort(reverse=True)
    year_alpha_and_r2 = [['year', 'alpha', 'R2']]
    year_alpha_and_r2_dict = {}
    for year in years:
        print(property_y, property_x, year)
        x_y = year_x_y[year]
        x_y = np.asarray(x_y)
        slope, r2, p_value, intercept, std_err = linear_regression(x_y)
        year_alpha_and_r2.append([year, slope, r2])
        year_alpha_and_r2_dict[year] = [slope, r2]

        # make the plots (linear regression)
        if ('impact' not in property_y and year == 2017) or ('impact' in property_y and year in [2012,2010]):
            if not np.isnan(slope):
                xlabel = property_x
                ylabel = '{} in {}'.format(property_y, year)
                fig_filename = '{}_vs_{}_in_{}_plots_cross'.format(property_y, property_x, year)
                line_plot(x_y[:, 0], x_y[:, 1], slope, intercept, r2, xlabel, ylabel, fig_filepath, fig_filename)


    year_alpha_and_r2 = np.asarray(year_alpha_and_r2[1:])
    curve_filename = '{}_vs_{}_curve_cross'.format(property_y, property_x)
    curve_plot(year_alpha_and_r2[:, 0], year_alpha_and_r2[:, 1], 'year',
               r'$\alpha$ of {} vs {} (cross)'.format(property_y, property_x), fig_filepath, curve_filename)
    year_alpha_and_r2 = year_alpha_and_r2.tolist()

    # output the results to a xlsx file
    data = [year_alpha_and_r2]
    sheet_names = ['exponent_and_R2_in_each_year']
    for year in years:
        data.append(year_x_y[year])
        sheet_names.append(str(year))


    # save_xlsx_file_multi_sheets(filepath, filename, np.asarray(data).tolist(), sheet_names)
    save_pkl_file(filepath, filename, year_alpha_and_r2_dict)


def within_institution_scaling(property_x, property_y, filepath, filename):
    fig_filepath = os.path.join(directory_figures, '{}_vs_{}'.format(property_y, property_x))
    make_dir(fig_filepath)

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
        x_y = affId_x_y[affId]
        x_y = np.asarray(x_y)
        slope, r2, p_value, intercept, std_err = linear_regression(affId_x_y[affId])
        if np.isnan(slope):
            continue
        valid_affIds.append(affId)
        affiliation = open_affiliation(affId)
        aff_name = affiliation.aff_name
        affId_alpha_and_R2.append([aff_name, slope, r2])
        affId_alpha_and_R2_dict[aff_name] = (slope, r2)

        # make the plots (linear regression)
        if 'Harvard' in open_affiliation(affId).aff_name and not np.isnan(slope):
            xlabel = property_x
            ylabel = '{} in {}'.format(property_y, open_affiliation(affId).aff_name)
            fig_filename = '{}_vs_{}_in_{}_within'.format(property_y, property_x, open_affiliation(affId).aff_name)
            line_plot(x_y[:, 0], x_y[:, 1], slope, intercept, r2, xlabel, ylabel, fig_filepath, fig_filename)

    hist_filename = '{}_vs_{}_hist_within'.format(property_y, property_x)
    affId_alpha_and_R2 = np.asarray(affId_alpha_and_R2[1:])
    # print(affId_alpha_and_R2[:, 1].dtype)
    histogram_plot(np.asarray(affId_alpha_and_R2[:, 1], dtype=np.float_),
                   r'$\alpha$ of {} vs {} (with)'.format(property_y, property_x), fig_filepath, hist_filename)
    affId_alpha_and_R2 = affId_alpha_and_R2.tolist()

    # save the data
    data = [affId_alpha_and_R2]
    sheet_names = ['alpha_and_R2_in_each_institute']
    for affId in valid_affIds:
        data.append(affId_x_y[affId])
        affiliation = open_affiliation(affId)
        aff_name = affiliation.aff_name
        sheet_names.append(aff_name[:min(29, len(aff_name))])

    # save_xlsx_file_multi_sheets(filepath, filename, np.asarray(data).tolist(), sheet_names)
    save_pkl_file(filepath, filename, affId_alpha_and_R2_dict)


def cross_and_within_institution_scaling(property_x, property_y, filepath, filename):
    cross_institution_scaling(property_x, property_y, filepath, filename+'_cross')
    within_institution_scaling(property_x, property_y, filepath, filename+'_within')
