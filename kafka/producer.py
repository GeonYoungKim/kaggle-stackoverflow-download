import threading
import config
from google.cloud import bigquery
from confluent_kafka import avro
from confluent_kafka.avro import AvroProducer

class KafkaAvroProducer(threading.Thread):
    def __init__(self, dict):
        threading.Thread.__init__(self)
        self.client = bigquery.Client.from_service_account_json('./resources/key_files/maptest-174316-deb1e644e273.json')
        self.avro = dict['avro']
        self.topic = dict['topic']
        self.table = dict['table']
        self.read_count = dict['read_count']
        self.start_index = dict['start']

    def run(self):
        print("topic => " + self.topic)
        print("table => " + self.table)
        print("avro => " + self.avro)
        print("read_count => " + str(self.read_count))

        record_schema = avro.load(self.avro)
        avroProducer = AvroProducer(
            {
                'bootstrap.servers': config.KAFKA_CONFIG['bootstrap_servers'],
                'schema.registry.url': config.KAFKA_CONFIG['schema_registry_url']
            },
            default_value_schema = record_schema,
            default_key_schema = record_schema
        )
        stackoverflow_tables_meta = self.client.dataset(config.KAGGLE_CONFIG['dataset'], project=config.KAGGLE_CONFIG['project'])
        stackoverflow_tables = self.client.get_dataset(stackoverflow_tables_meta)
        table = self.client.get_table(stackoverflow_tables.table(self.table))
        table_schema_dict = {}
        for schema in table.schema:
            table_schema_dict[schema._name] = schema._field_type
        start_index = self.start_index
        while True:
            # kaggle data select
            results = [dict(x) for x in self.client.list_rows(table, start_index=start_index, max_results=self.read_count)]
            # send kaggle data to kafka
            for result in results:
                for key, value in result.items():
                    if value != None and table_schema_dict[key] == 'TIMESTAMP':
                        result[key] = result[key].now().strftime("%Y-%m-%d %H:%M:%S")
                    if value == None and table_schema_dict[key] in ['STRING', 'TIMESTAMP']:
                        result[key] = ''
                    if value == None and table_schema_dict[key] in ['INTEGER', 'FLOAT']:
                        result[key] = 0
                # avroProducer.produce(topic=self.topic, value=result, key=result, value_schema=record_schema, key_schema=record_schema)

            # avroProducer.flush()
            start_index += self.read_count
            print('{0} => {1}'.format(self.topic, start_index))
            if len(results) < self.read_count:
                break