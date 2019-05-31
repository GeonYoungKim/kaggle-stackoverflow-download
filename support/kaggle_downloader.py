import threading
from configuration.kaggle_configutaion import KAGGLE_CONFIG
from google.cloud import bigquery
import datetime
import base64

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
        file = open("{}/{}".format(self.file_path, self.kaggle_table.start), 'w', encoding='UTF8')
        try:
            while True:
                results = [dict(x) for x in
                           self.client.list_rows(table, start_index=start_index, max_results=self.read_count)]
                for result in results:
                    # 파일 출력
                    file.write(writeStr(self.kaggle_table.table, result))
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


def pre_processing(source):
    return base64.b64encode(source.encode('utf-8'))

def writeStr(table, obj):
    if table == 'comments':
        return '{}`{}`{}`{}`{}`{}`{}\n'.format(
            str(obj['id']),
            pre_processing(str(obj['text'])),
            str(obj['creation_date']),
            str(obj['post_id']),
            str(obj['user_id']),
            str(obj['user_display_name']),
            str(obj['score'])
        )
    elif table == 'posts_answers':
        return '{}`{}`{}`{}`{}`{}`{}`{}`{}\n'.format(
            str(obj['id']),
            pre_processing(str(obj['body'])),
            str(obj['comment_count']),
            str(obj['creation_date']),
            str(obj['owner_display_name']),
            str(obj['owner_user_id']),
            str(obj['parent_id']),
            str(obj['score']),
            str(obj['tags']).replace('|', ',')
        )
    elif table == 'posts_questions':
        return '{}`{}`{}`{}`{}`{}`{}`{}`{}`{}`{}`{}\n'.format(
            str(obj['id']),
            pre_processing(str(obj['title'])),
            pre_processing(str(obj['body'])),
            str(obj['answer_count']),
            str(obj['comment_count']),
            str(obj['creation_date']),
            str(obj['favorite_count']),
            str(obj['owner_display_name']),
            str(obj['owner_user_id']),
            str(obj['score']),
            str(obj['tags']).replace('|', ','),
            str(obj['view_count'])
        )
    elif table == 'users':
        return '{}`{}`{}`{}`{}`{}`{}`{}`{}\n'.format(
            str(obj['id']),
            pre_processing(obj['display_name']),
            pre_processing(obj['about_me']),
            str(obj['age']),
            str(obj['creation_date']),
            str(obj['up_votes']),
            str(obj['down_votes']),
            str(obj['profile_image_url']),
            str(obj['website_url'])
        )
    elif table == 'post_links':
        return '{}`{}`{}\n'.format(
            str(obj['id']),
            str(obj['post_id']),
            str(obj['related_post_id'])
        )
