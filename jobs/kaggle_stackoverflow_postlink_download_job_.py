import os
import sys
from configuration.kaggle_configutaion import KAGGLE_CONFIG, FILE_CONFIG
from support.kaggle_downloader import KaggleDownloader
from model.kaggle_table import KaggleTable
from utils import kaggle_data_reader_util

root_path = os.path.abspath(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
sys.path.insert(0, root_path)

CONFIG_LINK_KEY = 'link'
CONFIG_TABLES_KEY = 'tables'

link_count = kaggle_data_reader_util.get_table_count(KAGGLE_CONFIG[CONFIG_TABLES_KEY][CONFIG_LINK_KEY]['full_name'])

link_max_index = kaggle_data_reader_util.get_max_index(link_count)
downloader_list = []

for index in range(0, link_max_index):
    downloader_list.append(
        KaggleDownloader(
            KaggleTable(
                KAGGLE_CONFIG[CONFIG_TABLES_KEY][CONFIG_LINK_KEY]['name'],
                (index * kaggle_data_reader_util.TABLE_ROW_INTERVAL),
                kaggle_data_reader_util.TABLE_ROW_INTERVAL
            ),
            FILE_CONFIG['file_path'][CONFIG_LINK_KEY]
        )
    )

for downloader in downloader_list:
    downloader.start()