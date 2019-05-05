from configuration.kaggle_configutaion import KAGGLE_CONFIG, FILE_CONFIG
from support.kaggle_downloader import KaggleDownloader
from model.kaggle_table import KaggleTable
from utils import kaggle_data_reader_util
import sys
sys.path.insert(0, "/home1/irteam/deploy/kaggle-stackoverflow-download")

CONFIG_QEUSTION_KEY = 'question'
CONFIG_TABLES_KEY = 'tables'

question_count = kaggle_data_reader_util.get_table_count(KAGGLE_CONFIG[CONFIG_TABLES_KEY][CONFIG_QEUSTION_KEY]['full_name'])

question_max_index = kaggle_data_reader_util.get_max_index(question_count)
downloader_list = []

for index in range(0, question_max_index):
    downloader_list.append(
        KaggleDownloader(
            KaggleTable(
                KAGGLE_CONFIG[CONFIG_TABLES_KEY][CONFIG_QEUSTION_KEY]['name'],
                (index * kaggle_data_reader_util.TABLE_ROW_INTERVAL),
                kaggle_data_reader_util.TABLE_ROW_INTERVAL
            ),
            FILE_CONFIG['file_path'][CONFIG_QEUSTION_KEY]
        )
    )

for downloader in downloader_list:
    downloader.start()
