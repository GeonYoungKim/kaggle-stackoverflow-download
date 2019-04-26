from support.bq_helper import BigQueryHelper

bigquery_client = BigQueryHelper(active_project="bigquery-public-data",
                                 dataset_name="stackoverflow")
TOTAL_COUNT_FIELD = 'total_count'
TABLE_ROW_INTERVAL = 3000000

def get_table_count(table):
    query = "SELECT count(1) as {} FROM {}".format(TOTAL_COUNT_FIELD, table)
    query_result_df = bigquery_client.query_to_pandas(query)
    return query_result_df.ix[0][TOTAL_COUNT_FIELD]

def get_max_index(table_count):
    return table_count // TABLE_ROW_INTERVAL +1
