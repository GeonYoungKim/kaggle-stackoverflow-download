from kafka.producer import KafkaAvroProducer
import config

read_count = 20000
thread_max_count = 1000000
kaggle_kafka_dict_list = []
for index in range(0, 6, 1):
    kaggle_kafka_dict_list.append(
        {"avro": config.POST_LINK_CONFIG['avro'], "topic": config.POST_LINK_CONFIG['topic'], "table": "post_links",
         "read_count": read_count, "start": thread_max_count * index, "thread_trt_max_count": thread_max_count,
         "thread_number": index})

for kaggle_kafka_dict in kaggle_kafka_dict_list:
    thread = KafkaAvroProducer(kaggle_kafka_dict)
    thread.start()
