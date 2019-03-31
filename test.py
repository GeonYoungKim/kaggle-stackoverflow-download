from google.cloud import bigquery
import config
from  bq_helper import BigQueryHelper

# client = bigquery.Client.from_service_account_json('./resources/key_files/maptest-174316-deb1e644e273.json')
# stackoverflow_tables_meta = client.dataset(config.KAGGLE_CONFIG['dataset'], project=config.KAGGLE_CONFIG['project'])
# stackoverflow_tables = client.get_dataset(stackoverflow_tables_meta)
# table = client.get_table(stackoverflow_tables.table("comments"))

# print(table.schema)

bq_assistant = BigQueryHelper(active_project= "bigquery-public-data",
                                       dataset_name = "stackoverflow")

QUERY = "SELECT count(1) FROM `bigquery-public-data.stackoverflow.comments`"
print(bq_assistant.query_to_pandas(QUERY))