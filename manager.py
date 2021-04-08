from engine import sql,JOB_SECTOR
from sqlalchemy.orm import sessionmaker
import mysql
from mysql import Base, JobSector
import os
import argparse

#migration 폴더 env.py 에 다음줄을 추가해야 migration 동작
# import sys
# sys.path.append('..')
# from manager import target_metadata

target_metadata = Base.metadata
parser = argparse.ArgumentParser(description='Manager 동작을 나타냅니다')
parser.add_argument('--manage','-m', type=str, 
                    help='''매니저 명령을 입력해주세요. 
                    ex)--manage create
                       -m migrate ''')
args = parser.parse_args()

Session = sessionmaker(bind=sql)

if args.manage is None :
	raise Exception('You must input parse. input [-h] tag help you')

if args.manage == 'create' :
    session = Session()
    target_metadata.create_all(sql)
    if session.query(JobSector).all() == [] :
        for sector_name in JOB_SECTOR:
            sector = JobSector()
            sector.name = sector_name
            session.add(sector)
        session.commit()

elif args.manage == 'migrate' :
    os.system('alembic revision --autogenerate')
