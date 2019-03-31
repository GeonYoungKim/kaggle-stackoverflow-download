import config
from kafka.producer import KafkaAvroProducer

read_count = 30000
thread_max_count = 3000000
kaggle_kafka_dict_list = []
for index in range(0, 24, 1):
    kaggle_kafka_dict_list.append(
        {"avro": config.COMMENTS_TOPIC_CONFIG['avro'], "topic": config.COMMENTS_TOPIC_CONFIG['topic'],
         "table": "comments", "read_count": read_count, "start":thread_max_count * index, "thread_trt_max_count": thread_max_count,
         "thread_number": index})


for kaggle_kafka_dict in kaggle_kafka_dict_list:
    thread = KafkaAvroProducer(kaggle_kafka_dict)
    thread.start()
