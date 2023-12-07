
from fastapi import Depends, FastAPI, HTTPException, BackgroundTasks
from fastapi_utils.timing import add_timing_middleware, record_timing
import logging
from citros.batch import Batch, NoBatchFoundException
from .config import config
import uvicorn

app = FastAPI()

# get batch info 
@app.get('/{simulation}/{batch_name}')
async def get_batch(simulation, batch_name):    
    try:
        batch = Batch(config.ROOT_DIR, simulation, batch_name)
        return batch.data    
    except NoBatchFoundException:
        raise HTTPException(status_code=404, detail="Item not found")            

def load_batch_run(simulation: str,batch_name: str, message=""):
    # TODO[critical] call to hot reload
    pass

# request access to batch, loads the batch simulations to DB
@app.post('/{simulation}/{batch_name}')
async def request_access_batch(simulation: str, batch_name: str, background_tasks: BackgroundTasks):    
    background_tasks.add_task(load_batch_run, simulation, batch_name, message="some notification")
    return {"message": "Batch run {simulation}/{batch_name} is loading. please wait"}

def main(args, argv):
    """_summary_
    
    :param args.debug:
	:param args.verbose:
    :param args.time:
    :param args.host:
    :param args.port:
    """
    # print("data args, argv", args, argv, args.debug, args.verbose)
    
    loglevel = logging._nameToLevel['ERROR']
    if args.debug:   
        loglevel = logging._nameToLevel['DEBUG']   
        logging.basicConfig(level=logging.DEBUG)
    if args.verbose:  
        loglevel = logging._nameToLevel['INFO']   
        logging.basicConfig(level=logging.INFO)    
    logging.basicConfig(level=logging.ERROR) # second call do nothing... 
         
    if args.time:
        logger = logging.getLogger('citros.data_access')
        add_timing_middleware(app, record=logger.debug, prefix="app", exclude="untimed")
    
    logging.getLogger("uvicorn.error").setLevel(level=loglevel)
    uvicorn.run(app, host=args.host, port=int(args.port), log_level=loglevel)
    
if __name__ == "__main__":
    main()
