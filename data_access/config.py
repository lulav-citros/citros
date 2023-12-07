import os
from dotenv import load_dotenv

load_dotenv()

# the directory where `citros run` records all data to
ROOT_DIR=os.getenv("ROOT_DIR", os.path.join(os.getcwd(), 'tmp'))
# print("ROOT_DIR", ROOT_DIR)