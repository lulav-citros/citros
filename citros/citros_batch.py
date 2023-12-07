import uuid
from pathlib import Path


class citros_batch():
    def __init__(self, citros):
        self.citros = citros      
        self.log = citros.log


    def generate_batch_id(self):
        # generate a random UUID
        return str(uuid.uuid4())
    
                        
    def get_batch(self, batch_run_id, simulation_name=None):
        batch = None

        if self.citros.CITROS_ENVIRONMENT != "CLUSTER":
            assert simulation_name is not None, \
                "Simulation name cannot be None while running locally."

            user_commit, user_branch = self.citros.get_git_info(self.citros.USER_PROJ_DIR)
            citros_commit, citros_branch = self.citros.get_git_info(self.citros.CITROS_REPO_DIR)

            sim_info = self.citros.get_simulation_info(simulation_name)

            batch = {
                'id' : str(self.citros._batch_id),
                'simulation': simulation_name,
                'message' : self.citros._batch_message,
                'name' : self.citros._batch_name,
                'citrosCommit' : citros_commit,
                'citrosBranch' : citros_branch,
                'userCommit' : user_commit,
                'userBranch' : user_branch,
                'cpu': sim_info['CPU'],             
                'gpu': sim_info['GPU'],
                'memory': sim_info['MEM'],
                'storageType': sim_info['storage_type'],
                'timeout': sim_info['timeout'],
                'metadata': None
            }
        else:
            query = """
            query getData($batchRunId: UUID!) {
            batchRun(id: $batchRunId) {
                    id
                    simulation                
                    message
                    name
                    citrosCommit
                    citrosBranch
                    userCommit
                    userBranch
                    cpu
                    gpu
                    memory
                    storageType,
                    timeout
                    metadata
                }
            }
            """
            batch = self.citros.gql_execute(query, variable_values={"batchRunId": batch_run_id})['batchRun']
        
        return batch       
    

    def create_batch(self, batch_id, repo_id, simulation_name, gpu, cpu, memory, storage_type, 
                     completions, user_commit, user_branch, citros_commit, citros_branch, latest_tag, timeout,
                     name="", message="", parallelism=1, metadata={}):
        query = """
        mutation createBatchRun($batch_run: CreateBatchRunInput!) {
            createBatchRun(input: $batch_run) {
            batchRun {
                id
            }
            }
        }
        """
        result = self.citros.gql_execute(query, variable_values={
            "batch_run": {
            "batchRun": {
                "id": batch_id, 
                "repoId": repo_id,
                "simulation": simulation_name,
                "gpu": gpu,
                "cpu": cpu,
                "memory": int(memory),
                "storageType": storage_type,
                "name": name,
                "message": message,
                "completions": int(completions),
                "parallelism": parallelism,
                "citrosBranch": citros_branch,
                "citrosCommit": citros_commit,
                "userBranch": user_branch,
                "userCommit": user_commit,
                "tag": latest_tag,
                "metadata": metadata,
                "timeout" : timeout
            }
            }
        })
           
        return result["createBatchRun"]["batchRun"]["id"]
   
   