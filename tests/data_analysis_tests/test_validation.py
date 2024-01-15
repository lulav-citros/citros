import numpy as np
import matplotlib.pyplot as plt

from citros import CitrosDB, Validation
from decouple import config
'''
tests for error_analysis module

just type:

pytest

in terminal in this folder
'''
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

def test_std_bound_test():
    df = citros.topic('A').set_order({'sid':'asc','rid':'asc'}).data(['data.x', 'data.x.x_1','data.x.x_2','data.x.x_3','data.time'])

    V = Validation(df, data_label = ['data.x.x_1'], param_label = 'data.time', 
                      method = 'bin', num = 50, units = 'm')
    V3 = Validation(df, data_label = ['data.x.x_1', 'data.x.x_2','data.x.x_3'], param_label = 'data.time', 
                        method = 'scale', num = 50, units = 'm')
    log, table, fig = V3.std_bound_test(limits = [0.25, 0.28, [-20, 10]], n_std = 3)
    
    assert (log['test_param']['limits'][0] - 0.25) < 0.001, "std_bound_test: ['test_param']['limits'][0] is wrong"
    assert (log['test_param']['limits'][2][1] - 10) < 0.001, "std_bound_test: ['test_param']['limits'][2][1] is wrong"
    assert log['data.x.x_1']['passed'] == True, "std_bound_test: ['data.x.x_1']['passed'] is wrong"
    assert log['data.x.x_3']['passed'] == False, "std_bound_test: ['data.x.x_3']['passed'] is wrong"
    assert abs(log['data.x.x_1']['pass_rate'] - 1.0) < 0.001, "std_bound_test: ['data.x.x_1']['pass_rate'] is wrong"
    assert abs(log['data.x.x_3']['pass_rate']) < 0.001, "std_bound_test: ['data.x.x_3']['pass_rate'] is wrong"

    assert table['data.x.x_3'].any() == False, "std_bound_test: table['data.x.x_3'] is wrong"
    assert table['data.x.x_1'].all() == True, "std_bound_test: table['data.x.x_1'] is wrong"
    assert len(fig.axes) == 3, "std_bound_test: the number of axes for 3d vector is wrong"

    log, table, fig = V3.std_bound_test(limits = [0.2, 0.2, [-20, 10]], n_std = 3)
    assert len(log['data.x.x_1']['failed']) == 4, "std_bound_test: ['data.x.x_1']['failed'] for n_std = 3 is wrong"

    log, table, fig = V3.std_bound_test(limits = [0.2, 0.2, [-20, 10]], n_std = 1)
    assert len(log['data.x.x_1']['failed']) == 0, "std_bound_test: ['data.x.x_1']['failed'] for n_std = 1 is wrong"

    log, table, fig = V.std_bound_test(limits = 0.2, n_std = 3)
    assert len(log['data.x.x_1']['failed']) == 3, "std_bound_test: ['data.x.x_1']['failed'] for n_std = 3 is wrong"

    log, table, fig = V.std_bound_test(limits = [0.2], n_std = 1)
    assert len(log['data.x.x_1']['failed']) == 0, "std_bound_test: ['data.x.x_1']['failed'] for n_std = 1 is wrong"
    assert len(fig.axes) == 1, "std_bound_test: the number of axes for 1d vector is wrong"
    assert log['data.x.x_1']['passed'] == True, "std_bound_test: ['data.x.x_1']['passed'] is wrong"

    V3_bin = Validation(df, data_label = ['data.x.x_1', 'data.x.x_2','data.x.x_3'], param_label = 'data.time', 
                      method = 'bin', num = 50, units = 'm')
    log, table, fig = V3_bin.std_bound_test(limits = [0.25, 0.28, [-20, 10]], n_std = 1)
    assert log['data.x.x_1']['passed'] == True, "std_bound_test: nan_passed default True: log['data.x.x_1']['passed'] is wrong"
    assert list(log['data.x.x_1']['nan_std'].keys())[0] == 49, "std_bound_test: nan_passed default True: log['data.x.x_1']['nan_std']  is wrong"
    assert len(log['data.x.x_3']['failed']) == 49, "std_bound_test: nan_passed default True: log['data.x.x_3']['failed'] is wrong"

    log, table, fig = V3_bin.std_bound_test(limits = [0.25], n_std = 1, nan_passed = False)
    assert log['data.x.x_1']['passed'] == False, "std_bound_test: nan_passed False: log['data.x.x_1']['passed']  is wrong"
    assert list(log['data.x.x_1']['nan_std'].keys())[0] == 49, "std_bound_test: nan_passed = False: log['data.x.x_1']['nan_std'] is wrong"
    assert len(log['data.x.x_3']['failed']) == 50, "std_bound_test: nan_passed default True: log['data.x.x_3']['failed'] is wrong"

    plt.close('all')

    #nan+inf

    df = citros.topic('A').set_order({'sid':'asc','rid':'asc'}).data(['data.y', 'data.y.y_1','data.y.y_2','data.y.y_3','data.time'])

    V = Validation(df, data_label = ['data.y.y_1'], param_label = 'data.y.y_3', 
                        method = 'bin', num = 50, units = 'm', omit_nan_rows = False)
    V3 = Validation(df, data_label = ['data.y.y_1', 'data.y.y_2'], param_label = 'data.y.y_3', 
                        method = 'scale', num = 50, units = 'm', omit_nan_rows = False)
    log3, table3, fig3 = V3.std_bound_test(limits = [30, [-25, 25]], n_std = 2)
    log, table, fig = V.std_bound_test(limits = 40, n_std = 3, connect_nan_std = True)
    passed = True
    for name in ['data.y.y_1', 'data.y.y_2']:
        passed = passed and log3[name]['passed']
    assert passed, 'std_bound_test, nan+inf 3d: omit_nan_rows False not passed'
    passed = True
    passed = passed and log['data.y.y_1']['passed']
    assert passed, 'std_bound_test, nan+inf 1d: omit_nan_rows False not passed'

    V = Validation(df, data_label = ['data.y.y_1'], param_label = 'data.y.y_3', 
                        method = 'scale', num = 50, units = 'm', omit_nan_rows = True)
    V3 = Validation(df, data_label = ['data.y.y_1', 'data.y.y_2'], param_label = 'data.y.y_3', 
                        method = 'bin', num = 50, units = 'm', omit_nan_rows = True)
    log3, table3, fig3 = V3.std_bound_test(limits = [30], n_std = 2, std_lines = False)
    log, table, fig = V.std_bound_test(limits = 40, n_std = 3, connect_nan_std = True, std_area = False)
    passed = True
    for name in ['data.y.y_1', 'data.y.y_2']:
        passed = passed and log3[name]['passed']
    assert passed, 'std_bound_test, nan+inf: omit_nan_rows True not passed'
    passed = True
    passed = passed and log['data.y.y_1']['passed']
    assert passed, 'std_bound_test, nan+inf: omit_nan_rows True not passed'

    plt.close('all')

def test_std_test():
    df = citros.topic('A').set_order({'sid':'asc','rid':'asc'}).data(['data.x', 'data.x.x_1','data.x.x_2','data.x.x_3','data.time'])

    V = Validation(df, data_label = ['data.x.x_1'], param_label = 'data.time', 
                        method = 'bin', num = 50, units = 'm')
    V3 = Validation(df, data_label = ['data.x.x_1', 'data.x.x_2','data.x.x_3'], param_label = 'data.time', 
                        method = 'scale', num = 50, units = 'm')
    log, table, fig = V3.std_test(limits = [0.1, 0.2, 90], n_std = 1)
    
    assert (log['test_param']['limits'][0] - 0.1) < 0.001, "std_test: ['test_param']['limits'][0] is wrong"
    assert (log['test_param']['limits'][1] - 0.2) < 0.001, "std_test: ['test_param']['limits'][2][1] is wrong"
    assert log['data.x.x_1']['passed'] == True, "std_test: ['data.x.x_1']['passed'] is wrong"
    assert log['data.x.x_3']['passed'] == False, "std_test: ['data.x.x_3']['passed'] is wrong"
    assert abs(log['data.x.x_1']['pass_rate'] - 1.0) < 0.001, "std_test: ['data.x.x_1']['pass_rate'] is wrong"
    assert abs(log['data.x.x_3']['pass_rate'] - 0.96) < 0.001, "std_test: ['data.x.x_3']['pass_rate'] is wrong"

    assert all([a in log['data.x.x_3']['failed'].keys() for a in [13, 17]]) == True, "std_test: table['data.x.x_3'] is wrong"
    assert table['data.x.x_1'].all() == True, "std_test: table['data.x.x_1'] is wrong"
    assert len(fig.axes) == 3, "std_test: the number of axes for 3d vector is wrong"

    log, table, fig = V3.std_test(limits = 0.1, n_std = 3)
    assert len(log['data.x.x_3']['failed']) == 50, "std_test: ['data.x.x_3']['failed'] for n_std = 3 is wrong"

    log, table, fig = V.std_test(limits = 0.125, n_std = 2)
    assert len(log['data.x.x_1']['failed']) == 2, "std_test: ['data.x.x_1']['failed'] for n_std = 2 is wrong"

    log, table, fig = V.std_test(limits = [0.1], n_std = 1)
    assert len(log['data.x.x_1']['failed']) == 0, "std_test: ['data.x.x_1']['failed'] for n_std = 1 is wrong"
    assert len(fig.axes) == 1, "std_test: the number of axes for 1d vector is wrong"
    assert log['data.x.x_1']['passed'] == True, "std_test: ['data.x.x_1']['passed'] is wrong"

    V3_bin = Validation(df, data_label = ['data.x.x_1', 'data.x.x_2','data.x.x_3'], param_label = 'data.time', 
                      method = 'bin', num = 50, units = 'm')
    log, table, fig = V3_bin.std_test(limits = [0.1, 0.2, 90], n_std = 1)
    assert log['data.x.x_1']['passed'] == True, "std_test: nan_passed default True: log['data.x.x_1']['passed'] is wrong"
    assert list(log['data.x.x_1']['nan_std'].keys())[0] == 49, "std_test: nan_passed default True: log['data.x.x_1']['nan_std']  is wrong"
    assert len(log['data.x.x_3']['failed']) == 0, "std_test: nan_passed default True: log['data.x.x_3']['failed'] is wrong"

    log, table, fig = V3_bin.std_test(limits = [0.25], n_std = 1, nan_passed = False)
    assert log['data.x.x_3']['passed'] == False, "std_test: nan_passed False: log['data.x.x_3']['passed']  is wrong"
    assert list(log['data.x.x_1']['nan_std'].keys())[0] == 49, "std_test: nan_passed = False: log['data.x.x_1']['nan_std'] is wrong"
    assert len(log['data.x.x_3']['failed']) == 50, "std_test: nan_passed default True: log['data.x.x_3']['failed'] is wrong"

    plt.close('all')

    #nan+inf

    df = citros.topic('A').set_order({'sid':'asc','rid':'asc'}).data(['data.y', 'data.y.y_1','data.y.y_2','data.y.y_3','data.time'])

    V = Validation(df, data_label = ['data.y.y_1'], param_label = 'data.y.y_3', 
                        method = 'bin', num = 50, units = 'm', omit_nan_rows = False)
    V3 = Validation(df, data_label = ['data.y.y_1', 'data.y.y_2'], param_label = 'data.y.y_3', 
                        method = 'scale', num = 50, units = 'm', omit_nan_rows = False)
    log3, table3, fig3 = V3.std_test(limits = [30, 25], n_std = 2)
    log, table, fig = V.std_test(limits = 40, n_std = 3, connect_nan_std = True)
    passed = True
    for name in ['data.y.y_1', 'data.y.y_2']:
        passed = passed and log3[name]['passed']
    assert passed, 'std_test, nan+inf 3d: omit_nan_rows False not passed'
    passed = True
    passed = passed and log['data.y.y_1']['passed']
    assert passed, 'std_test, nan+inf 1d: omit_nan_rows False not passed'

    V = Validation(df, data_label = ['data.y.y_1'], param_label = 'data.y.y_3', 
                        method = 'scale', num = 50, units = 'm', omit_nan_rows = True)
    V3 = Validation(df, data_label = ['data.y.y_1', 'data.y.y_2'], param_label = 'data.y.y_3', 
                        method = 'bin', num = 50, units = 'm', omit_nan_rows = True)
    log3, table3, fig3 = V3.std_test(limits = [30], n_std = 2, std_lines = False)
    log, table, fig = V.std_test(limits = 40, n_std = 3, connect_nan_std = True, std_area = False)
    passed = True
    for name in ['data.y.y_1', 'data.y.y_2']:
        passed = passed and log3[name]['passed']
    assert passed, 'std_bound_test, nan+inf: omit_nan_rows True not passed'
    passed = True
    passed = passed and log['data.y.y_1']['passed']
    assert passed, 'std_bound_test, nan+inf: omit_nan_rows True not passed'

    plt.close('all')

def test_mean_test():
    df = citros.topic('A').set_order({'sid':'asc','rid':'asc'}).data(['data.x', 'data.x.x_1','data.x.x_2','data.x.x_3','data.time'])
    V = Validation(df, data_label = ['data.x.x_1'], param_label = 'data.time', 
                      method = 'bin', num = 50, units = 'm')
    V3 = Validation(df, data_label = ['data.x.x_1', 'data.x.x_2','data.x.x_3'], param_label = 'data.time', 
                        method = 'scale', num = 50, units = 'm')
    
    log, table, fig = V3.mean_test(limits = [[-0.1, 0.08], 0.1, 0.1])
    assert (log['test_param']['limits'][0][0] == -0.1) and (log['test_param']['limits'][0][1] == 0.08) \
        and (log['test_param']['limits'][1] == 0.1) and (log['test_param']['limits'][2] == 0.1), "mean_test: 'test_param' are wrong"
    
    assert log['data.x.x_1']['passed'] == True, "mean_test: ['data.x.x_1']['passed'] is wrong"
    assert abs(log['data.x.x_1']['pass_rate'] - 1.0) < 0.001, "mean_test: ['data.x.x_1']['pass_rate'] is wrong"
    assert log['data.x.x_3']['passed'] == False, "mean_test: ['data.x.x_3']['passed'] is wrong"
    assert abs(log['data.x.x_3']['pass_rate']) < 0.001, "mean_test: ['data.x.x_3']['pass_rate'] is wrong"
    assert len(log['data.x.x_3']['failed']) == 50, "mean_test: ['data.x.x_3']['failed'] is wrong"
    assert len(log['data.x.x_1']['failed']) == 0, "mean_test: ['data.x.x_1']['failed'] is wrong"
    assert len(fig.axes) == 3, "mean_test: the number of axes for 3d vector is wrong"

    log, table, fig = V3.mean_test(limits = [[-0.1, 0.05], 0.078])
    assert log is None, "mean_test: passing wrong limits does not lead to None output"

    log, table, fig = V3.mean_test(limits = [[-0.1, 0.08], 0.1, [0, 200]])
    assert all([x in ['data.time', 'data.x.x_1', 'data.x.x_2', 'data.x.x_3'] for x in table.columns]), "mean_test: columns are wrong"
    assert table[['data.x.x_1','data.x.x_2','data.x.x_3']].all().all() == True, "mean_test: table is wrong"

    log, table, fig = V3.mean_test(limits = [[-0.1, 0.08], 0.1, [0, 200]])
    assert all([x in ['data.time', 'data.x.x_1', 'data.x.x_2', 'data.x.x_3'] for x in table.columns]), "mean_test: columns are wrong"
    assert table[['data.x.x_1','data.x.x_2','data.x.x_3']].all().all() == True, "mean_test: table is wrong"

    log, table, fig = V.mean_test(limits = [-0.1, 0.08])
    # all pass the test
    assert len(fig.axes) == 1, "mean_test: the number of axes for 1d vector is wrong"
    assert log['data.x.x_1']['passed'] == True, "mean_test: 1d vector: ['data.x.x_1']['passed'] is wrong"
    assert abs(log['data.x.x_1']['pass_rate'] - 1) < 0.001, "mean_test: 1d vector: ['data.x.x_1']['pass_rate'] is wrong"
    assert len(log['data.x.x_1']['failed']) == 0, "mean_test: 1d vector: length of 'failed' is wrong"
    assert all([x in ['data.time', 'data.x.x_1'] for x in table.columns]) == True, "mean_test: 1d vector: table column names are wrong"

    log, table, fig = V.mean_test(limits = 0.001)
    # all fail test
    assert log['data.x.x_1']['passed'] == False, "mean_test: 1d vector: ['data.x.x_1']['passed'] is wrong"
    assert abs(log['data.x.x_1']['pass_rate']) < 0.001, "mean_test: 1d vector: ['data.x.x_1']['pass_rate'] is wrong"
    assert len(log['data.x.x_1']['failed']) == 50, "mean_test: 1d vector: length of 'failed' is wrong"

    log, table, fig = V.mean_test(limits = [0.001, 0.44, 0.22])
    assert log is None, "test_norm_test: passing wrong limits does not lead to None output"

    plt.close('all')

    #nan + inf
    df = citros.topic('A').set_order({'sid':'asc','rid':'asc'}).data(['data.y', 'data.y.y_1','data.y.y_2','data.y.y_3','data.time'])
    V = Validation(df, data_label = ['data.y.y_1'], param_label = 'data.y.y_3', 
                        method = 'bin', num = 50, units = 'm', omit_nan_rows = False)
    V3 = Validation(df, data_label = ['data.y.y_1', 'data.y.y_2'], param_label = 'data.y.y_3', 
                        method = 'scale', num = 50, units = 'm', omit_nan_rows = False)
    log3, table3, fig3 = V3.mean_test(limits = [10])
    log, table, fig = V.mean_test(limits = [10])

    passed = True
    for name in ['data.y.y_1', 'data.y.y_2']:
        passed = passed and log3[name]['passed']
    assert passed, 'std_mean_test, nan+inf: omit_nan_rows False not passed'

    passed = log['data.y.y_1']['passed']
    assert passed, 'std_mean_test, nan+inf: omit_nan_rows False not passed'

    V = Validation(df, data_label = ['data.y.y_1'], param_label = 'data.y.y_3', 
                        method = 'scale', num = 50, units = 'm', omit_nan_rows = True)
    V3 = Validation(df, data_label = ['data.y.y_1', 'data.y.y_2'], param_label = 'data.y.y_3', 
                        method = 'bin', num = 50, units = 'm', omit_nan_rows = True)
    log3, table3, fig3 = V3.mean_test(limits = [10])
    log, table, fig = V.mean_test(limits = [10])

    passed = True
    for name in ['data.y.y_1', 'data.y.y_2']:
        passed = passed and log3[name]['passed']
    assert passed, 'std_mean_test, nan+inf: omit_nan_rows True not passed'

    passed = log['data.y.y_1']['passed']
    assert passed, 'std_mean_test, nan+inf: omit_nan_rows True not passed'

    plt.close('all')

def test_norm_test():
    df = citros.topic('A').set_order({'sid':'asc','rid':'asc'}).data(['data.x', 'data.x.x_1','data.x.x_2','data.x.x_3','data.time'])
    V = Validation(df, data_label = ['data.x.x_1'], param_label = 'data.time', 
                      method = 'bin', num = 50, units = 'm')
    V3 = Validation(df, data_label = ['data.x.x_1', 'data.x.x_2','data.x.x_3'], param_label = 'data.time', 
                        method = 'scale', num = 50, units = 'm')
    
    log, table, fig = V3.norm_test(norm_type = 'Linf', limits = [[1.0, 0.1], 0.5])
    assert log is None, "test_norm_test: passing wrong limits does not lead to None output"

    log, table, fig = V3.norm_test(norm_type = 'Linf', limits = [1.0, 0.1, 0.5])
    assert log['data.x.x_1']['passed'] == True, "norm_test: ['data.x.x_1']['passed'] is wrong"
    assert log['data.x.x_3']['passed'] == False, "norm_test: ['data.x.x_1']['passed'] is wrong"
    assert abs(log['data.x.x_1']['pass_rate'] - 1.0) < 0.001, "norm_test: ['data.x.x_1']['pass_rate'] is wrong"
    assert abs(log['data.x.x_3']['pass_rate']) < 0.001, "norm_test: ['data.x.x_1']['pass_rate'] is wrong"
    assert len(log['data.x.x_3']['failed']) == 3, "number of failed sid is wrong"

    cols = ['data.x.x_1', 'data.x.x_2', 'data.x.x_3']
    for s in set(df['sid']):
        for col in cols:
            S = max(abs(V3.db.data.xs(s, level = 'sid')[col]))
            assert abs(S - log[col]['norm_value'][s]) < 0.0001, f"norm_test: sid = {s}, col = {col} is wrong"
    assert table['data.x.x_1'].all() and table['data.x.x_3'].any() == False, "norm_test Linf: table for is wrong"
    assert len(fig.axes) == 3, "norm_test: the number of axes for 3d vector is wrong"

    log, table, fig = V3.norm_test(norm_type = 'L2', limits = [1.0, 0.1, 0.5])
    cols = ['data.x.x_1', 'data.x.x_2', 'data.x.x_3']
    for s in set(df['sid']):
        for col in cols:
            S = 0
            for x in V3.db.data.xs(s, level = 'sid')[col]:
                S += x**2
            assert abs(np.sqrt(S) - log[col]['norm_value'][s]) < 0.0001, f"norm_test L2: sid = {s}, col = {col} is wrong"

    V = Validation(df, data_label = ['data.x.x_1'], param_label = 'data.time', 
                      method = 'bin', num = 50, units = 'm')
    log, table, fig = V.norm_test(norm_type = 'L2', limits = 0.4)
    assert log['data.x.x_1']['passed'] == True, "norm_test 1d L2: ['data.x.x_1']['passed'] is wrong"
    assert abs(log['data.x.x_1']['pass_rate'] - 1.0) < 0.001, "norm_test 1d L2: ['data.x.x_1']['pass_rate'] is wrong"
    assert len(log['data.x.x_1']['failed']) == 0, "norm tests 1d L2: number of failed sid is wrong"

    for s in set(df['sid']):
        S = 0
        for x in V.db.data.xs(s, level = 'sid')['data.x.x_1']:
            S += x**2
        assert abs(np.sqrt(S) - log['data.x.x_1']['norm_value'][s]) < 0.0001, f"norm_test 1d L2: sid = {s} is wrong"

    log, table, fig = V.norm_test(norm_type = 'Linf', limits = 0.1)
    assert log['data.x.x_1']['passed'] == True, "norm_test 1d Linf: ['data.x.x_1']['passed'] is wrong"
    assert abs(log['data.x.x_1']['pass_rate'] - 1.0) < 0.001, "norm_test 1d Linf: ['data.x.x_1']['pass_rate'] is wrong"
    assert len(log['data.x.x_1']['failed']) == 0, "norm_test 1d Linf: number of failed sid is wrong"

    for s in set(df['sid']):
        S = max(abs(V.db.data.xs(s, level = 'sid')['data.x.x_1']))
        assert abs(S - log['data.x.x_1']['norm_value'][s]) < 0.0001, f"norm_test 1d Linf: sid = {s} is wrong"

    plt.close('all')

    #nan+inf
    df = citros.topic('A').set_order({'sid':'asc','rid':'asc'}).data(['data.y', 'data.y.y_1','data.y.y_2','data.y.y_3','data.time'])

    V = Validation(df, data_label = ['data.y.y_1'], param_label = 'data.y.y_3', 
                        method = 'scale', num = 50, units = 'm', omit_nan_rows = False)#, inf_vals = None)
    V3 = Validation(df, data_label = ['data.y.y_1', 'data.y.y_2'], param_label = 'data.y.y_3', 
                        method = 'bin', num = 50, units = 'm', omit_nan_rows = False)
    log3, table3, fig3 = V3.norm_test(norm_type = 'Linf', limits = 10)
    log, table, fig = V.norm_test(norm_type = 'Linf', limits = 1)

    passed = True
    for name in ['data.y.y_1', 'data.y.y_2']:
        passed = passed and log3[name]['passed']
    assert passed, 'norm_test 2d Linf, nan+inf: omit_nan_rows False not passed'
    passed = not log['data.y.y_1']['passed']
    assert passed, 'norm_test 1d Linf, nan+inf: omit_nan_rows False not passed'

    plt.close('all')

    V = Validation(df, data_label = ['data.y.y_1'], param_label = 'data.y.y_3', 
                        method = 'scale', num = 50, units = 'm', omit_nan_rows = True)#, inf_vals = None)
    V3 = Validation(df, data_label = ['data.y.y_1', 'data.y.y_2'], param_label = 'data.y.y_3', 
                        method = 'bin', num = 50, units = 'm', omit_nan_rows = True)
    log3, table3, fig3 = V3.norm_test(norm_type = 'Linf', limits = 10)
    log, table, fig = V.norm_test(norm_type = 'Linf', limits = 1)

    passed = True
    for name in ['data.y.y_1', 'data.y.y_2']:
        passed = passed and log3[name]['passed']
    assert passed, 'norm_test 2d Linf, nan+inf: omit_nan_rows False not passed'
    passed = not log['data.y.y_1']['passed']
    assert passed, 'norm_test 1d Linf, nan+inf: omit_nan_rows False not passed'

    plt.close('all')

    V = Validation(df, data_label = ['data.y.y_1'], param_label = 'data.y.y_3', 
                        method = 'scale', num = 50, units = 'm', omit_nan_rows = False)
    V3 = Validation(df, data_label = ['data.y.y_1', 'data.y.y_2'], param_label = 'data.y.y_3', 
                        method = 'bin', num = 50, units = 'm', omit_nan_rows =False)
    log3, table3, fig3 = V3.norm_test(norm_type = 'L2', limits = 35)
    log, table, fig = V.norm_test(norm_type = 'L2', limits = 25)

    passed = True
    for name in ['data.y.y_1', 'data.y.y_2']:
        passed = passed and log3[name]['passed']
    assert passed, 'norm_test 2d L2, nan+inf: omit_nan_rows False not passed'
    passed = not log['data.y.y_1']['passed']
    assert passed, 'norm_test 1d L2, nan+inf: omit_nan_rows False not passed'

    plt.close('all')

    V = Validation(df, data_label = ['data.y.y_1'], param_label = 'data.y.y_3', 
                            method = 'scale', num = 50, units = 'm', omit_nan_rows = True)
    V3 = Validation(df, data_label = ['data.y.y_1', 'data.y.y_2'], param_label = 'data.y.y_3', 
                        method = 'bin', num = 50, units = 'm', omit_nan_rows =True)
    log3, table3, fig3 = V3.norm_test(norm_type = 'L2', limits = 35)
    log, table, fig = V.norm_test(norm_type = 'L2', limits = 25)

    passed = True
    for name in ['data.y.y_1', 'data.y.y_2']:
        passed = passed and log3[name]['passed']
    assert passed, 'norm_test 2d L2, nan+inf: omit_nan_rows True not passed'
    passed = not log['data.y.y_1']['passed']
    assert passed, 'norm_test 1d L2, nan+inf: omit_nan_rows True not passed'

    plt.close('all')

def test_sid_test():
    df = citros.topic('A').set_order({'sid':'asc','rid':'asc'}).data(['data.x', 'data.x.x_1','data.x.x_2','data.x.x_3','data.time'])
    V = Validation(df, data_label = ['data.x.x_1'], param_label = 'data.time', 
                      method = 'bin', num = 50, units = 'm')
    V3 = Validation(df, data_label = ['data.x.x_1', 'data.x.x_2','data.x.x_3'], param_label = 'data.time', 
                        method = 'scale', num = 50, units = 'm')
    log, table, fig = V3.sid_test(limits = [0.1, [-0.2, 0.02], 300])
    assert log['test_param']['limits'][0] == 0.1 and log['test_param']['limits'][1][0] == -0.2 \
        and log['test_param']['limits'][1][1] == 0.02 and log['test_param']['limits'][2] == 300, "sid test tests param are wrong"
    
    assert log['data.x.x_1']['passed'] == True, "sid test: ['data.x.x_1']['passed'] is wrong"
    assert log['data.x.x_2']['passed'] == False, "sid test: ['data.x.x_2']['passed'] is wrong"
    assert abs(log['data.x.x_1']['pass_rate']['sid_fraction'] - 1) < 0.001, "sid test: ['data.x.x_1']['passed'] is wrong"
    assert abs(log['data.x.x_2']['pass_rate']['sid_fraction']) < 0.001, "sid test: ['data.x.x_2']['passed'] is wrong"
    assert abs(log['data.x.x_1']['pass_rate'][3] - 1) < 0.001, "sid test: ['data.x.x_1']['passed'] is wrong"
    for s in set(table.index.get_level_values('sid')):
        assert abs(table['data.x.x_2'].xs(s, level = 'sid').value_counts()[True]/len(table['data.x.x_2'].xs(s, level = 'sid')) - \
                log['data.x.x_2']['pass_rate'][s]) < 0.001, f"sid test, sid = {s}: 'data.x.x_2' pass rate is wrong"
        assert abs(table['data.x.x_2'].xs(s, level = 'sid').value_counts()[False] - \
                len(log['data.x.x_2']['failed'][s])) < 0.001, f"sid test, sid = {s}: 'data.x.x_2' failed length is wrong"
    assert len(log['data.x.x_1']['failed']) == 0, "sid test, failed length is wrong"
    assert len(log['data.x.x_2']['failed']) == 3, "sid test, failed length is wrong"
    assert len(fig.axes) == 3, "sid test 3d vector, ax number is wrong"

    log, table, fig = V.sid_test(limits = [0.1, [-0.2, 0.02], 300])
    assert log is None, "passing wrong limits does not lead to None output"
    log, table, fig = V.sid_test(limits = [0.1])
    assert log['test_param']['limits'][0] == 0.1, "sid test 1d vector test_param is wrong"
    
    assert log['data.x.x_1']['passed'] == True, "sid test 1d: ['data.x.x_1']['passed'] is wrong"
    assert abs(log['data.x.x_1']['pass_rate']['sid_fraction'] - 1) < 0.001, "sid test: ['data.x.x_1']['pass_rate']['sid_fraction'] is wrong"
    assert abs(log['data.x.x_1']['pass_rate'][3] - 1) < 0.001, "sid test: ['data.x.x_1']['pass_rate'] sid 3 is wrong"
    assert len(log['data.x.x_1']['failed']) == 0, "sid test, failed length is wrong"

    log, table, fig = V.sid_test(limits = 0.01)
    assert abs(log['data.x.x_1']['pass_rate']['sid_fraction']) < 0.001, "sid test: ['data.x.x_1']['sid_fraction'] is wrong"
    for s in set(table.index.get_level_values('sid')):
        assert abs(table['data.x.x_1'].xs(s, level = 'sid').value_counts()[True]/len(table['data.x.x_1'].xs(s, level = 'sid')) - \
                log['data.x.x_1']['pass_rate'][s]) < 0.001, f"sid test, sid = {s}: 'data.x.x_1' pass rate is wrong"
        assert abs(table['data.x.x_1'].xs(s, level = 'sid').value_counts()[False] - \
                len(log['data.x.x_1']['failed'][s])) < 0.001, f"sid test, sid = {s}: 'data.x.x_1' failed length is wrong"
    assert len(log['data.x.x_1']['failed']) == 3, "sid test, failed length is wrong"

    plt.close('all')
    df = citros.topic('A').set_order({'sid':'asc','rid':'asc'}).data(['data.y', 'data.y.y_1','data.y.y_2','data.y.y_3','data.time'])

    V = Validation(df, data_label = ['data.y.y_1'], param_label = 'data.y.y_3', 
                        method = 'scale', num = 50, units = 'm', omit_nan_rows = False)
    V3 = Validation(df, data_label = ['data.y.y_1', 'data.y.y_2'], param_label = 'data.y.y_3', 
                        method = 'bin', num = 50, units = 'm', omit_nan_rows =False)
    log3, table3, fig3 = V3.sid_test(limits = 10)
    log, table, fig = V.sid_test(limits = 10)

    passed = True
    for name in ['data.y.y_1', 'data.y.y_2']:
        passed = passed and log3[name]['passed']
    assert passed, 'norm_test 2d L2, nan+inf: omit_nan_rows False not passed'
    passed = log['data.y.y_1']['passed']
    assert passed, 'norm_test 1d L2, nan+inf: omit_nan_rows False not passed'

    V = Validation(df, data_label = ['data.y.y_1'], param_label = 'data.y.y_3', 
                            method = 'scale', num = 50, units = 'm', omit_nan_rows = True)
    V3 = Validation(df, data_label = ['data.y.y_1', 'data.y.y_2'], param_label = 'data.y.y_3', 
                        method = 'bin', num = 50, units = 'm', omit_nan_rows =True)
    log3, table3, fig3 = V3.sid_test(limits = 10)
    log, table, fig = V.sid_test(limits = 10)

    passed = True
    for name in ['data.y.y_1', 'data.y.y_2']:
        passed = passed and log3[name]['passed']
    assert passed, 'sid_test 2d, nan+inf: omit_nan_rows True not passed'
    passed = log['data.y.y_1']['passed']
    assert passed, 'sid_test 1d L2, nan+inf: omit_nan_rows True not passed'

    plt.close('all')

def test_set_tests():
    df = citros.topic('A').set_order({'sid':'asc','rid':'asc'}).data(['data.x', 'data.x.x_1','data.x.x_2','data.x.x_3','data.time'])
    V = Validation(df, data_label = ['data.x.x_1'], param_label = 'data.time', 
                      method = 'bin', num = 50, units = 'm')
    V3 = Validation(df, data_label = ['data.x.x_1', 'data.x.x_2','data.x.x_3'], param_label = 'data.time', 
                        method = 'scale', num = 50, units = 'm')
    test_names = ['std_bound', 'mean', 'sid', 'norm_L2', 'norm_Linf']
    log, tables, figures = V3.set_tests(test_method = {'std_bound' : {'limits' : 1.0, 'n_std': 3, 'nan_passed': True},
                                       'mean' : {'limits' : 1.0},
                                       'sid' : {'limits' : 1.0},
                                       'norm_L2' : {'limits' : 1.0},
                                       'norm_Linf' : {'limits' : 1.0}})
    
    assert all([name in log.keys() for name in test_names]), "set_tests: test names are wrong"
    assert all([name in tables.keys() for name in test_names]), "set_tests: test names are wrong"
    assert all([name in figures.keys() for name in test_names]), "set_tests: test names are wrong"

    log, tables, figures = V.set_tests(test_method = {'std_bound' : {'limits' : 1.0, 'n_std': 3, 'nan_passed': True},
                                       'mean' : {'limits' : 1.0},
                                       'sid' : {'limits' : 1.0},
                                       'norm_L2' : {'limits' : 1.0},
                                       'norm_Linf' : {'limits' : 1.0}})
    
    assert all([name in log.keys() for name in test_names]), "set_tests 1d: test names are wrong"
    assert all([name in tables.keys() for name in test_names]), "set_tests 1d: test names are wrong"
    assert all([name in figures.keys() for name in test_names]), "set_tests 1d: test names are wrong"

    plt.close('all')

    #nan+inf
    df = citros.topic('A').set_order({'sid':'asc','rid':'asc'}).data(['data.y', 'data.y.y_1','data.y.y_2','data.y.y_3','data.time'])
    V3 = Validation(df, data_label = ['data.y.y_1', 'data.y.y_2'], param_label = 'data.y.y_3', 
                        method = 'bin', num = 50, units = 'm', omit_nan_rows =False)
    log, tables, figures = V3.set_tests(test_method = {'std_bound' : {'limits' : 20.0, 'n_std': 1, 'nan_passed': True, 'std_area' : False, 'connect_nan_std':True},
                                        'mean' : {'limits' : 20.0},
                                        'sid' : {'limits' : 20.0},
                                        'norm_L2' : {'limits' : 35.0},
                                        'norm_Linf' : {'limits' : 10.0}})
    plt.close('all')
    passed = True
    for method in log.keys():
        for name in ['data.y.y_1', 'data.y.y_2']:
            passed = passed and log[method][name]['passed']
    assert passed, "set_tests, omit_nan_rows =False: not passed"

    V3 = Validation(df, data_label = ['data.y.y_1', 'data.y.y_2'], param_label = 'data.y.y_3', 
                        method = 'scale', num = 50, units = 'm', omit_nan_rows =True)
    log, tables, figures = V3.set_tests(test_method = {'std_bound' : {'limits' : 20.0, 'n_std': 1, 'nan_passed': True, 'std_area' : False, 'connect_nan_std':True},
                                        'mean' : {'limits' : 20.0},
                                        'sid' : {'limits' : 20.0},
                                        'norm_L2' : {'limits' : 40.0},
                                        'norm_Linf' : {'limits' : 10.0}})
    plt.close('all')
    passed = True
    for method in log.keys():
        for name in ['data.y.y_1', 'data.y.y_2']:
            passed = passed and log[method][name]['passed']
    assert passed, "set_tests, omit_nan_rows =True: not passed"