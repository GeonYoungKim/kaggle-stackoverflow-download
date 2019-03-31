from kafka.producer import KafkaAvroProducer
import config

read_count = 20000
thread_max_count = 1000000
kaggle_kafka_dict_list = []
for index in range(0, 18, 1):
    kaggle_kafka_dict_list.append(
        {"avro": config.POST_QUESTION_TOPIC_CONFIG['avro'], "topic": config.POST_QUESTION_TOPIC_CONFIG['topic'],
         "table": "posts_questions", "read_count": read_count, "start": thread_max_count * index,
         "thread_trt_max_count": thread_max_count, "thread_number": index})

for kaggle_kafka_dict in kaggle_kafka_dict_list:
    thread = KafkaAvroProducer(kaggle_kafka_dict)
    thread.start()
