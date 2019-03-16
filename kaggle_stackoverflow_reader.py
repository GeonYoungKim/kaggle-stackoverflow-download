from kafka.producer import KafkaAvroProducer
import config

if __name__ == "__main__":
    # 1. kaggle dataset select 2. kafka send(raw data using confluent avro schema registry)
    # 1. 캐글 데이터 셋 조회 2. 원본 데이터 카프카로 전송(confluent avro schema registry 사용.)
    read_count = 1000
    kaggle_kafka_dict_list = [
        {"avro": config.COMMENTS_TOPIC_CONFIG['avro'], "topic": config.COMMENTS_TOPIC_CONFIG['topic'], "table": "comments", "read_count": read_count},
        {"avro": config.USERS_TOPIC_CONFIG['avro'], "topic": config.USERS_TOPIC_CONFIG['topic'], "table": "users", "read_count": read_count},
        {"avro": config.POST_QUESTION_TOPIC_CONFIG['avro'], "topic": config.POST_QUESTION_TOPIC_CONFIG['topic'], "table": "posts_questions","read_count": read_count},
        {"avro": config.POST_ANSWER_TOPIC_CONFIG['avro'], "topic": config.POST_ANSWER_TOPIC_CONFIG['topic'], "table": "posts_answers", "read_count": read_count},
        {"avro": config.POST_LINK_CONFIG['avro'], "topic": config.POST_LINK_CONFIG['topic'], "table": "post_links", "read_count": read_count}
    ]

    for kaggle_kafka_dict in kaggle_kafka_dict_list:
        thread = KafkaAvroProducer(kaggle_kafka_dict)
        thread.start()