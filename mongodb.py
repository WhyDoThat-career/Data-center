from engine import MONGO_CONN

class ResumeMongo :
    mongodb = MONGO_CONN

    @classmethod
    def conn_mongodb(cls,db_name) :
        try:
            cls.mongodb.admin.command('ismaster')
            resume_db = cls.mongodb.resume_db[f'{db_name}']
        except :
            cls.mongodb = MONGO_CONN
            resume_db = cls.mongodb.resume_db[f'{db_name}']
        return resume_db