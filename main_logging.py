import logging
import time
from datetime import datetime

from read_json import read_json
from test_logging1 import show_index_0

time_str = time.strftime("%Y%m%d_%H%M%S")

logging.basicConfig(filename=datetime.now().strftime('output_log_%H%M%S_%Y%m%d.log'),
                    encoding='utf-8',
                    level=logging.INFO,
                    filemode='w',
                    format='%(asctime)s %(message)s')


list_vertex = read_json('sample.json')
logging.info(list_vertex)

first_vertex = show_index_0(list_vertex)
logging.info(first_vertex)
