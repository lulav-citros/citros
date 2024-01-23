import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

from citros import CitrosDB, CitrosData, CitrosDataArray
from decouple import config
'''
tests for error_analysis module

just type:

pytest

in terminal in this folder
'''
#connect to a database
table_name = 'test_table'

if config('TEST_ENV', None) == 'github':
    citros = CitrosDB(simulation = 'public',
                      batch = table_name,
                      host=config('POSTGRES_HOST'),
                      user=config('POSTGRES_USER'),
                      password=config('POSTGRES_PASSWORD'),
                      database=config('POSTGRES_DB'),
                      port = config('POSTGRES_PORT'))
else:
    citros = CitrosDB(simulation = 'public',
                        batch = table_name)

citros_D = CitrosData()

x_1 = [5.0, -2.0, -10.0, -2.0, 8.0, -10.0, 0.0, 4.0, -9.0, 5.0, 4.0, np.nan, 8.0, 1.0, -1.0]
x_2 = [0.91, 0.27, 0.27, 0.58, 0.7, 0.21, 0.77, 0.26, 0.74, 0.79, 0.42, 0.03, 0.27, 0.98, 0.71]
x_3 = [-1.4, 1.6, -0.5, 0.9, 9.7, 2.6, -0.8, -6.0, -6.0, 3.3, 4.7, -8.9, 5.9, np.nan, -5.1]
F=pd.DataFrame({'x_1': x_1, 'x_2': x_2, 'x_3': x_3})

X = np.array([[4,17,4],[11,10,12],[6,9,2]])

def test_get_mu():
    mu = citros_D._get_mu(X)
    mu_expected = np.array([7, 12, 6])
    for val in abs(mu -mu_expected):
        assert val < 0.00001, "mu from array is wrong"
    
    mu_2 = citros_D._get_mu(F[['x_1','x_2','x_3']].iloc[9:])
    mu_2_expected = np.array([4.0, 0.5475, 2.2])
    for val in abs(mu_2 -mu_2_expected):
        assert val < 0.00001, "mu from data frame is wrong"

def test_get_covar_matrix():
    sigm = citros_D._get_covar_matrix(X)
    sigm_expected = np.array([[13,-10,17],[-10,19,-5],[17,-5,28]])
    for i in range(3):
        for j in range(3):
            assert abs(sigm[i][j]-sigm_expected[i][j]) < 0.00001, "covariance matrix from array is wrong"

    sigm_2 = citros_D._get_covar_matrix(F[['x_1','x_2','x_3']].iloc[9:])
    sigm_2_expected = np.array([[14.0000, -0.5600, 17.46667],[-0.5600, 0.0594917, -0.7550,],[17.46667,-0.7550,24.81333]])
    for i in range(3):
        for j in range(3):
            assert abs(sigm_2[i][j]-sigm_2_expected[i][j]) < 0.00001, "covariance matrix from data frame is wrong"

def test_get_disp():
    disp = citros_D._get_disp(X)
    disp_expected = [3.60555, 4.358899, 5.291503] 
    for val in abs(disp - disp_expected):
        assert val < 0.00001, "dispersion from array is wrong"

    disp_2 = citros_D._get_disp(F[['x_1','x_2','x_3']].iloc[9:])
    disp_2_expected =[3.741657, 0.243909, 4.981298]
    for val in abs(disp_2 - disp_2_expected):
        assert val < 0.00001, "dispersion from data frame is wrong"

def test_CitrosData():
    #construct CitrosDataSet object with 3 data-columns from 'data.x', parameter from the column 'data.p'
    df = citros.topic('A').data(['data.x', 'data.time', 'data.p'])
    dataset = CitrosData(df, type_name = 'x', data_label=['data.x'], units = 'm', parameter_label='data.p')
    assert len(dataset.data.columns) == 3, 'CitrosData: wrong number of columns'
    assert dataset.units == 'm', 'CitrosData: wrong units'
    assert list(dataset.parameters.keys())[0] == 'data.p', 'CitrosData: wrong parameter_label'
    assert dataset.type == 'x', 'CitrosData: wrong type'

    #construct CitrosDataSet object with 2 data-columns, parameter from the column 'data.p'
    df = citros.topic('A').data(['data.x.x_1','data.x.x_2', 'data.time', 'data.p', 'data.t'])
    dataset = CitrosData(df, type_name = 'x', data_label=['data.x.x_1','data.x.x_2'], units = 'm')
    dataset.set_parameter('p', 5.5)
    dataset.set_parameter('k', 8)
    assert len(dataset.data.columns) == 2, 'CitrosData: wrong number of columns'
    assert dataset.parameters['p'] == 5.5 and dataset.parameters['k'] == 8, 'CitrosData: parameters set wrong'
    
    #construct CitrosDataSet object with 1 data-columns, parameter from 2 columns 'data.p' and 'data.t'
    dataset = CitrosData(df, type_name = 'x', data_label=['data.x.x_1'], units = 'm', parameter_label=['data.p','data.t'])
    assert len(dataset.data.columns) == 1, 'CitrosData: wrong number of columns'
    assert ('data.p' in list(dataset.parameters.keys())) and ('data.t' in list(dataset.parameters.keys())), 'CitrosData: wrong parameter_label'
    
    #test filter on columns with nan and inf == +-10**308 values
    df = citros.topic('A').data(['data.y.y_1', 'data.y.y_2'])
    dataset = CitrosData(df, data_label = ['data.y.y_1','data.y.y_2'], units = 'm')
    assert (((dataset.data['data.y.y_1'].abs()-10**307)>=0) | dataset.data['data.y.y_1'].isna() | 
            ((dataset.data['data.y.y_2'].abs()-10**307)>=0) | dataset.data['data.y.y_2'].isna())\
                .value_counts()[True] == dataset.filter['data.y.y_2'].value_counts()[False], \
                'CitrosData: omit_nan_rows, inf_vals: wrong filter'
    assert (dataset.filter['data.y.y_2'] == dataset.filter['data.y.y_1']).all() == True, \
        'CitrosData: omit_nan_rows, inf_vals: filters are not equal'

    dataset = CitrosData(df, data_label = ['data.y.y_1','data.y.y_2'], units = 'm', inf_vals = None)
    assert (dataset.data['data.y.y_1'].isna() | dataset.data['data.y.y_2'].isna()).\
        value_counts()[True] == dataset.filter['data.y.y_2'].value_counts()[False], \
        'CitrosData: omit_nan_rows: wrong filter'
    assert (dataset.filter['data.y.y_2'] == dataset.filter['data.y.y_1']).all() == True, \
        'CitrosData: omit_nan_rows: filters are not equal'

    dataset = CitrosData(df, data_label = ['data.y.y_1','data.y.y_2'], units = 'm', omit_nan_rows=False)
    assert (((dataset.data['data.y.y_1'].abs()-10**307)>=0) | dataset.data['data.y.y_1'].isna()).\
        value_counts()[True] == dataset.filter['data.y.y_1'].value_counts()[False], \
        'CitrosData: inf_vals: wrong filter for the first column'
    assert (((dataset.data['data.y.y_2'].abs()-10**307)>=0) | dataset.data['data.y.y_2'].isna()).\
        value_counts()[True] == dataset.filter['data.y.y_2'].value_counts()[False], \
        'CitrosData: inf_vals: wrong filter for the second column'

    dataset = CitrosData(df, data_label = ['data.y.y_1','data.y.y_2'], units = 'm', inf_vals=None, omit_nan_rows=False)
    assert (dataset.data['data.y.y_1'].isna()).value_counts()[True] == dataset.filter['data.y.y_1'].value_counts()[False], \
        'CitrosData: no inf_vals, omit_nan_rows=False : wrong filter for the first column'
    assert (dataset.data['data.y.y_2'].isna()).value_counts()[True] == dataset.filter['data.y.y_2'].value_counts()[False], \
        'CitrosData: no inf_vals, omit_nan_rows=False : wrong filter for the second column'

def test_bin_data():
    #test_bin_data
    df = citros.topic('A').rid(start = 0, end = 10).data(['data.x', 'data.time', 'data.p'])
    dataset = CitrosData(df, type_name = 'x', data_label=['data.x'], units = 'm')
    db_bin=dataset.bin_data(n_bins = 5, param_label = 'data.time')

    time_min = min(dataset.addData['data.time'])
    time_max = max(dataset.addData['data.time'])
    time_bin = np.linspace(time_min, time_max, 6)
    time_bin_centers_answ = [(time_bin[i-1]+time_bin[i])/2 for i in range(1,len(time_bin))]

    time_bin_centers = list(set(db_bin.addData['data.time']))
    time_bin_centers.sort()

    assert len(time_bin_centers)==len(time_bin_centers_answ), 'wrong bin centers length'
    assert all([abs(t-answ)<0.01 for t, answ in zip(time_bin_centers, time_bin_centers_answ)]), 'wrong bin centers'

    flag_bin1 = (dataset.addData['data.time'] >= time_bin[0]) & (dataset.addData['data.time'] <= time_bin[1])
    assert len(dataset.addData[flag_bin1]) == 10, 'number of counts in the first bin is wrong'

    assert abs(db_bin.data.loc[0].loc[1].subtract(dataset.data[flag_bin1 & (dataset.addData['sid']==1)].mean()).sum()) < 0.001, 'data values in the first bin, sid = 1 is wrong'
    assert abs(db_bin.data.loc[0].loc[2].subtract(dataset.data[flag_bin1 & (dataset.addData['sid']==2)].mean()).sum()) < 0.001, 'data values in the first bin, sid = 2 is wrong'
    assert abs(db_bin.data.loc[0].loc[3].subtract(dataset.data[flag_bin1 & (dataset.addData['sid']==3)].mean()).sum()) < 0.001, 'data values in the first bin, sid = 3 is wrong'

    flag_bin2 = (dataset.addData['data.time'] > time_bin[1]) & (dataset.addData['data.time'] <= time_bin[2])
    assert len(dataset.addData[flag_bin2]) == 11, 'number of counts in the second bin is wrong'
    assert abs(db_bin.data.loc[1].loc[1].subtract(dataset.data[flag_bin2 & (dataset.addData['sid']==1)].mean()).sum()) < 0.001, 'data values in the second bin, sid = 1 is wrong'
    assert abs(db_bin.data.loc[1].loc[2].subtract(dataset.data[flag_bin2 & (dataset.addData['sid']==2)].mean()).sum()) < 0.001, 'data values in the second bin, sid = 2 is wrong'
    assert abs(db_bin.data.loc[1].loc[3].subtract(dataset.data[flag_bin2 & (dataset.addData['sid']==3)].mean()).sum()) < 0.001, 'data values in the second bin, sid = 3 is wrong'

    flag_bin3 = (dataset.addData['data.time'] > time_bin[2]) & (dataset.addData['data.time'] <= time_bin[3])
    assert len(dataset.addData[flag_bin3]) == 7, 'number of counts in the third bin is wrong'
    assert abs(db_bin.data.loc[2].loc[1].subtract(dataset.data[flag_bin3 & (dataset.addData['sid']==1)].mean()).sum()) < 0.001, 'data values in the third bin, sid = 1 is wrong'
    assert abs(db_bin.data.loc[2].loc[2].subtract(dataset.data[flag_bin3 & (dataset.addData['sid']==2)].mean()).sum()) < 0.001, 'data values in the third bin, sid = 2 is wrong'
    assert abs(db_bin.data.loc[2].loc[3].subtract(dataset.data[flag_bin3 & (dataset.addData['sid']==3)].mean()).sum()) < 0.001, 'data values in the third bin, sid = 3 is wrong'

    flag_bin4 = (dataset.addData['data.time'] > time_bin[3]) & (dataset.addData['data.time'] <= time_bin[4])
    assert len(dataset.addData[flag_bin4]) == 2, 'number of counts in the fourth bin is wrong'
    assert abs(db_bin.data.loc[3].loc[1].subtract(dataset.data[flag_bin4 & (dataset.addData['sid']==1)].mean()).sum()) < 0.001, 'data values in the fourth bin, sid = 1 is wrong'
    assert abs(db_bin.data.loc[3].loc[2].subtract(dataset.data[flag_bin4 & (dataset.addData['sid']==2)].mean()).sum()) < 0.001, 'data values in the fourth bin, sid = 2 is wrong'

    flag_bin5 = (dataset.addData['data.time'] > time_bin[4]) & (dataset.addData['data.time'] <= time_bin[5])
    assert len(dataset.addData[flag_bin5]) == 3, 'number of counts in the fifth bin is wrong'
    assert abs(db_bin.data.loc[4].loc[1].subtract(dataset.data[flag_bin5 & (dataset.addData['sid']==1)].mean()).sum()) < 0.001, 'data values in the fifth bin, sid = 1 is wrong'

def test_bin_data_with_nan_1col():
    #tests bin with nan and inf vals, 1 column
    df = citros.topic('A').data(['data.y.y_1', 'data.y.y_2'])
    dataset = CitrosData(df, data_label = 'data.y.y_1', units = 'm')
    db = dataset.bin_data(n_bins = 1, param_label = 'data.y.y_2', show_fig = True)
    db.data.loc[0]

    flag_y = (((dataset.data['data.y.y_1'].abs()-10**308)<0) & dataset.data['data.y.y_1'].notna())
    flag_x = (((dataset.addData['data.y.y_2'].abs()-10**307)<0) & dataset.addData['data.y.y_2'].notna())
    flag = flag_x & flag_y
    assert (db.data.loc[0] == dataset.data[flag].groupby(dataset.addData[flag.values]['sid']).mean())['data.y.y_1'].all(),\
        'tests bin with nan and inf vals, 1 column: wrong result'
    assert (dataset.addData['data.y.y_2'][flag_x].max() + dataset.addData['data.y.y_2'][flag_x].min())/2 == db.addData['data.y.y_2'].loc[(0,1)], \
        'tests bin with nan and inf vals, 1 column: wrong result for x'

def test_bin_data_with_nan_2col_omit_nan_rows():
    #tests bin with nan and inf vals, omit_nan_rows=True, 2 columns
    df = citros.topic('A').data(['data.y.y_1', 'data.y.y_2', 'data.y.y_3'])
    dataset = CitrosData(df, data_label = ['data.y.y_1', 'data.y.y_3'], units = 'm', omit_nan_rows=True)
    db = dataset.bin_data(n_bins = 1, param_label = 'data.y.y_2', show_fig = False)

    flag_y = (((dataset.data['data.y.y_1'].abs()-10**308)<0) & dataset.data['data.y.y_1'].notna())
    flag_y = flag_y & (((dataset.data['data.y.y_3'].abs()-10**308)<0) & dataset.data['data.y.y_3'].notna())
    flag_x = (((dataset.addData['data.y.y_2'].abs()-10**308)<0) & dataset.addData['data.y.y_2'].notna())
    flag = flag_x & flag_y
    assert (db.data.xs(0, level = db.xid_label) == dataset.data[flag].groupby(dataset.addData[flag.values]['sid']).mean())['data.y.y_1'].all(), \
        'tests bin with nan and inf vals, 2 columns, omit_nan_rows=True: wrong result for the first column'
    assert (db.data.xs(0, level = db.xid_label) == dataset.data[flag].groupby(dataset.addData[flag.values]['sid']).mean())['data.y.y_3'].all(), \
        'tests bin with nan and inf vals, 2 columns, omit_nan_rows=True: wrong result for the second column'
    assert (dataset.addData['data.y.y_2'][flag_x].max() + dataset.addData['data.y.y_2'][flag_x].min())/2 == db.addData['data.y.y_2'].loc[(0,1)], \
        'tests bin with nan and inf vals, 2 columns, omit_nan_rows=True: wrong result for x'

def test_bin_data_with_nan_1co2():
    #tests bin with nan and inf vals, omit_nan_rows=False, 2 columns
    df = citros.topic('A').data(['data.y.y_1', 'data.y.y_2', 'data.y.y_3'])
    dataset = CitrosData(df, data_label = ['data.y.y_1', 'data.y.y_3'], units = 'm', omit_nan_rows=False)
    db = dataset.bin_data(n_bins = 1, param_label = 'data.y.y_2', show_fig = True)

    flag_1y = (((dataset.data['data.y.y_1'].abs()-10**308)<0) & dataset.data['data.y.y_1'].notna())
    flag_3y = (((dataset.data['data.y.y_3'].abs()-10**308)<0) & dataset.data['data.y.y_3'].notna())
    flag_x = (((dataset.addData['data.y.y_2'].abs()-10**308)<0) & dataset.addData['data.y.y_2'].notna())
    flag_1 = flag_x & flag_1y
    flag_3 = flag_x & flag_3y
    assert (db.data['data.y.y_1'].loc[0] == dataset.data['data.y.y_1'][flag_1].groupby(dataset.addData[flag_1.values]['sid']).mean()).all(), \
        'tests bin with nan and inf vals, 2 columns, omit_nan_rows=False: wrong result for the first column'
    assert (db.data['data.y.y_3'].loc[0] == dataset.data['data.y.y_3'][flag_3].groupby(dataset.addData[flag_3.values]['sid']).mean()).all(), \
        'tests bin with nan and inf vals, 2 columns, omit_nan_rows=False: wrong result for the second column'
    assert (dataset.addData['data.y.y_2'][flag_x].max() + dataset.addData['data.y.y_2'][flag_x].min())/2 == db.addData['data.y.y_2'].loc[(0,1)], \
        'tests bin with nan and inf vals, 2 columns, omit_nan_rows=False: wrong result for x'

def test_scale_data():
    df = citros.topic('A').rid(start = 0, end = 10).data(['data.x', 'data.time', 'data.p'])
    dataset = CitrosData(df, type_name = 'x', data_label=['data.x'], units = 'm')
    db_sc = dataset.scale_data(n_points = 5, 
                                    param_label = 'data.time', 
                                    show_fig = False)

    time_points_answ = np.linspace(0, 1, 5)
    time_points = list(set(db_sc.addData['data.time']))
    time_points.sort()

    assert len(time_points)==len(time_points_answ), 'wrong number of points'
    assert all([abs(t-answ)<0.01 for t, answ in zip(time_points, time_points_answ)]), 'wrong points centers'

    def check_interpolation_value(n_time_point, n_sid, label):
        flag = dataset.addData['sid']==n_sid
        time_scaled = (dataset.addData['data.time'] -min(dataset.addData[flag]['data.time']))/(max(dataset.addData[flag]['data.time'])-min(dataset.addData[flag]['data.time']))
        index = abs(time_scaled[dataset.addData['sid']==n_sid] - time_points[n_time_point]).idxmin()

        assert abs(dataset.data.loc[index][label] - db_sc.data.loc[n_time_point].loc[n_sid][label])< 0.1*abs(dataset.data.loc[index][label]), \
            'error time_point = '+str(n_time_point)+' ,sid = '+str(n_sid)+', label = '+label

    check_interpolation_value(n_time_point = 1, n_sid = 2, label = 'data.x.x_1')
    check_interpolation_value(n_time_point = 3, n_sid = 3, label = 'data.x.x_1')
    check_interpolation_value(n_time_point = 3, n_sid = 1, label = 'data.x.x_1')
    check_interpolation_value(n_time_point = 1, n_sid = 3, label = 'data.x.x_2')
    check_interpolation_value(n_time_point = 4, n_sid = 2, label = 'data.x.x_2')

# @image_comparison(baseline_images=['scale_data_omit_nan_rows'], remove_text=True,
#                   extensions=['png'], style='mpl20')
# def test_scale_data_omit_nan_rows():
#     # with nan values and inf values = +-1e308
#     plt.close('all')
#     df = citros.topic('A').data(['data.y.y_1', 'data.y.y_2', 'data.y.y_3'])
#     dataset = CitrosData(df, data_label = ['data.y.y_1','data.y.y_3'], units = 'm', omit_nan_rows=True)
#     db = dataset.scale_data(n_points = 5, 
#                             param_label = 'data.y.y_2', 
#                             show_fig = True)
#     plt.close()
#     time_points_answ = np.linspace(0, 1, 5)
#     assert len(db.addData.groupby('data.y.y_2_id').first()['data.y.y_2'])==len(time_points_answ), 'wrong number of points'
#     assert all([abs(t-answ)<0.01 for t, answ in zip(db.addData.groupby('data.y.y_2_id').first()['data.y.y_2'], time_points_answ)]), 'wrong points centers'

# @image_comparison(baseline_images=['scale_data_with_nan_rows'], remove_text=True,
#                   extensions=['png'], style='mpl20')
# def test_scale_data_with_nan_rows():
#     # with nan values and inf values = +-1e308
#     plt.close('all')
#     df = citros.topic('A').data(['data.y.y_1', 'data.y.y_2', 'data.y.y_3'])
#     dataset = CitrosData(df, data_label = ['data.y.y_1','data.y.y_3'], units = 'm', omit_nan_rows=False)
#     db = dataset.scale_data(n_points = 5, 
#                             param_label = 'data.y.y_2', 
#                             show_fig = True)
#     plt.close()
#     time_points_answ = np.linspace(0, 1, 5)
#     assert len(db.addData.groupby('data.y.y_2_id').first()['data.y.y_2'])==len(time_points_answ), \
#         'scale_data_with_nan_rows: wrong number of points'
#     assert all([abs(t-answ)<0.01 for t, answ in zip(db.addData.groupby('data.y.y_2_id').first()['data.y.y_2'], time_points_answ)]), \
#         'scale_data_with_nan_rows: wrong points centers'

def test_get_statistics():
    df = citros.topic('A').rid(start = 0, end = 10).data(['data.x', 'data.time', 'data.p'])
    dataset = CitrosData(df, type_name = 'x', data_label=['data.x'], units = 'm')
    db_sc = dataset.scale_data(n_points = 5, 
                                    param_label = 'data.time', 
                                    show_fig = False)

    def check_statistic_values(time_id):
        assert (db_sc.get_statistics().loc[time_id]['mean']-np.array(db_sc.data.loc[time_id].mean())).sum() < 0.01,\
            'mean value for time_id = '+str(time_id)+' is wrong'
        assert (np.array(db_sc.data.loc[time_id].cov())-db_sc.get_statistics().loc[time_id]['covar_matrix']).sum() < 0.01,\
            'covariant matrix for time_id = '+str(time_id)+' is wrong'
        assert (np.sqrt(np.diag(np.array(db_sc.data.loc[time_id].cov())))-db_sc.get_statistics().loc[time_id]['sigma']).sum() < 0.01,\
            'standard deviation for time_id = '+str(time_id)+' is wrong'
    
    check_statistic_values(0)
    check_statistic_values(1)
    check_statistic_values(2)
    check_statistic_values(3)
    check_statistic_values(4)

    df = citros.topic('A').data(['data.y.y_1', 'data.y.y_2'])
    #get_statistics with nan and inf, 1 col
    #bin
    dataset = CitrosData(df, data_label = 'data.y.y_1', units = 'm')
    db = dataset.bin_data(n_bins = 10, param_label = 'data.y.y_2', show_fig = False)
    stat = db.get_statistics(return_format='citrosStat')
    assert (db.data.groupby(db.xid_label).mean() == stat.mean)['data.y.y_1'].all(), 'get_statistics with nan and inf, bin: mean is wrong'
    assert (stat.covar_matrix.apply(lambda x: x[0][0]).fillna(True) == 
            db.data.groupby(db.xid_label).cov().groupby(level = 0).first()['data.y.y_1'].fillna(True)).all(), \
            'get_statistics with nan and inf, bin: cov is wrong'
    assert (db.data.groupby(db.xid_label).std().fillna(True) == stat.std.fillna(True))['data.y.y_1'].all(), \
            'get_statistics with nan and inf, bin: std is wrong'
    #scale
    db = dataset.scale_data(n_points = 10, param_label = 'data.y.y_2', show_fig = False)
    stat = db.get_statistics(return_format='citrosStat')
    assert (db.data.groupby(db.xid_label).mean() == stat.mean)['data.y.y_1'].all(), 'get_statistics with nan and inf, scale: wrong'
    assert (stat.covar_matrix.apply(lambda x: x[0][0]).fillna(True) == 
            db.data.groupby(db.xid_label).cov().groupby(level = 0).first()['data.y.y_1'].fillna(True)).all(), \
            'get_statistics with nan and inf, scale: cov is wrong'
    assert (db.data.groupby(db.xid_label).std().fillna(True) == stat.std.fillna(True))['data.y.y_1'].all(), \
            'get_statistics with nan and inf, scale: std is wrong'
    
    df = citros.topic('A').data(['data.y.y_1', 'data.y.y_2', 'data.y.y_3'])
    #get_statistics with nan and inf 2 cols, omit_nan_rows = True
    #bin
    dataset = CitrosData(df, data_label = ['data.y.y_1', 'data.y.y_3'], units = 'm')
    db = dataset.bin_data(n_bins = 10, param_label = 'data.y.y_2', show_fig = False)
    stat = db.get_statistics(return_format='citrosStat')
    assert (db.data.groupby(db.xid_label).mean() == stat.mean).all().all(),\
            'get_statistics with nan and inf 2cols, bin: mean is wrong'
    
    assert (db.data.groupby(db.xid_label).cov().xs('data.y.y_1', level = 1)['data.y.y_1'] == 
            stat.covar_matrix.apply(lambda x: x[0][0])).all() and \
            (db.data.groupby(db.xid_label).cov().xs('data.y.y_1', level = 1)['data.y.y_3'] == 
            stat.covar_matrix.apply(lambda x: x[0][1])).all() and \
            (db.data.groupby(db.xid_label).cov().xs('data.y.y_3', level = 1)['data.y.y_3'] == 
            stat.covar_matrix.apply(lambda x: x[1][1])).all(), \
            'get_statistics with nan and inf, bin 2cols: cov is wrong'
    
    assert (db.data.groupby(db.xid_label).std() == stat.std).all().all(), \
            'get_statistics with nan and inf, bin 2cols: std is wrong'
    #scale
    db = dataset.scale_data(n_points = 10, param_label = 'data.y.y_2', show_fig = False)
    stat = db.get_statistics(return_format='citrosStat')
    assert (db.data.groupby(db.xid_label).mean().fillna(True) == stat.mean.fillna(True)).all().all(),\
            'get_statistics with nan and inf, scale 2cols: mean is wrong'
    assert (db.data.groupby(db.xid_label).cov().fillna(True).xs('data.y.y_1', level = 1)['data.y.y_1'] == 
            stat.covar_matrix.apply(lambda x: x[0][0]).fillna(True)).all() and \
            (db.data.groupby(db.xid_label).cov().fillna(True).xs('data.y.y_1', level = 1)['data.y.y_3'] == 
            stat.covar_matrix.apply(lambda x: x[0][1]).fillna(True)).all() and \
            (db.data.groupby(db.xid_label).cov().fillna(True).xs('data.y.y_3', level = 1)['data.y.y_3'] == 
            stat.covar_matrix.apply(lambda x: x[1][1]).fillna(True)).all(), \
            'get_statistics with nan and inf, scale 2cols: cov is wrong'
    assert (db.data.groupby(db.xid_label).std().fillna(True) == stat.std.fillna(True)).all().all(), \
            'get_statistics with nan and inf, scale 2cols: std is wrong'
    
    #get_statistics with nan and inf, omit_nan_rows = False
    dataset = CitrosData(df, data_label = ['data.y.y_1', 'data.y.y_3'], units = 'm', omit_nan_rows = False)
    db = dataset.bin_data(n_bins = 10, param_label = 'data.y.y_2', show_fig = False)
    stat = db.get_statistics(return_format='citrosStat')
    assert (db.data.groupby(db.xid_label).mean() == stat.mean).all().all(),\
            'get_statistics with nan and inf 2cols, bin, omit_nan_rows = False: mean is wrong'
    assert (db.data.groupby(db.xid_label).cov().xs('data.y.y_1', level = 1)['data.y.y_1'] == 
            stat.covar_matrix.apply(lambda x: x[0][0])).all() and\
            ((db.data.groupby(db.xid_label).cov().xs('data.y.y_1', level = 1)['data.y.y_3'] == 
            stat.covar_matrix.apply(lambda x: x[0][1])).all()) and \
            ((db.data.groupby(db.xid_label).cov().xs('data.y.y_3', level = 1)['data.y.y_3'] == 
            stat.covar_matrix.apply(lambda x: x[1][1])).all()), \
            'get_statistics with nan and inf 2cols, bin 2cols, omit_nan_rows = False: cov is wrong'
    assert (db.data.groupby(db.xid_label).std() == stat.std).all().all(), \
            'get_statistics with nan and inf, bin 2cols, omit_nan_rows = False: std is wrong'

    db = dataset.scale_data(n_points = 10, param_label = 'data.y.y_2', show_fig = False)
    stat = db.get_statistics(return_format='citrosStat')
    assert (db.data.groupby(db.xid_label).mean().fillna(True) == stat.mean.fillna(True)).all().all(),\
            'get_statistics with nan and inf, scale 2cols, omit_nan_rows = False: mean is wrong'
    assert (db.data.groupby(db.xid_label).cov().fillna(True).xs('data.y.y_1', level = 1)['data.y.y_1'] == 
            stat.covar_matrix.apply(lambda x: x[0][0]).fillna(True)).all() and \
            (db.data.groupby(db.xid_label).cov().fillna(True).xs('data.y.y_1', level = 1)['data.y.y_3'] == 
            stat.covar_matrix.apply(lambda x: x[0][1]).fillna(True)).all() and \
            (db.data.groupby(db.xid_label).cov().fillna(True).xs('data.y.y_3', level = 1)['data.y.y_3'] == 
            stat.covar_matrix.apply(lambda x: x[1][1]).fillna(True)).all(), \
            'get_statistics with nan and inf, scale 2cols, omit_nan_rows = False: cov is wrong'
    assert (db.data.groupby(db.xid_label).std().fillna(True) == stat.std.fillna(True)).all().all(), \
            'get_statistics with nan and inf, scale 2cols, omit_nan_rows = False: std is wrong'

def test_show_statistics():
    plt.close('all')
    df = citros.topic('C').data(['data.x.x_1','data.x.x_2', 'data.time', 'data.p'])
    dataset = CitrosData(df, type_name = 'x', data_label=['data.x.x_1', 'data.x.x_2'], units = 'm')
    db_sc = dataset.scale_data(n_points = 35, 
                            param_label = 'data.time', 
                            show_fig = False)
    fig, axes = db_sc.show_statistics(return_fig=True)

    for ax in axes:
        n_lines = len(ax.get_lines())
        assert n_lines == 6, 'show_statistics: number of lines is wrong'

def test_show_statistics_1col_nan_rows_false():
    plt.close('all')
    df = citros.topic('A').data(['data.y.y_1', 'data.y.y_2', 'data.time'])
    dataset = CitrosData(df, data_label = 'data.y.y_1', units = 'm', omit_nan_rows = False)
    db = dataset.scale_data(n_points = 10, param_label = 'data.y.y_2', show_fig = False)
    fig, axes = db.show_statistics(std_color = 'b', return_fig = True)
    for ax in axes:
        n_lines = len(ax.get_lines())
        assert n_lines == 6, 'show_statistics_1col_nan_rows_false: number of lines is wrong'

def test_show_statistics_1col_nan_rows_false():
    plt.close('all')
    df = citros.topic('A').data(['data.y.y_1', 'data.y.y_2', 'data.time'])
    dataset = CitrosData(df, data_label = 'data.y.y_1', units = 'm', omit_nan_rows = False)
    db = dataset.scale_data(n_points = 10, param_label = 'data.y.y_2', show_fig = False)
    fig, axes = db.show_statistics(std_color = 'b', return_fig = True, connect_nan_std = False, std_area = True, std_lines = True)

    for ax in axes:
        n_lines = len(ax.get_lines())
        assert n_lines == 6, 'show_statistics_1col_nan_rows_false: number of lines is wrong'

def test_show_statistics_1col_nan_rows_true():
    plt.close('all')
    df = citros.topic('A').data(['data.y.y_1', 'data.y.y_2', 'data.time'])
    dataset = CitrosData(df, data_label = 'data.y.y_1', units = 'm', omit_nan_rows = True)
    db = dataset.bin_data(n_bins = 50, param_label = 'data.y.y_2', show_fig = False)
    fig, axes = db.show_statistics(return_fig = True, connect_nan_std = False, std_area = True, std_lines = False)
    for ax in axes:
        n_lines = len(ax.get_lines())
        assert n_lines == 4, 'show_statistics_1col_nan_rows_true: number of lines is wrong'

def test_show_statistics_2col_nan_rows_true():
    plt.close('all')
    df = citros.topic('A').data(['data.y.y_3', 'data.y.y_1', 'data.y.y_2', 'data.time'])
    dataset = CitrosData(df, data_label = ['data.y.y_1', 'data.y.y_3'], units = 'm', omit_nan_rows = True)
    db = dataset.scale_data(n_points = 10, param_label = 'data.y.y_2', show_fig = False)
    fig, axes = db.show_statistics(return_fig = True, connect_nan_std = True, std_area = True, std_lines = False)
    for ax in axes:
        n_lines = len(ax.get_lines())
        assert n_lines == 4, 'show_statistics_2col_nan_rows_true: number of lines is wrong'

def test_show_statistics_2col_nan_rows_false():
    plt.close('all')
    df = citros.topic('A').data(['data.y.y_3', 'data.y.y_1', 'data.y.y_2', 'data.time'])
    dataset = CitrosData(df, data_label = ['data.y.y_1', 'data.y.y_3'], units = 'm', omit_nan_rows = False)
    db = dataset.bin_data(n_bins = 10, param_label = 'data.y.y_2', show_fig = False)
    fig, axes = db.show_statistics(return_fig = True)
    for ax in axes:
        n_lines = len(ax.get_lines())
        assert n_lines == 6, 'show_statistics_2col_nan_rows_false: number of lines is wrong'

def test_show_statistics_1col():
    plt.close('all')
    fig = plt.figure(figsize = (6,6))
    df = citros.topic('C').data(['data.x.x_1', 'data.time', 'data.p'])
    dataset = CitrosData(df, type_name = 'x', data_label=['data.x.x_1'], units = 'm')
    #dataset.data = dataset.data.add(p)
    db_sc = dataset.scale_data(n_points = 35, 
                            param_label = 'data.time', 
                            show_fig = False)
    fig, axes = db_sc.show_statistics(fig =fig, return_fig=True)
    for ax in axes:
        n_lines = len(ax.get_lines())
        assert n_lines == 6, 'show_statistics_1col: number of lines is wrong'
    
def test_show_correlation_output():
    #when passing figure to plot
    plt.close('all')
    fig = plt.figure(figsize = (6,6))
    df = citros.topic('C').data(['data.x.x_1','data.x.x_2', 'data.time', 'data.p'])
    dataset = CitrosData(df, type_name = 'x', data_label=['data.x.x_1', 'data.x.x_2'], units = 'm')
    #dataset.data = dataset.data.add(p)
    db_sc = dataset.scale_data(n_points = 35, 
                            param_label = 'data.time', 
                            show_fig = False)
    db_sc.show_correlation(x_col = 'data.x.x_1',
                        y_col = 'data.x.x_2',
                        slice_id = 2,
                        n_std = [1,2,3], display_id=False, fig = fig)
    
    for ax in fig.axes:
        n_lines = len(ax.get_lines())
        n_patches = len(ax.patches)
        assert n_lines == 2, 'show_correlation_output: number of lines is wrong'
        assert n_patches == 3, 'show_correlation_output: number of patches is wrong'

def test_show_correlation_output_2():
    #when creating figure to plot and return it
    plt.close('all')
    df = citros.topic('C').data(['data.x.x_1','data.x.x_2', 'data.time', 'data.p'])
    dataset = CitrosData(df, type_name = 'x', data_label=['data.x.x_1', 'data.x.x_2'], units = 'm')
    db_sc = dataset.scale_data(n_points = 35, 
                            param_label = 'data.time', 
                            show_fig = False)
    fig, ax = db_sc.show_correlation(x_col = 'data.x.x_1',
                                       y_col = 'data.x.x_2',
                                       slice_id = 2,
                                       n_std = [1,2,3], display_id=False, return_fig = True)
    
    n_lines = len(ax.get_lines())
    n_patches = len(ax.patches)
    assert n_lines == 2, 'show_correlation_output_2: number of lines is wrong'
    assert n_patches == 3, 'show_correlation_output_2: number of patches is wrong'

def test_show_correlation_nan_inf():
    df = citros.topic('A').data(['data.y.y_1', 'data.y.y_2', 'data.y.y_3', 'data.time'])
    n_lines_answ_sc = [0, 4, 4, 4, 4, 4, 4, 4, 4, 1]
    n_patches_answ_sc = [0, 1, 1, 1, 1, 1, 1, 1, 1, 0]

    n_lines_answ_bin = [4]*10
    n_patches_answ_bin = [1]*10

    dataset = CitrosData(df, data_label = ['data.y.y_2', 'data.y.y_3'], units = 'm', omit_nan_rows = True)
    db = dataset.scale_data(n_points = 10, param_label = 'data.y.y_1', show_fig = False)
    for i in list(set(db.data.index.get_level_values('data.y.y_1_id'))):
        fig, ax = db.show_correlation(x_col = 'data.y.y_2', y_col = 'data.y.y_3', slice_id = i, bounding_error=True, display_id=False, return_fig = True)
        assert len(ax.get_lines()) == n_lines_answ_sc[i], f'show_correlation_nan_inf: the number of lines for slice_id = {i} is incorrect'
        assert len(ax.patches) == n_patches_answ_sc[i], f'show_correlation_nan_inf: the number of patches for slice_id = {i} is incorrect'
    plt.close('all')

    db = dataset.bin_data(n_bins = 10, param_label = 'data.y.y_1', show_fig = False)
    for i in list(set(db.data.index.get_level_values('data.y.y_1_id'))):
        fig, ax = db.show_correlation(x_col = 'data.y.y_2', y_col = 'data.y.y_3', slice_id = i, bounding_error=True, display_id=False, n_std = 1, return_fig =True)
        assert len(ax.get_lines()) == n_lines_answ_bin[i], f'the number of lines for slice_id = {i} is incorrect'
        assert len(ax.patches) == n_patches_answ_bin[i], f'the number of patches for slice_id = {i} is incorrect'
    plt.close('all')

    dataset = CitrosData(df, data_label = ['data.y.y_2', 'data.y.y_3'], units = 'm', omit_nan_rows = False)
    db = dataset.scale_data(n_points = 10, param_label = 'data.y.y_1', show_fig = False)
    for i in list(set(db.data.index.get_level_values('data.y.y_1_id'))):
        fig, ax = db.show_correlation(x_col = 'data.y.y_2', y_col = 'data.y.y_3', slice_id = i, bounding_error=True, display_id=False, return_fig = True)
        assert len(ax.get_lines()) == n_lines_answ_sc[i], f'show_correlation_nan_inf: the number of lines for slice_id = {i} is incorrect'
        assert len(ax.patches) == n_patches_answ_sc[i], f'show_correlation_nan_inf: the number of patches for slice_id = {i} is incorrect'
    plt.close('all')

    db = dataset.bin_data(n_bins = 10, param_label = 'data.y.y_1', show_fig = False)
    for i in list(set(db.data.index.get_level_values('data.y.y_1_id'))):
        fig, ax = db.show_correlation(x_col = 'data.y.y_2', y_col = 'data.y.y_3', slice_id = i, bounding_error=True, display_id=False, n_std = 1, return_fig =True)
        assert len(ax.get_lines()) == n_lines_answ_bin[i], f'the number of lines for slice_id = {i} is incorrect'
        assert len(ax.patches) == n_patches_answ_bin[i], f'the number of patches for slice_id = {i} is incorrect'
    plt.close('all')

def test_show_correlation_output_2db():
    #when two databases
    plt.close('all')
    df = citros.topic('C').data(['data.x.x_1','data.x.x_2', 'data.time', 'data.p'])
    dataset = CitrosData(df, type_name = 'x', data_label=['data.x.x_1', 'data.x.x_2'], units = 'm')
    #dataset.data = dataset.data.add(p)
    db_sc = dataset.scale_data(n_points = 35, 
                            param_label = 'data.time', 
                            show_fig = False)
    db_sc2 = dataset.scale_data(n_points = 60, 
                            param_label = 'data.time', 
                            show_fig = False)
    _, ax = db_sc.show_correlation(db2 = db_sc2,
                           x_col = 'data.x.x_1',
                           y_col = 'data.x.x_2',
                           slice_id = 2,
                           n_std = 1, display_id=False, return_fig=True)

    n_lines = len(ax.get_lines())
    n_patches = len(ax.patches)
    assert n_lines == 2, 'show_correlation_output_2: number of lines is wrong'
    assert n_patches == 1, 'show_correlation_output_2: number of patches is wrong'

def test_show_correlation_output_bound_error():
    plt.close('all')
    fig = plt.figure(figsize = (6,6))
    df = citros.topic('C').data(['data.x.x_1','data.x.x_2', 'data.time', 'data.p'])
    dataset = CitrosData(df, type_name = 'x', data_label=['data.x.x_1', 'data.x.x_2'], units = 'm')
    #dataset.data = dataset.data.add(p)
    db_sc = dataset.scale_data(n_points = 35, 
                            param_label = 'data.time', 
                            show_fig = False)
    db_sc.show_correlation(x_col = 'data.x.x_1',
                        y_col = 'data.x.x_2',
                        slice_id = 2,
                        n_std = [1,2], display_id=False, fig = fig, bounding_error=True)
    for ax in fig.axes:
        n_lines = len(ax.get_lines())
        n_patches = len(ax.patches)
    assert n_lines == 5, 'show_correlation_output_bound_error: number of lines is wrong'
    assert n_patches == 2, 'show_correlation_output_bound_error: number of patches is wrong'

def test_set_parameter():
    #I parameter setting by parameter_label
    df = citros.topic('A').set_filter({'data.t':[10]}).data(['data.x.x_1', 'data.time', 'data.p', 'data.t'])
    dataset = CitrosData(df, type_name = 'x', data_label=['data.x.x_1'], units = 'm', parameter_label='data.t')
    assert abs(dataset.parameters['data.t'] - 10) < 0.001, 'I parameter setting by parameter_label is wrong'

    #II parameter setting by parameter_label
    df = citros.topic('A').set_filter({'data.t':[10]}).data(['data.x.x_1', 'data.time', 'data.p', 'data.t'])
    dataset = CitrosData(df, type_name = 'x', data_label=['data.x.x_1'], units = 'm', parameter_label=['data.t', 'data.p'])
    assert abs(dataset.parameters['data.t'] - 10) < 0.001, 'II parameter setting by parameter_label is wrong'
    assert abs(dataset.parameters['data.p'] - 0.8) < 0.001, 'II parameter setting by parameter_label is wrong'

    #III parameter setting parameters dict
    df = citros.topic('A').set_filter({'data.t':[10]}).data(['data.x.x_1', 'data.time', 'data.p', 'data.t'])
    dataset = CitrosData(df, type_name = 'x', data_label=['data.x.x_1'], units = 'm', parameters = {'m': 55, 'k': 94})
    assert abs(dataset.parameters['m']-55) < 0.001, 'III parameter setting by parameters dict is wrong'
    assert abs(dataset.parameters['k']-94) < 0.001, 'III parameter setting by parameters dict is wrong'

    #IV parameter setting by set_parameter
    dataset.set_parameter(key = 'v', value = 10)
    dataset.set_parameter(item = {'f': 5, 'g': 1.5})
    assert abs(dataset.parameters['v'] - 10) < 0.001, 'IV parameter setting by set_parameter is wrong'
    assert abs(dataset.parameters['f'] - 5) < 0.001, 'IV parameter setting by set_parameter is wrong'
    assert abs(dataset.parameters['g'] - 1.5) < 0.001, 'IV parameter setting by set_parameter is wrong'
    dataset.drop_parameter('v')
    assert 'v' not in dataset.parameters.keys(), 'IV parameter setting, drop_parameter works wrong'

def test_prediction():
    db_array = CitrosDataArray()
    parameters = [-0.2, 0, 0.2, 0.6]
    
    df = citros.topic('C').data(['data.x.x_1', 'data.time', 'data.p'])
    for p in parameters:
        dataset = CitrosData(df, type_name = 'x', data_label=['data.x.x_1'], units = 'm')
        dataset.set_parameter('p', p)
        dataset.data = dataset.data.add(p)
        db_sc = dataset.scale_data(n_points = 35, 
                                param_label = 'data.time', 
                                show_fig = False)
        db_array.add_db(db_sc)
    p_pred = 0.4
    predicted = db_array.get_prediction(parameters = {'p': p_pred}, 
                                        method = ['neural_net', 'poly','gmm'], 
                                        n_poly = 2, 
                                        activation='tanh', solver='lbfgs', hidden_layer_sizes = (30,), random_state = 9)

    dataset = CitrosData(df, type_name = 'x', data_label=['data.x.x_1'], units = 'm')
    dataset.data = dataset.data.add(p_pred)
    db_sc = dataset.scale_data(n_points = 35, 
                            param_label = 'data.time', 
                            show_fig = False)
    stat = db_sc.get_statistics()

    assert all((predicted[0]['data.x.x_1']-stat['mean'].apply(lambda x: x[0]))/predicted[0]['data.x.x_1']<0.1),\
        'get_prediction(): "neural_net", difference more than 10 percents'
    assert all((predicted[1]['data.x.x_1']-stat['mean'].apply(lambda x: x[0]))/predicted[0]['data.x.x_1']<0.1),\
        'get_prediction(): "poly", difference more than 10 percents'
    assert all((predicted[2]['data.x.x_1']-stat['mean'].apply(lambda x: x[0]))/predicted[0]['data.x.x_1']<0.1),\
        'get_prediction(): "gmm", difference more than 10 percents'

def test_show_prediction():
    plt.close('all')
    db_array = CitrosDataArray()
    parameters = [-0.2, 0, 0.2, 0.6]
    
    df = citros.topic('C').data(['data.x.x_1', 'data.time', 'data.p'])
    for p in parameters:
        dataset = CitrosData(df, type_name = 'x', data_label=['data.x.x_1'], units = 'm')
        dataset.set_parameter('p', p)
        dataset.data = dataset.data.add(p)
        db_sc = dataset.scale_data(n_points = 35, 
                                param_label = 'data.time', 
                                show_fig = False)
        db_array.add_db(db_sc)

    p_pred = 0.4
    _, fig, ax = db_array.get_prediction(parameters = {'p': p_pred}, 
                                        method = ['neural_net', 'poly','gmm'], 
                                        n_poly = 2, 
                                        activation='tanh', solver='lbfgs', hidden_layer_sizes = (30,), random_state = 9,  
                                        show_fig = True, return_fig=True)
    n_lines = len(ax.get_lines())
    assert n_lines == 7, 'show_prediction: number of lines is wrong'
    
def test_show_prediction_2par():
    plt.close('all')
    fig = plt.figure(figsize = (6,6))
    db_array = CitrosDataArray()
    parameters = [-0.2, 0, 0.2, 0.6]
    
    df = citros.topic('C').data(['data.x.x_1', 'data.time', 'data.p'])
    for p in parameters:
        dataset = CitrosData(df, type_name = 'x', data_label=['data.x.x_1'], units = 'm')
        dataset.set_parameter('p', p)
        dataset.set_parameter('t', p)
        dataset.data = dataset.data.add(p)
        db_sc = dataset.scale_data(n_points = 35, 
                                param_label = 'data.time', 
                                show_fig = False)
        db_array.add_db(db_sc)
    p_pred = 0.4
    _ = db_array.get_prediction(parameters = {'p': p_pred, 't': p_pred},
                                        method = ['neural_net', 'poly','gmm'], 
                                        n_poly = 2, 
                                        activation='tanh', solver='lbfgs', hidden_layer_sizes = (30,), random_state = 9,  
                                        fig = fig)
    n_lines = len(fig.axes[0].get_lines())
    assert n_lines == 7, 'show_prediction: number of lines is wrong'
    
def test_show_prediction_3col():
    plt.close('all')
    fig = plt.figure(figsize = (6,6))
    db_array = CitrosDataArray()
    parameters = [-0.2, 0, 0.2, 0.6]
    
    df = citros.topic('C').data(['data.x.x_1', 'data.x.x_2', 'data.time', 'data.p'])
    for p in parameters:
        dataset = CitrosData(df, type_name = 'x', data_label=['data.x.x_1', 'data.x.x_2'], units = 'm')
        dataset.set_parameter('p', p)
        dataset.data = dataset.data.add(p)
        db_sc = dataset.scale_data(n_points = 35, 
                                param_label = 'data.time', 
                                show_fig = False)
        db_array.add_db(db_sc)

    p_pred = 0.4
    _ = db_array.get_prediction(parameters = {'p': p_pred}, 
                                        method = ['neural_net', 'poly','gmm'], 
                                        n_poly = 2, 
                                        activation='tanh', solver='lbfgs', hidden_layer_sizes = (30,), random_state = 9,  
                                        fig = fig)
    
    for ax in fig.axes:
        n_lines = len(ax.get_lines())
        assert n_lines == 7, 'show_prediction: number of lines is wrong'


def test_get_prediction_with_nan_inf():
    
    def compare(omit_nan_rows, method):
        list_t = [10,20,40]

        db_array = CitrosDataArray()
        for t in list_t:
            df = citros.topic('A').\
                        data(['data.y.y_1', 'data.y.y_2', 'data.y.y_3']).assign(**{'data.y.y_1': lambda F: F['data.y.y_1']+t,
                                                                    'data.y.y_2': lambda F: F['data.y.y_2']+t})
            dataset = CitrosData(df, data_label=['data.y.y_1', 'data.y.y_2'], units = 'm', omit_nan_rows = omit_nan_rows )
            dataset.set_parameter('t', t)
            if method == 'scale':
                db_sc = dataset.scale_data(n_points = 10, 
                                                param_label = 'data.y.y_3', 
                                                show_fig = False)
            elif method == 'bin': 
                db_sc = dataset.bin_data(n_bins = 10, 
                                                param_label = 'data.y.y_3', 
                                                show_fig = False)
            db_array.add_db(db_sc)

        df = citros.topic('A').\
                    data(['data.y.y_1', 'data.y.y_2', 'data.y.y_3']).assign(**{'data.y.y_1': lambda F: F['data.y.y_1']+30,
                                                                    'data.y.y_2': lambda F: F['data.y.y_2']+30})
        dataset = CitrosData(df, data_label=['data.y.y_1', 'data.y.y_2'], units = 'm', omit_nan_rows = omit_nan_rows )
        dataset.set_parameter('t', t)
        if method == 'scale':
            db_answ = dataset.scale_data(n_points = 10, 
                                            param_label = 'data.y.y_3', 
                                            show_fig = False)
        elif method == 'bin': 
            db_answ = dataset.bin_data(n_bins = 10, 
                                            param_label = 'data.y.y_3', 
                                            show_fig = False)

        fig = plt.figure(figsize = (8,8))
        prediction_method = ['neural_net', 'poly','gmm']
        predicted = db_array.get_prediction(parameters = {'t':30}, 
                                            method = prediction_method, 
                                            n_poly = 2, 
                                            activation='tanh', solver='lbfgs', hidden_layer_sizes = (15,), random_state = 9,  
                                            show_fig = False,
                                            fig = fig)

        limit_list = [0.2, 1e-5, 1e-5]
        for i, limit in enumerate(limit_list):
            print(f'{omit_nan_rows}')
            print(f'{method}')
            print(predicted[i][['data.y.y_1', 'data.y.y_2']])
            print(db_answ.get_statistics(return_format = 'citrosStat').mean)
            print((predicted[i][['data.y.y_1', 'data.y.y_2']] - db_answ.get_statistics(return_format = 'citrosStat').mean).fillna(0).abs() < limit )
            assert ((predicted[i][['data.y.y_1', 'data.y.y_2']] - db_answ.get_statistics(return_format = 'citrosStat').mean).fillna(0).abs() < limit).all().all() == True,\
                f"test_get_prediction_with_nan_inf: omit_nan_rows = {omit_nan_rows}, method = {method}, prediction method = {prediction_method[i]}: result is wrong"

    compare(omit_nan_rows = True, method = 'bin')
    compare(omit_nan_rows = True, method = 'scale')
    compare(omit_nan_rows = False, method = 'bin')
    compare(omit_nan_rows = False, method = 'scale')
