from configuration.kaggle_configutaion import KAGGLE_CONFIG, FILE_CONFIG
from support.kaggle_downloader import KaggleDownloader
from model.kaggle_table import KaggleTable
from utils import kaggle_data_reader_util

CONFIG_ANSWER_KEY = 'comment'
CONFIG_TABLES_KEY = 'tables'

comment_count = kaggle_data_reader_util.get_table_count(KAGGLE_CONFIG[CONFIG_TABLES_KEY][CONFIG_ANSWER_KEY]['full_name'])

comment_max_index = kaggle_data_reader_util.get_max_index(comment_count)
downloader_list = []
print('comment_max_index => {}'.format(comment_max_index))

for index in range(0, comment_max_index):
    downloader_list.append(
        KaggleDownloader(
            KaggleTable(
                KAGGLE_CONFIG[CONFIG_TABLES_KEY][CONFIG_ANSWER_KEY]['name'],
                (index * kaggle_data_reader_util.TABLE_ROW_INTERVAL),
                kaggle_data_reader_util.TABLE_ROW_INTERVAL
            ),
            FILE_CONFIG['file_path'][CONFIG_ANSWER_KEY]
        )
    )

for downloader in downloader_list:
    downloader.start()
