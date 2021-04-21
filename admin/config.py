import pymongo
import json

def load_key(key_file) :
    with open(key_file) as key_file :
        key = json.load(key_file)
        print(key)
    return key

FLASK_ADMIN_SWATCH = 'readable'

ADMIN_KEY = 'qekjqihbbjbjksknqnqklajdflkjsdivlkqjlkwjkljadslfkjibalksnf'
SECRET_KEY = 'data-center_secretkey'

db = load_key(key_file='./keys/aws_dc_sql_key.json')
database = "career-center"
MYSQL_URI = f"mysql+pymysql://{db['user']}:{db['password']}@localhost:{db['port']}/{database}?charset=utf8mb4"
SQLALCHEMY_ECHO = True
SQLALCHEMY_TRACK_MODIFICATIONS = False

mongo = load_key(key_file='./keys/aws_dc_mongo_key.json')
MONGO_CONN = pymongo.MongoClient(f"mongodb://{mongo['host']}:{mongo['port']}",
                                    username=mongo['user'],password=mongo['password'])

JOB_SECTOR = ['Back-end','Front-end','WEB/Full-stack','Android','IOS',
              'Mobile','Data-analyst','Data-engineer','Data-scientist',
              'Machine-learning','DevOps','Game','Embedded/Robotics',
              'Project-manager','Web-publisher','Security','Computer-vision',
              'Block-chain','Hardware','CTO','Unity/AR/VR/3D',
              'JAVA-dev','Anonymous','QA/QC','C#/C++/C','PHP-dev']