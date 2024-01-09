import matplotlib.pyplot as plt

from citros import CitrosDB

'''
tests for lulav data access module

just type:

pytest

in terminal in this folder
'''

#connect to a database
table_name = 'test_table'

citros = CitrosDB(simulation = 'public',
                  batch = table_name)

def test_topic():
    assert citros.topic('B')._topic == ['B'], 'topic(): topic was set wrong'
    assert citros.topic(['B', 'C'])._topic == ['B', 'C'], 'topic(): topic was set wrong'

def test_time():
    assert citros.time(start = 5000000000)._time_val['time'] == {'>=': 5000000000}, 'time(): start is wrong'
    assert citros.time(start = 5000000000, end = 10000000000)._time_val['time']['>='] == 5000000000, 'time(): start is wrong'
    assert citros.time(start = 5000000000, end = 10000000000)._time_val['time']['<='] == 10000000000, 'time(): end is wrong'
    assert citros.time(end = 10000000000)._time_val['time']['<='] == 10000000000, 'time(): start is wrong'
    assert citros.time(start = 2000000000, duration = 5000000000)._time_val['time']['>='] == 2000000000, 'time(): start is wrong'
    assert citros.time(start = 2000000000, duration = 5000000000)._time_val['time']['<'] == 7000000000, 'time(): duration is wrong'
    assert citros.time(duration = 5000000000)._time_val['time']['<'] == 5000000000, 'time(): duration is wrong'
    assert citros.time(start = 5.5, end = 10.8)._time_val['time']['>='] == 5, 'time(): start cast to int is wrong'
    assert citros.time(start = 5.5, end = 10.8)._time_val['time']['<='] == 10, 'time(): end cast to int is wrong'
    assert citros.time(duration = 10.8)._time_val['time']['<'] == 10, 'time(): duration cast to int is wrong'

def test_rid():
    assert citros.rid(1)._rid_val['rid'] == [1], 'rid(): value is wrong'
    assert citros.rid([1, 2])._rid_val['rid'] == [1, 2], 'rid(): value is wrong'
    assert citros.rid(1.5)._rid_val['rid'] == [1], 'rid(): value cast to int is wrong'
    assert citros.rid([1.4, 2.5])._rid_val['rid'] == [1, 2], 'rid(): value cast to is wrong'
    assert citros.rid(start = 5)._rid_val['rid'] == {'>=': 5}, 'rid(): start is wrong'
    assert citros.rid(start = 5, end = 10)._rid_val['rid']['>='] == 5, 'rid(): start is wrong'
    assert citros.rid(start = 5, end = 10)._rid_val['rid']['<='] == 10, 'rid(): end is wrong'
    assert citros.rid(end = 10)._rid_val['rid']['<='] == 10, 'rid(): start is wrong'
    assert citros.rid(start = 2, count = 5)._rid_val['rid']['>='] == 2, 'rid(): start is wrong'
    assert citros.rid(start = 2, count = 5)._rid_val['rid']['<'] == 7, 'rid(): count is wrong'
    assert citros.rid(count = 5)._rid_val['rid']['<'] == 5, 'rid(): count is wrong'
    assert citros.rid(start = 5.5, end = 10.8)._rid_val['rid']['>='] == 5, 'rid(): start cast to int is wrong'
    assert citros.rid(start = 5.5, end = 10.8)._rid_val['rid']['<='] == 10, 'rid(): end cast to int is wrong'
    assert citros.rid(count = 10.8)._rid_val['rid']['<'] == 10, 'rid(): count cast to int is wrong'
    assert citros.rid([1, 2], start = 5)._rid_val['rid'] == [1, 2], 'rid(): value override is wrong'
    assert citros.rid([1, 2], end = 5)._rid_val['rid'] == [1, 2], 'rid(): value override is wrong'
    assert citros.rid([1, 2], count = 5)._rid_val['rid'] == [1, 2], 'rid(): value override is wrong'

def test_sid():
    assert citros.sid([1])._sid == [1], 'sid(): sid is wrong'
    assert citros.sid(1)._sid == [1], 'sid(): sid is wrong'
    assert citros.sid([10,5])._sid == [10,5], 'sid(): sid is wrong'
    assert citros.sid(11.8)._sid == [11], 'sid(): cast to int is wrong'
    assert citros.sid([11.8, 15.6])._sid == [11,15], 'sid(): cast to int is wrong'
    assert citros.sid(start = 5)._sid_val['sid'] == {'>=': 5}, 'sid(): start is wrong'
    assert citros.sid(start = 5, end = 10)._sid_val['sid']['>='] == 5, 'sid(): start is wrong'
    assert citros.sid(start = 5, end = 10)._sid_val['sid']['<='] == 10, 'sid(): end is wrong'
    assert citros.sid(end = 10)._sid_val['sid']['<='] == 10, 'sid(): start is wrong'
    assert citros.sid(start = 2, count = 5)._sid_val['sid']['>='] == 2, 'sid(): start is wrong'
    assert citros.sid(start = 2, count = 5)._sid_val['sid']['<'] == 7, 'sid(): count is wrong'
    assert citros.sid(count = 5)._sid_val['sid']['<'] == 5, 'sid(): count is wrong'
    assert citros.sid(start = 5.5, end = 10.8)._sid_val['sid']['>='] == 5, 'sid(): start cast to int is wrong'
    assert citros.sid(start = 5.5, end = 10.8)._sid_val['sid']['<='] == 10, 'sid(): end cast to int is wrong'
    assert citros.sid(count = 10.8)._sid_val['sid']['<'] == 10, 'sid(): count cast to int is wrong'
    
def test_set_filter():
    assert citros.set_filter({'x': {'gte': 3}, 'y': [1,2,3]})._filter_by['x'] == {'gte': 3}, 'set_filter() result is wrong'
    assert citros.set_filter({'x': {'gte': 3}, 'y': [1,2,3]})._filter_by['y'] == [1,2,3], 'set_filter() result is wrong'
    assert citros.set_filter({'x': {'>': 3}, 'y': [1,2,3]})._filter_by['x'] == {'>': 3}, 'set_filter() result is wrong'
    assert citros.set_filter({'x': {'<=': 3}, 'y': [1,2,3]})._filter_by['x'] == {'<=': 3}, 'set_filter() result is wrong'

def test_set_order():
    assert citros.set_order({'x': 'asc', 'y': 'desc'})._order_by['x'] == 'asc', 'set_order() result is wrong'
    assert citros.set_order({'x': 'AsC', 'y': 'Desc'})._order_by['x'] == 'asc', 'set_order() result is wrong'
    assert citros.set_order({'x': 'AsC', 'y': 'Desc'})._order_by['y'] == 'desc', 'set_order() result is wrong'
    assert citros.set_order(['x', 'y'])._order_by['x'] == 'asc', 'set_order() result is wrong'
    assert citros.set_order(['x', 'y'])._order_by['y'] == 'asc', 'set_order() result is wrong'
    assert citros.set_order('x')._order_by['x'] == 'asc', 'set_order() result is wrong'

def test_skip():
    assert citros.skip(10)._method == 'skip', 'skip(): method set wrong'
    assert citros.skip(10)._n_skip == 10, 'skip(): n_skip is wrong'

def test_avg():
    assert citros.avg(10)._method == 'avg', 'avg(): method set wrong'
    assert citros.avg(10)._n_avg == 10, 'avg(): n_avg is wrong'

def test_move_avg():
    assert citros.move_avg(15, 10)._method == 'move_avg', 'move_avg(): method set wrong'
    assert citros.move_avg(15, 10)._n_avg == 15, 'move_avg(): n_avg is wrong'
    assert citros.move_avg(15, 10)._n_skip == 10, 'move_avg(): n_skip is wrong'

def test_info():
    #info I
    result = citros.info()
    assert result['message_count'] == 2000, 'info I: message_count is wrong'
    assert result['topic_list'] == ['A', 'B', 'C', 'D'], 'info I: topic_list is wrong'
    assert isinstance(result['size'], str), 'info I: size is wrong'
    assert result['sid_list'] == [1, 2, 3], 'info I: sid_list is wrong'

    #info II
    result = citros.topic('C').info()
    assert result['message_count'] == 513, 'info II: message_count is wrong'
    assert isinstance(result['size'], str), 'info I: size type is wrong'
    assert result['topics']['C']['message_count'] == 513, 'info II: topics: message_count is wrong'
    assert result['topics']['C']['type'] == 'c', 'info II: topics: type is wrong'

    #info III
    result = citros.sid(1).info()
    assert result['message_count'] == 688, 'info III: message_count is wrong'
    assert result['sids'][1]['topics']['A']['message_count'] == 155, 'info III: A: message_count is wrong'
    assert abs(result['sids'][1]['topics']['A']['frequency'] - 1.547) < 0.01, 'info III: A: frequency is wrong'

    #info IV
    result = citros.sid([1,2]).info()
    assert abs(result['sids'][2]['topics']['A']['start_time'] - 457223744) < 0.01, 'info IV: start_time is wrong'
    assert abs(result['sids'][1]['topics']['B']['end_time'] - 100752013600) < 0.01, 'info IV: end_time is wrong'
    assert abs(result['sids'][2]['topics']['B']['frequency'] - 1.677) < 0.001, 'info IV: B: frequency is wrong'

    #info V
    result = citros.topic('D').sid([1,2]).info()
    assert result['message_count'] == 356, 'info V: message_count is wrong'
    assert abs(result['sids'][2]['topics']['D']['duration'] - 98875941479) < 0.001, 'info V: duration is wrong'

def test_batch():
    citros1 = CitrosDB()
    assert citros1.batch()._batch_name is None, 'batch(): batch is not None'
    assert citros1.batch('11-22-33')._batch_name == '11-22-33', 'batch(): batch is not set right'
    citros1.batch('1-1-1', inplace = True)
    assert citros1._batch_name == '1-1-1', 'batch(): batch is not set right'
    citros1.batch(inplace = True)
    assert citros1._batch_name is None, 'batch(): batch is not None'
    
def test_get_batch_name():
    citros1 = CitrosDB()
    assert citros1.get_batch_name() is None, 'get_batch_name(): batch_name is not None'
    citros1 = CitrosDB(batch = 'new_batch_name')
    assert citros1.get_batch_name() == 'new_batch_name', 'get_batch_name(): batch_name is not right'

def test_simulation():
    citros1 = CitrosDB()
    assert citros1._simulation is None, 'simulation(): simulation is not None'
    assert citros1.simulation()._simulation is None, 'simulation(): simulation is not None'
    assert citros1.simulation('new_simulation_name')._simulation == 'new_simulation_name', 'simulation(): simulation is not set right'

    citros1 = CitrosDB(simulation = 'new_simulation')
    assert citros1._simulation == 'new_simulation', 'simulation(): simulation is not None'
    assert citros1.simulation()._simulation is None, 'simulation(): simulation is not None'
    assert citros1.simulation('new_simulation_name')._simulation == 'new_simulation_name', 'simulation(): simulation is not set right'

def test_get_simulation_name():
    citros1 = CitrosDB()
    assert citros1.get_simulation_name() is None, 'get_simulation_name(): simulation name is not None'
    assert citros1.simulation('new_simulation').get_simulation_name() == 'new_simulation', 'get_simulation_name(): simulation name is not got right'

def test_get_simulation():
    citros1 = CitrosDB()
    assert citros1.get_simulation()['name'] is None, 'get_simulation(): simulation is not None'
    assert citros1.simulation('new_simulation').get_simulation()['name'] == 'new_simulation', 'get_simulation(): simulation is not got right'

    citros1 = CitrosDB(simulation = 'new_simulation')
    assert citros1.get_simulation()['name'] == 'new_simulation', 'get_simulation(): simulation is not got right'

def test_is_batch_set():
    citros1 = CitrosDB()
    assert citros1._is_batch_set() is False, 'is_batch_set(): wrong when batch is not set'
    citros1.batch(table_name, inplace = True)
    assert citros1._is_batch_set() is True, 'is_batch_set(): wrong result when the batch exists'
    assert citros._is_batch_set() is True, 'is_batch_set(): wrong result when the batch was passed during creation'

def test_is_batch_in_database():
    citros1 = CitrosDB(simulation = 'public')
    assert citros1._is_batch_in_database('11-22-33') is False, 'is_batch_set(): wrong when the batch does not exist'
    assert citros1._is_batch_in_database(table_name) is True, 'is_batch_set(): wrong when the batch exists'

def test_data():
    #table I
    df = citros.topic('B').data()
    assert len(df) == 494, 'table I: length is wrong'

    #table II
    df = citros.topic('A').sid([1,2]).rid(start = 1, end = 7).time(start = 3000000000, end = 17000000000).data()
    assert len(df) == 7, 'table II: length is wrong'
    assert len(df.columns) == 16, 'table II: number of columns is wrong'

    #table III
    df = citros.topic('A').sid([1,2]).rid(start = 4).time(start = 3000000000, duration = 4000000000).\
        data(['data.x.x_1','data.note[2][0]','data.note[3].n'])
    df.set_index(['sid','rid'], inplace = True)
    assert df['data.note[2][0]'].loc[(2,4)] == 63, 'table III: value in the column data.note[2][0] is wrong'
    assert df['data.note[3].n'].loc[(2,4)] == 49, 'table III: value in the column data.note[2][0] is wrong'

    #table IV
    df = citros.topic('A').rid(start = 5, count = 1).time(start = 4000000000).\
        data(['data.x.x_1','data.note[2][0]','data.note[3].n'])
    assert df.iloc[0]['data.note[3].n']  == 59, 'table IV: values in the column "data.x.x_1" is wrong'

    #table V
    df = citros.topic('A').rid(start = 1, count = 5).avg(2).\
        data(['data.x.x_1','data.note[2][0]'])
    df.set_index(['sid','rid'], inplace = True)

    assert abs(df.loc[(1,1),'time'] - 679271808) < 0.001, 'table V: avg: sid=1, rid = 1: time is wrong'
    assert abs(df.loc[(1,1),'data.x.x_1'] - 0.012) < 0.001, 'table V: avg: sid=1, rid = 1: "data.x.x_1" is wrong'

    assert abs(df.loc[(3,3),'time'] - 2313463838.5) < 0.001, 'table V: avg: sid=3, rid = 3: time is wrong'
    assert abs(df.loc[(3,3),'data.x.x_1'] - (-0.076)) < 0.001, 'table V: avg: sid=3, rid = 3: "data.x.x_1" is wrong'

    #table VI
    df = citros.topic('A').rid(start = 2, count = 5).skip(3).\
        data(['data.x.x_1','data.note[2][0]'])
    df.set_index(['sid','rid'], inplace = True)

    assert abs(df.loc[(1,2),'time'] - 951279608) < 0.001, 'table VI: skip: sid=1, rid = 2: time is wrong'
    assert abs(df.loc[(1,2),'data.x.x_1'] - 0.016) < 0.1, 'table VI: skip: sid=1, rid = 2: "data.x.x_1" is wrong'

    assert abs(df.loc[(3,5),'time'] - 3015094214) < 0.001, 'table VI: skip: sid=3, rid = 5: time is wrong'
    assert abs(df.loc[(3,5),'data.x.x_1'] - (-0.071)) < 0.001, 'table VI: skip: sid=4, rid = 5: "data.x.x_1" is wrong'

    #table VII
    df = citros.topic('A').rid(start = 2, count = 5).move_avg(3,2).\
        data(['data.x.x_1','data.note[2][0]'])
    df.set_index(['sid','rid'], inplace = True)

    assert abs(df.loc[(1,2),'time'] - 1959866873) < 1, 'table VII: move_avg: sid=1, rid = 2: time is wrong'
    assert abs(df.loc[(1,2),'data.x.x_1'] - 0.024) < 0.1, 'table VII: move_avg: sid=1, rid = 2: "data.x.x_1" is wrong'

    assert abs(df.loc[(2,2),'time'] - 2683647505) < 1, 'table VII: move_avg: sid=2, rid = 2: time is wrong'
    assert abs(df.loc[(2,2),'data.x.x_1'] - (-0.038)) < 0.01, 'table VII: move_avg: sid=2, rid = 2: "data.x.x_1" is wrong'

    assert abs(df.loc[(3,4),'time'] - 3530094020) < 1, 'table VII: move_avg: sid=3, rid = 4: time is wrong'
    assert abs(df.loc[(3,4),'data.x.x_1'] - (-0.071)) < 0.001, 'table VII: move_avg: sid=3, rid = 4: "data.x.x_1" is wrong'

    #table VIII
    result = citros.topic('B').sid().time(start = 5000000000).rid(start = 2).set_filter({'data.x.x_1': {'gte': 0.08}}).data()
    result = citros.topic('B').sid().time(start = 5000000000).rid(start = 2).set_filter({'data.x.x_1': {'>=': 0.08}}).data()
    assert len(result) == 117, 'table VIII: length is wrong'

    #table IX
    result = citros.topic('A').rid(start = 2, count = 5).skip(2).set_filter({'data.x.x_3': {'gte':150}}).\
                    set_order({'sid': 'asc', 'rid': 'asc'}).data(['data.x.x_3','data.note[2][0]'])
    assert len(result) == 3, 'table IX: length is wrong'
    assert result['data.note[2][0]'].iloc[1] == 63, 'table IX: value is wrong'

    #table X
    result = citros.topic('A').sid([1,2]).move_avg(3,3).rid(start = 6, end =16).set_filter({'data.x.x_3': {'gte':130}}).\
                    set_order({'sid':'asc','data.x.x_3':'desc'}).data(['data.x.x_3', 'data.time'])
    assert len(result) == 3, 'table X: length is wrong'
    assert abs(result['data.x.x_3'].iloc[0] - 166.08)<0.01, 'table X: value is wrong'
    assert abs(result['time'].iloc[0] - 4198639459)< 1, 'table X: time is wrong'

    #table XI
    result = citros.topic('A').avg(5).rid(start = 6, end =16).set_filter({'data.x.x_3': {'gte':130}}).\
                    set_order({'data.x.x_3':'asc'}).data(['data.x.x_3', 'data.time'])
    assert len(result) == 5, 'table XI: length is wrong'
    assert abs(result['data.x.x_3'].iloc[1] - 145.08) < 0.01, 'table XI: value is wrong'
    assert abs(result['time'].iloc[2] - 5943826822)<0.001, 'table XI: time is wrong'

    #table XII
    result = citros.topic('A').avg(5).rid(start = 6, end =16).set_filter({'data.x.x_3': {'gte':130}}).\
                    set_order({'data.x.x_3':'asc'}).data(['data.x.x_3', 'data.time'])
    assert len(result) == 5, 'table XII: length is wrong'
    assert abs(result['data.x.x_3'].iloc[1] - 145.08) < 0.01, 'table XII: value is wrong'
    assert abs(result['time'].iloc[2] - 5943826822)<0.001, 'table XII: time is wrong'

    #table XIII nan behavior
    assert abs(citros.topic('A').sid(1).rid(start=2, end=4).avg(3).data(['data.y.y_1'])['data.y.y_1'].iloc[0] - 1.14) < 0.01, 'table XIII: average for column with nan values is wrong'
    assert abs(citros.topic('A').sid(1).rid(start=2, end=5).move_avg(2).data(['data.y.y_1'])['data.y.y_1'].iloc[0] - 6.46) < 0.01, 'table XIII: moving average for column with nan value is wrong'
    assert abs(citros.topic('A').sid(1).rid(start=2, end=5).move_avg(2).data(['data.y.y_1'])['data.y.y_1'].iloc[1] + 4.18) < 0.01, 'table XIII: moving average for column with nan value is wrong'
    assert abs(citros.topic('A').sid(1).rid(start=0, end=5).set_filter({'data.y.y_1':{'gt':0}}).data(['data.y.y_1'])['data.y.y_1'].iloc[0] - 6.46) < 0.01, 'table XIII: set_filter for column with nan value is wrong'
    assert abs(citros.topic('A').sid(1).rid(start=0, end=5).set_order({'data.y.y_1':'asc'}).data(['data.y.y_1'])['data.y.y_1'].iloc[2] - 6.46)<0.01, 'table XIII: set_order for column with nan value is wrong'

    #table XIV additional columns
    df = citros.topic('A').data(['data.x.x_2', 'data.time'])
    assert all([x in df.columns for x in ['sid', 'rid', 'time', 'topic', 'type']]), 'table XIV: wrong additional columns'

    df = citros.topic('A').rid([1,2,3]).data(['data.x.x_2', 'data.time'], additional_columns = ['topic','time'])
    assert all([x in df.columns for x in['sid', 'time', 'topic']]), 'table XIV: wrong additional columns: columns are not quired'
    assert all([x not in df.columns for x in ['rid', 'type']]), 'table XIV: wrong additional columns: some of the columns should not be queried'
    df1 = citros.topic('A').rid([1,2,3]).data(['data.x.x_2', 'data.time'])
    assert all(df1['rid']<=3) and len(df1)==len(df), 'table XIV: rid filter is not set'

    df = citros.topic('A').sid(1).data(['data.x.x_2', 'data.time'], additional_columns = 'sid')
    assert 'sid' in df.columns, 'table XIV: wrong additional columns: sid is not quired'
    assert all([x not in df.columns for x in ['rid', 'time', 'topic', 'type']]), 'table XIV: wrong additional columns: columns should not be queried'
    assert all(df['sid']==1), 'table XIV: sid filter is not set'

def test_data_dict():
    #test_data_dict I
    dfs = citros.topic('A').\
                 set_filter({'sid':[1,2]}).\
                 set_order({'rid':'desc', 'time':'asc'}).\
                 avg(2).\
                 data_dict(['data.x.x_2', 'data.time'])
    assert all([x in dfs[1].columns for x in ['sid', 'rid', 'time', 'topic', 'type']]), 'test_data_dict I: wrong additional columns'
    assert abs(dfs[1]['data.x.x_2'].iloc[0] - (-0.076)) < 0.001, 'test_data_dict I: value is wrong'
    assert abs(dfs[1]['data.x.x_2'].iloc[3] - (-0.052)) < 0.001, 'test_data_dict I: value is wrong'

    #test_data_dict II
    dfs = citros.topic('A').\
                 data_dict(['data.x.x_2', 'data.time'], 
                           additional_columns = ['topic','time'])
    assert all([x in dfs[1].columns for x in['sid', 'time', 'topic']]), 'test_data_dict II: wrong additional columns: columns are not quired'
    assert all([x not in dfs[1].columns for x in ['rid', 'type']]), 'test_data_dict II: wrong additional columns: some of the columns should not be queried'

    #test_data_dict III
    dfs = citros.topic('A').\
                 data_dict(['data.x.x_2', 'data.time'], 
                           additional_columns = 'sid')
    assert 'sid' in dfs[1].columns, 'test_data_dict III: wrong additional columns: sid is not quired'
    assert all([x not in dfs[1].columns for x in ['rid', 'time', 'topic', 'type']]), 'test_data_dict III: wrong additional columns: columns should not be queried'

def test_get_batch_size():
    assert isinstance(citros._get_batch_sizes(), list), 'get_batch_size(): returning type is not list'

def test_get_data_structure():
    assert isinstance(citros._download_data_structure(out_format = 'str'), list), 'get_data_structure(): returning type is not list'
    assert citros._download_data_structure(filter_by = {'topic': ['C']}, out_format = 'str')[0][2] == \
        '{\n  p: float,\n  t: int,\n  x: {\n    x_1: float,\n    x_2: float,\n    x_3: float\n  },\n  y: {\n    y_1: float,\n    y_2: float,\n    y_3: float\n  },\n  note: list,\n  time: float,\n  height: float\n}',\
        'topic().get_data_structure(): data structure is wrong'
    assert citros._download_data_structure(filter_by = {'topic': ['B']}, out_format = 'str')[0][2] == \
        '{\n  p: float,\n  t: int,\n  x: {\n    x_1: float,\n    x_2: float,\n    x_3: float\n  },\n  y: {\n    y_1: int,\n    y_2: int,\n    y_3: float\n  },\n  note: list,\n  time: float,\n  height: float\n}',\
        'get_data_structure(topic): data structure is wrong'

def test_min_max():
    #min_max I
    column_name = 'data.height'
    filter_by = {'topic': ['A'], 'data.x.x_3': {'gt' : 25}}
    result = citros.get_min_value(column_name, filter_by)
    assert abs(result - (-13884.705)) < 0.001, 'min_max I: min value is wrong'

    result = citros.get_max_value(column_name, filter_by)
    assert abs(result - 949.799) < 0.001, 'min_max I: max value is wrong'

    #min_max II
    column_name = 'data.height'
    result = citros.topic('A').set_filter({'data.x.x_3': {'gt' : 25}}).get_min_value(column_name)
    assert abs(result - (-13884.705)) < 0.001, 'min_max II: min value is wrong'

    result = citros.topic('A').set_filter({'data.x.x_3': {'gt' : 25}}).get_max_value(column_name)
    assert abs(result - 949.799) < 0.001, 'min_max II: max value is wrong'

    #min_max III
    result = citros.topic('C').sid([1,3]).time(start = 5000000000, duration = 15000000000).rid(start = 4, end = 10).get_min_value('data.height')
    assert abs(result - 14.117)< 0.001, 'min_max III: min value is wrong'

    result = citros.topic('C').sid([1,3]).time(start = 5000000000, end = 20000000000).rid(start = 4, count = 6).get_max_value('data.height')
    assert abs(result - 248.129)< 0.001, 'min_max III: max value is wrong'

    #min_max IV
    assert abs(citros.set_filter({'data.y.y_1': {'lt': 1e308}}).get_max_value('data.y.y_1')-9.99)<0.01, 'min_max IV: max value is wrong'
    assert abs(citros.set_filter({'data.y.y_1': {'gt': -1e308}}).get_min_value('data.y.y_1') + 9.98)<0.01, 'min_max IV: min value is wrong'

    #min_max V index
    max_val, sid, rid = citros.get_max_value('time', return_index=True)
    assert (max_val == 100752013600) and (sid == 1) and (rid==177), 'min_max V index: max value is wrong'

    min_val, sid, rid  = citros.get_min_value('time', return_index=True)
    assert (min_val == 95738240) and (sid == 1) and (rid==0), 'min_max V index: min value is wrong'

    #min_max VI index
    max_val, sid, rid  = citros.get_max_value('data.x.x_3', return_index=True)
    assert (max_val == 219.91) and (sid == 3) and (rid==39), 'min_max VI index: max value is wrong'

    min_val, sid, rid  = citros.get_min_value('data.x.x_3', return_index=True)
    assert (min_val == -29.89) and (sid == 2) and (rid==75), 'min_max VI index: min value is wrong'

    #min_max VII index
    max_val, sid, rid = citros.get_max_value('data.x.x_1', return_index=True)
    assert (len(sid) == 12) and (max_val == 0.15), 'min_max VII index: max value is wrong'

    min_val, sid, rid = citros.get_min_value('data.x.x_1', return_index=True)
    assert (len(rid) == 12) and (min_val == -0.15), 'min_max VII index: min value is wrong'

def test_get_unique_values():
    #get_unique_values('topic')
    res = citros.get_unique_values('topic')
    answ = ['A', 'B', 'C', 'D']
    assert all([t in res for t in answ] + [len(res) == len(answ)]), 'get_unique_values("topic"): wrong result'

    #get_unique_values(['topic','type'])
    res = citros.get_unique_values(['topic','type'])
    answ = [('A', 'a'), ('B', 'b'), ('C', 'c'), ('D', 'd')]
    assert all([t in res for t in answ] + [len(res) == len(answ)]), 'get_unique_values(["topic","type"]): wrong result'

    #get_unique_values('type')
    assert citros.topic('A').get_unique_values('type') == ['a'], 'get_unique_values(type): wrong result'

    #get_unique_values(['topic','rid'])
    res = citros.topic('C').rid(start = 2, end = 5).get_unique_values(['topic','rid'])
    answ = [('C', 2), ('C', 3), ('C', 4), ('C', 5)]
    assert all([t in res for t in answ] + [len(res) == len(answ)]), 'get_unique_values(["topic","rid"]): wrong result'

    #get_unique_values('data.note[0]')
    res = citros.get_unique_values('data.note[0]')
    answ = ['aa', 'bb']
    assert  all([t in res for t in answ] + [len(res) == len(answ)]), 'get_unique_values("data.note[0]"): wrong result'

    #get_unique_values for column with nan, removing big values
    len(citros.set_filter({'data.y.y_1': {'gt': -1e308, 'lt': 1e308,}}).get_unique_values('data.y.y_1')) == 783, 'get_unique_values for column with nan, removing big values is wrong'

def test_get_counts():
    #get_counts('topic')
    assert citros.get_counts('topic')[0][0] == 2000, "get_counts('topic'): wrong result"

    #get_counts('topic', group_by='type')
    res = citros.get_counts('topic', group_by='type')
    answ = [('a', 474), ('b', 494), ('c', 513), ('d', 519)]
    assert  all([t in res for t in answ] + [len(res) == len(answ)]), "get_counts('topic', group_by='type'): wrong result"

    #get_counts('topic'), sid = 1
    assert citros.sid([1]).get_counts('topic')[0][0] == 688, "get_counts('topic'), sid = 1: wrong result"

    #get_counts('data.note[0]'), sid = 1
    assert citros.sid([1]).get_counts('data.note[0]')[0][0] == 688, "get_counts('data.note[0]'), sid = 1: wrong result"

    #get_counts('topic', group_by='type'), sid = 1
    res = citros.sid(1).get_counts('topic', group_by='type')
    answ = [('a', 155), ('b', 178), ('c', 175), ('d', 180)]
    assert  all([t in res for t in answ] + [len(res) == len(answ)]), "get_counts('topic', group_by='type'), sid = 1: wrong result"

    #get_counts for column with nan values, nan excluded
    citros.get_counts('data.y.y_1', nan_exclude = True)[0][0]==1482, "get_counts for column with nan values, nan excluded is wrong"

    #get_counts for column with nan values
    citros.get_counts('data.y.y_1')[0][0]==2000, "get_counts for column with nan values is wrong"

def test_get_unique_counts():
    #get_counts('topic')
    assert citros.get_unique_counts('topic')[0][0] == 4, "get_unique_counts('topic'): wrong result"

    #get_unique_counts('topic', group_by='type')
    res = citros.get_unique_counts('topic', group_by='type')
    answ = [('a', 1), ('b', 1), ('c', 1), ('d', 1)]
    assert  all([t in res for t in answ] + [len(res) == len(answ)]), "get_unique_counts('topic', group_by='type'): wrong result"

    #get_unique_counts('topic'), sid = 1
    assert citros.sid([1]).get_unique_counts('topic')[0][0] == 4, "get_unique_counts('topic'), sid = 1: wrong result"

    #get_unique_counts('data.note[0]'), sid = 1
    assert citros.sid([1]).get_unique_counts('data.note[0]')[0][0] == 2, "get_unique_counts('data.note[0]'), sid = 1: wrong result"

    #get_unique_counts('topic', group_by='type'), sid = 1
    res = citros.sid(1).get_unique_counts('topic', group_by='type')
    answ = [('a', 1), ('b', 1), ('c', 1), ('d', 1)]
    assert  all([t in res for t in answ] + [len(res) == len(answ)]), "get_unique_counts('topic', group_by='type'), sid = 1: wrong result"

    #get_unique_counts for column with nan, removing big values
    assert citros.set_filter({'data.y.y_1': {'gt': -1e308, 'lt': 1e308,}}).get_unique_counts('data.y.y_1')[0][0] == 783, "get_unique_counts for column with nan, removing big values is wrong"
    assert citros.set_filter({'data.y.y_1': {'>': -1e308, '<': 1e308,}}).get_unique_counts('data.y.y_1')[0][0] == 783, "get_unique_counts for column with nan, removing big values is wrong"

    #get_unique_values for column with nan, nan_exclude
    assert citros.topic(['A']).rid([1,2,3]).get_unique_counts('data.y.y_1')[0][0] == 5, "get_unique_counts, nan_exclude is wrong"

    #get_unique_values for column with nan, group_by, nan_exclude
    assert citros.topic(['A']).rid([1,2,3]).get_unique_counts('data.y.y_1', nan_exclude = True)[0][0] == 4, "get_unique_counts, group_by, nan_exclude, is wrong"

    #get_unique_values for *, group_by, nan_exclude
    assert ('A', 9) in citros.topic(['A','B']).rid([1,2,3]).get_unique_counts(group_by = 'topic', nan_exclude = True), "get_unique_counts, group_by, *, nan_exclude, is wrong"

    #get_unique_values for *, nan_exclude
    assert citros.topic(['A','B']).rid([1,2,3]).get_unique_counts(nan_exclude = True)[0][0] == 18, "get_unique_counts, *, nan_exclude, is wrong"

    #get_unique_values for *, group_by, nan_exclude
    assert ('A', 9) in citros.topic(['A','B']).rid([1,2,3]).get_unique_counts(group_by = 'topic'), "get_unique_counts, group_by, *, is wrong"

    #get_unique_values for *, nan_exclude
    assert citros.topic(['A','B']).rid([1,2,3]).get_unique_counts()[0][0] == 18, "get_unique_counts, *, is wrong"

def test_plot_graph():
    plt.close('all')
    fig, ax = plt.subplots()
    df = citros.topic('A').data()
    citros.plot_graph(df, 'data.time','data.x.x_1', '.', ax=ax)
    n_lines = len(ax.get_lines())
    assert n_lines == 3, 'plot_graph: number of lines is wrong'

def test_plot_graph_nan():
    plt.close('all')
    df = citros.topic('A').data()
    fig, ax = citros.plot_graph(df, 'data.y.y_2','data.y.y_1', '.', remove_nan = True, inf_vals = 1e308)
    n_lines = len(ax.get_lines())
    assert n_lines == 3, 'plot_graph_nan: number of lines is wrong'
    
def test_time_plot():
    plt.close('all')
    fig, ax = plt.subplots()
    citros.topic('B').time_plot(ax, var_name = 'data.x.x_1', time_step = 0.5)
    n_lines = len(ax.get_lines())
    assert n_lines == 3, 'time_plot_nan: number of lines is wrong'

def test_time_plot_nan():
    plt.close('all')
    fig, ax = plt.subplots()
    citros.topic('B').time_plot(ax, var_name = 'data.y.y_1', time_step = 0.5, remove_nan = True, inf_vals = 1e308)
    n_lines = len(ax.get_lines())
    assert n_lines == 3, 'time_plot_nan: number of lines is wrong'

def test_xy_plot():
    plt.close('all')
    fig, ax = plt.subplots()
    citros.topic('A').xy_plot(ax, var_x_name = 'data.time', var_y_name = 'data.height')
    n_lines = len(ax.get_lines())
    assert n_lines == 3, 'xy_plot_nan: number of lines is wrong'

def test_xy_plot_nan():
    plt.close('all')
    fig, ax = plt.subplots()
    citros.topic('A').xy_plot(ax, var_x_name = 'data.y.y_1', var_y_name = 'data.y.y_2', remove_nan = True, inf_vals = 1e308)
    n_lines = len(ax.get_lines())
    assert n_lines == 3, 'xy_plot_nan: number of lines is wrong'

def test_plot_3dgraph():
    plt.close('all')
    df = citros.topic('A')\
           .sid([1,2,3])\
           .data(['data.x.x_1', 'data.x.x_2', 'data.x.x_3'])
    fig = plt.figure(figsize=(6, 6))
    ax = fig.add_subplot(111, projection='3d')
    citros.plot_3dgraph(df, 'data.x.x_1', 'data.x.x_2', 'data.x.x_3', '-', ax = ax, scale = False, 
                        title = None, legend = False)
    
    n_lines = len(ax.get_lines())
    assert n_lines == 3, 'plot_3dgraph: number of lines is wrong'

def test_plot_3dgraph_nan():
    plt.close('all')
    df = citros.topic('A')\
           .sid([1,2,3])\
           .data(['data.y.y_1', 'data.y.y_2', 'data.y.y_3'])
    # ax = fig.add_subplot(111, projection='3d')
    fig, ax = citros.plot_3dgraph(df, 'data.y.y_1', 'data.y.y_2', 'data.y.y_3', '-', scale = True, 
                        title = None, legend = False, remove_nan = True, inf_vals = 1e308)
    n_lines = len(ax.get_lines())
    assert n_lines == 3, 'plot_3dgraph_nan: number of lines is wrong'
    
def test_multiple_y_plot():
    plt.close('all')
    df = citros.topic('A')\
           .data(['data.x.x_1', 'data.x.x_2', 'data.x.x_3', 'data.time'])
    fig = plt.figure(figsize=(6, 6))
    citros.multiple_y_plot(df, 'data.x.x_1', ['data.x.x_1', 'data.x.x_2', 'data.x.x_3'], '--', fig = fig,
                                     legend = False, title = None)
    for ax in fig.axes:
        n_lines = len(ax.get_lines())
        assert n_lines == 3, 'multiple_y_plot_nan: number of lines is wrong'

def test_multiple_y_plot_nan():
    plt.close('all')
    df = citros.topic('A')\
           .data(['data.y.y_1', 'data.y.y_2', 'data.y.y_3', 'data.time'])
    fig, axes = citros.multiple_y_plot(df, 'data.y.y_1', ['data.y.y_1', 'data.y.y_2', 'data.y.y_3'], '--',
                                     legend = False, title = None, remove_nan = True, inf_vals = 1e308)
    for ax in axes:
        n_lines = len(ax.get_lines())
        assert n_lines == 3, 'multiple_y_plot_nan: number of lines is wrong'

def test_multiplot():
    plt.close('all')
    df = citros.topic('A')\
           .data(['data.x.x_1', 'data.x.x_2', 'data.x.x_3', 'data.time'])
    fig = plt.figure(figsize=(6, 6))
    citros.multiplot(df, ['data.x.x_1','data.x.x_2','data.x.x_3'],'.',fig = fig, scale =False)
    n_lines = [0, 3, 3, 3, 0, 3, 3, 3, 0]
    n_patches = [3, 0, 0, 0, 3, 0, 0, 0, 3]
    for ax, n in zip(fig.axes, zip(n_lines, n_patches)):
        assert len(ax.get_lines()) == n[0], 'multiplot: number of lines is wrong'
        assert len(ax.patches) == n[1], 'multiplot: number of patches is wrong'

def test_multiplot_nan():
    plt.close('all')
    df = citros.topic('A')\
           .data(['data.y.y_1', 'data.y.y_2', 'data.y.y_3', 'data.time'])
    fig, axes = citros.multiplot(df, ['data.y.y_1','data.y.y_2','data.y.y_3'], 'o-', scale =False)
    n_lines = [0, 3, 3, 3, 0, 3, 3, 3, 0]
    n_patches = [3, 0, 0, 0, 3, 0, 0, 0, 3]
    for ax, n in zip(axes.flatten(), zip(n_lines, n_patches)):
        assert len(ax.get_lines()) == n[0], 'multiplot: number of lines is wrong'
        assert len(ax.patches) == n[1], 'multiplot: number of patches is wrong'

def test_plot_sigma_ellipse():
    plt.close('all')
    df = citros.topic('A').data(['data.y.y_1', 'data.y.y_2'])
    fig, ax = citros.plot_sigma_ellipse(df, x_label = 'data.y.y_1', y_label = 'data.y.y_2', n_std = [1,2,3], plot_origin=True, bounding_error=True,
                                    set_x_label='y_1, [m]', set_y_label = 'y_2, [m]', title = 'Coordinates')
    for ax in fig.axes:
        n_lines = len(ax.get_lines())
        n_patches = len(ax.patches)
    assert n_lines == 6, 'plot_sigma_ellipse: number of lines is wrong'
    assert n_patches == 3, 'plot_sigma_ellipse: number of patches is wrong'

    fig, ax, ellipse_param = citros.plot_sigma_ellipse(df, x_label = 'data.y.y_1', y_label = 'data.y.y_2', n_std = [1,2,3], plot_origin=True,
                                    set_x_label='y_1, [m]', set_y_label = 'y_2, [m]', title = 'Coordinates', return_ellipse_param=True)
    
    assert isinstance(ellipse_param, list), 'ellipse_param type is wrong'
    assert len(ellipse_param) == 3, 'ellipse_param length is wrong'
    assert all([k in ellipse_param[0].keys() for k in ['x', 'y', 'width', 'height', 'alpha']]), 'ellipse_param keys are wrong'
    fig, ax, ellipse_param = citros.plot_sigma_ellipse(df, x_label = 'data.y.y_1', y_label = 'data.y.y_2', n_std = 1, plot_origin=True, bounding_error=True,
                                    set_x_label='y_1, [m]', set_y_label = 'y_2, [m]', title = 'Coordinates', return_ellipse_param=True)
    
    assert all([k in ellipse_param.keys() for k in ['x', 'y', 'width', 'height', 'alpha', 'bounding_error']]), 'ellipse_param keys for one ellipse are wrong'
    
    answ = {'x': 0.320747663551402, 'y': 0.569532710280374, 'width': 11.50897818996438, 'height': 10.38635366297768, 'alpha': -12.309437674631502, 'bounding_error': 6.098441476968801}
    for k, v in ellipse_param.items():
        assert abs(answ[k] - v) < 0.01, f'value for ellipse_param key {k} is wrong'

    plt.close('all')
    