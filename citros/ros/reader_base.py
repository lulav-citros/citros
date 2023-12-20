from .reader_mcap import BagReaderMcap
from .reader_sqlite import BagReaderSQL

class BagReader():
    def read_messages(self, input_bag, simulation_run_id):
        '''        
        return: 
            StringIO
        '''
        postfix = input_bag.split('.')[-1]
        
        br = None
        if (postfix == 'mcap'):
            br = BagReaderMcap()            
        elif( postfix == 'db3'):
            br = BagReaderSQL()            
        else:
            raise NotImplementedError

        return br.read_messages(input_bag, simulation_run_id)
        