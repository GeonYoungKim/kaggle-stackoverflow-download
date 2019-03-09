KAGGLE_CONFIG = {
    "dataset" : "stackoverflow",
    "project" : "bigquery-public-data"
}

KAFKA_CONFIG = {
    "bootstrap_servers" : "dev-geon-test001-ncl.nfra.io:9092,dev-geon-test002-ncl.nfra.io:9092,dev-geon-test003-ncl.nfra.io:9092,dev-geon-test004-ncl.nfra.io:9092,dev-geon-test005-ncl.nfra.io:9092",
    "schema_registry_url" : "http://dev-geon-test003-ncl.nfra.io:8081"
}

COMMENTS_TOPIC_CONFIG = {
    "topic" : "COMMENTS_RAW_DATA",
    "avro" : "kafka/schema/Comments.avsc"

}

USERS_TOPIC_CONFIG = {
    "topic" : "USERS_RAW_DATA",
    "avro" : "kafka/schema/Users.avsc"
}

POST_QUESTION_TOPIC_CONFIG = {
    "topic" : "POST_QUESTION_RAW_DATA",
    "avro" : "kafka/schema/PostsQuestions.avsc"
}

POST_ANSWER_TOPIC_CONFIG = {
    "topic" : "POST_ANSWER_RAW_DATA",
    "avro" : "kafka/schema/PostsAnswers.avsc"
}

POST_LINK_CONFIG = {
    "topic" : "POST_LINK_RAW_DATA",
    "avro" : "kafka/schema/PostLinks.avsc"
}