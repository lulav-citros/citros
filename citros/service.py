import os
import uvicorn
import logging
from citros import get_logger, shutdown_log
from pathlib import Path
from fastapi import Depends, FastAPI, HTTPException, BackgroundTasks
from citros.batch import Batch, NoBatchFoundException
from fastapi_utils.timing import add_timing_middleware, record_timing

app = FastAPI()


class NoDataFoundException(Exception):
    def __init__(self, message="No Data found."):
        super().__init__(message)


# get batch info
@app.get("/{simulation}/{batch_name}")
async def get_batch(simulation, batch_name):
    try:
        batch = Batch(
            app.root,
            simulation,
            batch_name,
            log=app.log,
            debug=app.debug,
            verbose=app.verbose,
        )
        return batch.data
    except NoBatchFoundException:
        raise HTTPException(status_code=404, detail="Item not found")


def load_batch_run(simulation: str, batch_name: str, message=""):
    # TODO[critical] work that will load the data to DB
    pass


# request access to batch, loads the batch simulations to DB
@app.post("/{simulation}/{batch_name}")
async def request_access_batch(
    simulation: str, batch_name: str, background_tasks: BackgroundTasks
):
    background_tasks.add_task(
        load_batch_run, simulation, batch_name, message="some notification"
    )
    return {"message": "Batch run {simulation}/{batch_name} is loading. please wait"}


def data_access_service(
    root, time=False, host="localhost", port=8080, debug=False, verbose=False
):
    app.root = root
    if not root:
        raise ValueError("root path is required")
    if not Path(root).exists():
        raise NoDataFoundException(f"root path {root} does not exists")
    app.debug = debug
    app.verbose = verbose
    app.log = get_logger(
        __name__,
        log_level=os.environ.get("LOGLEVEL", "DEBUG" if debug else "INFO"),
        log_file=str(Path(root) / "citros.log"),
        verbose=verbose,
    )

    loglevel = logging._nameToLevel["ERROR"]
    # if debug:
    #     loglevel = logging._nameToLevel["DEBUG"]
    # logging.basicConfig(level=logging.DEBUG)
    if verbose:
        loglevel = logging._nameToLevel["INFO"]
        # logging.basicConfig(level=logging.INFO)
    # logging.basicConfig(level=logging.ERROR)  # second call do nothing...

    if time:
        logger = logging.getLogger("citros.data_access")
        add_timing_middleware(app, record=logger.info, prefix="app", exclude="untimed")

    from fastapi.logger import logger as fastapi_logger

    # app.log.
    uvicorn.run(app, host=host, port=int(port), log_level=loglevel)
