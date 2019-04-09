import matplotlib.pyplot as plt
import random as rd
from utils.linear_regression import *
# from sklearn.gaussian_process import GaussianProcess
from matplotlib.backends.backend_pdf import PdfPages
import matplotlib
matplotlib.rcParams['pdf.fonttype'] = 42
matplotlib.rcParams['ps.fonttype'] = 42
matplotlib.rcParams['figure.figsize'] = (12, 6) # 设置figure_size尺寸
import os


def data_binning(x, y):
    assert len(x) == len(y)
    x_y = {}
    for i in range(len(x)):
        each_x = x[i]
        each_y = y[i]
        if each_x > 8:
            k = math.floor(math.log(each_x, 2))
            a = pow(2,k)
            b = pow(2,k+1)
            each_x = (a+b)/2
        if each_x not in x_y:
            x_y[each_x] = []
        x_y[each_x].append(each_y)
    x_ymean_error = []
    for each_x in x_y:
        _y = np.array(x_y[each_x])
        ymean = _y.mean()
        error = _y.std() / math.sqrt(len(_y))
        x_ymean_error.append([each_x, ymean, error])
    return x_ymean_error


def errorbar_plotting_util(x, y, dy):
    colors = ['b', 'g', 'r', 'c', 'm', 'y']
    ecolor = 'k'
    rd.shuffle(colors)
    color = rd.sample(colors, 1)[0]
    plt.errorbar(x, y, yerr=dy, fmt='x', ecolor=ecolor, color=color, elinewidth=1, capsize=3)

def errorbar_plotting(x, y):
    data = data_binning(x, y)
    _x = [each[0] for each in data]
    _y = [each[1] for each in data]
    dy = [each[2] for each in data]
    errorbar_plotting_util(_x, _y, dy)


def linear_regression_plot(x, y, filepath, filename):
    data = []
    for i in range(len(x)):
        each_x = x[i]
        each_y = y[i]
        data.append([each_x, each_y])
    slope, intercept, R2, p_value, std_err = linear_regression(data)
    if np.isnan(slope):
        raise ValueError("Invalid Data")
    a = math.pow(10, intercept)
    b = slope

    min_x, max_x = min(x), max(x)
    x_pred = np.linspace(min_x, max_x, 1000)
    y_pred = [a*math.pow(each_x_pred, b) for each_x_pred in x_pred]

    # # Compute the Gaussian process fit
    # gp = GaussianProcess(corr='cubic', theta0=1e-2, thetaL=1e-4, thetaU=1E-1,
    #                      random_start=100)
    # gp.fit(x[:, np.newaxis], y)
    # xfit = np.linspace(0, 10, 1000)
    # yfit, MSE = gp.predict(xfit[:, np.newaxis], eval_MSE=True)
    # dyfit = 2 * np.sqrt(MSE)  # 2*sigma ~ 95% confidence region



    colors = ['b', 'g', 'r', 'c', 'm', 'y']
    while 1:
        rd.shuffle(colors)
        color1 = rd.sample(colors, 1)[0]
        color2 = rd.sample(colors, 1)[0]
        if color1 == 'b':
            continue
        if color1 == 'r':
            continue
        if color1 != color2:
            break
    plt.scatter(x, y, s=15, c='black', alpha=0.4)
    plt.plot(x_pred, y_pred, linewidth=3, c='red')
    plt.xscale('log')
    plt.yscale('log')

    # Visualize the result
    # plt.plot(xfit, yfit, '-', color='gray')

    # plt.fill_between(xfit, yfit - dyfit, yfit + dyfit,
    #                  color='gray', alpha=0.2)

    y_axis = min(y)
    x_axis = min(x)
    plt.text(x_axis, y_axis, r'$\beta='+str(np.round(slope, 3))
             + '\pm' + str(np.round(std_err, 3)) + '$\n'
             + r'$R^2=' + str(np.round(R2, 3))
             # + r'\ P-Value=' + str(np.round(p_value, 3))
             + '$',
             fontsize=14)

    pdf = PdfPages(os.path.join(filepath, filename+'.pdf'))
    pdf.savefig(bbox_inches='tight')
    pdf.close()


def get_column(matrix, col):
    return [each[col] for each in matrix]
