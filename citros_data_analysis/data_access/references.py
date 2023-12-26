from ._gql_base import _GqlBase
from datetime import datetime
from urllib.parse import quote

class Ref(_GqlBase):
    '''
    Stores references to the batches used in the work
    '''
    _references = []

    def __init__(self):
        super().__init__()

    def print(self):
        '''
        Print the information about all batches that were used.

        Displays the batch creator's first and last name and email, batch name, message and creation time, link to the batch.
        The output is sorted by the last names.

        Examples
        --------
        Display references to the batches that were used in the current notebook:

        >>> from citros_data_analysis import data_access as da
        >>> ref = da.Ref()
        >>> ref.print()
        stevenson mary, mary@mail.com
        robotics, 'robotics system', 2023-06-01 09:00:00
        https://citros.io/robot_master/batch/00000000-aaaa-1111-2222-333333333333/
        '''
        print('REFERENCES:\n')
        ref_batch_id = list(set(self._references))
        if len(ref_batch_id) != 0:
            str_list = []
            for ref_id in ref_batch_id:
                ref_info = self._get_reference(ref_id)['batchRunsList']
                for ref in ref_info:
                    firstName = ref['user']['firstName']
                    lastname = ref['user']['lastName']
                    email = ref['user']['email']
                    message = ref['message']
                    repo_name = quote(ref['repo']['name'], safe='')
                    batch_name = ref['name']
                    batch_id = ref['id']
                    try:
                        createdAt = datetime.fromisoformat(ref['createdAt']).strftime('%Y-%m-%d %H:%M:%S')
                    except ValueError:
                        date_str = ref['createdAt']
                        if '+' in date_str:
                            timezone = date_str.split('+')[-1]
                            date_str = date_str.split('+')[0]+'0'+'+'+timezone
                        else:
                            timezone = date_str.split('-')[-1]
                            date_str = '-'.join(date_str.split('-')[0:-1])+'0'+'-'+timezone
                        createdAt = datetime.fromisoformat(date_str).strftime('%Y-%m-%d %H:%M:%S')
                    str_list.append(f"{lastname} {firstName}, {email}\n{batch_name}, '{message}', {createdAt}\nhttps://citros.io/{repo_name}/batch/{batch_id}/\n")
            str_list.sort()

            for str_item in str_list:
                print(str_item)
        else:
            print('')

    def _get_reference(self, batch_id):
        '''
        '''
        query = """query MyQuery($batch_id: UUID!) {
                  batchRunsList(condition: {id: $batch_id}) {
                    id
                    name
                    createdAt
                    message
                    user {
                      firstName
                      lastName
                      email
                    }
                    repo {
                      name
                    }
                  }
                }
                """
        variable_values = {'batch_id': batch_id}
        return self._gql_execute(query, variable_values = variable_values)