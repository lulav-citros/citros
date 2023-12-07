
import sys
import logging

from logging.handlers import TimedRotatingFileHandler


FORMATTER = logging.Formatter("[%(asctime)s] [%(name)s.%(funcName)s:%(lineno)d] [%(levelname)s]: %(message)s")

# log to console
def get_console_handler():
   console_handler = logging.StreamHandler(sys.stdout)
   console_handler.setFormatter(FORMATTER)
   return console_handler


# log to file
def get_file_handler(log_file):
   file_handler = TimedRotatingFileHandler(log_file, when='midnight')   
   file_handler.setFormatter(FORMATTER)
   return file_handler


def get_log_level(level : str):
   if level == 'debug':
      return logging.DEBUG
   elif level == 'info':
      return logging.INFO
   elif level == 'warn':
      return logging.WARNING
   elif level == 'error':
      return logging.ERROR
   else:
      # default to debug on invalid input
      return logging.DEBUG

   
Loggers = {}

def get_logger(logger_name, batch_run_id=None, simulation_run_id=None, 
               log_level='debug', log_file='.citros/logs/citros.log', on_cluster=False):
   
   logger_name = f"{logger_name}-{batch_run_id}-{simulation_run_id}"

   if Loggers.get(logger_name, None):   
      return Loggers[logger_name]
   
   logger = logging.getLogger(logger_name)
   logger.setLevel(get_log_level(log_level))

   file_handler = get_file_handler(log_file)
   logger.addHandler(file_handler)

   # write to console when debugging
   if log_level=='debug' or on_cluster:
      console_handler = get_console_handler()
      logger.addHandler(console_handler)

   Loggers[logger_name] = logger
   
   return Loggers[logger_name]


def shutdown():
   logging.shutdown()
