KAGGLE_CONFIG = {
    "dataset" : "stackoverflow",
    "project" : "bigquery-public-data",
    "tables" : {
        "comment": {
            "full_name" : '`bigquery-public-data.stackoverflow.comments`',
            "name" : "comments"
        },
        "answer" :{
            "full_name" :'`bigquery-public-data.stackoverflow.posts_answers`',
            "name" : "posts_answers"
        },
        "question" : {
            "full_name" : '`bigquery-public-data.stackoverflow.posts_questions`',
            "name" : "posts_questions"
        },
        "user" : {
            "full_name" : '`bigquery-public-data.stackoverflow.users`',
            "name" : "users"
        },
        "link" : {
            "full_name" : '`bigquery-public-data.stackoverflow.post_links`',
            "name" : "post_links"
        }
    }
}

FILE_CONFIG = {
    "file_path" : {
        # "comment" : "C:\\Users\\geonyeongkim\\Desktop\\data\\comment",
        # "answer" : "C:\\Users\\geonyeongkim\\Desktop\\data\\answer",
        # "question" : "C:\\Users\\geonyeongkim\\Desktop\\data\\question",
        # "link" : "C:\\Users\\geonyeongkim\\Desktop\\data\\link",
        # "user" : "C:\\Users\\geonyeongkim\\Desktop\\data\\user"
        "comment": "/home1/irteam/data/comment",
        "answer": "/home1/irteam/data/answer",
        "question": "/home1/irteam/data/question",
        "link": "/home1/irteam/data/link",
        "user": "/home1/irteam/data/user"
    }
}