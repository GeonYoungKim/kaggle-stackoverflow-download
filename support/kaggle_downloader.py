import threading
from configuration.kaggle_configutaion import KAGGLE_CONFIG
from google.cloud import bigquery
import datetime
import json


class KaggleDownloader(threading.Thread):
    def __init__(self, KaggleTable, file_path):
        threading.Thread.__init__(self)
        self.client = bigquery.Client.from_service_account_json(
            '../resources/key_files/maptest-174316-deb1e644e273.json')
        self.read_count = 10000
        self.kaggle_table = KaggleTable
        self.file_path = file_path

    def run(self):
        print(self.kaggle_table.table)
        print(self.kaggle_table.start)

        tables_meta = self.client.dataset(KAGGLE_CONFIG['dataset'],
                                          project=KAGGLE_CONFIG['project'])
        tables = self.client.get_dataset(tables_meta)
        table = self.client.get_table(tables.table(self.kaggle_table.table))
        total_count = 0
        start_index = self.kaggle_table.start
        file = open("{}/{}".format(self.file_path, self.kaggle_table.start), 'w')
        try:
            while True:
                results = [dict(x) for x in
                           self.client.list_rows(table, start_index=start_index, max_results=self.read_count)]
                for result in results:
                    # 파일 출력
                    file.write('{}\t{}\t{}\n'.format(
                            str(result['id']),
                            str(result['post_id']),
                            str(result['related_post_id'])
                        )
                    )
                total_count += self.read_count
                start_index += self.read_count
                print('total_index => {}, start_index=> {}'.format(total_count, start_index))
                if len(results) < self.read_count or total_count >= self.kaggle_table.interval:
                    print('work end!!')
                    break
        finally:
            file.close()

def myconverter(o):
    if isinstance(o, datetime.datetime):
        return o.__str__()