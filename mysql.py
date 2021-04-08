from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship, backref
Base = declarative_base()

class JobSkill(Base) :
    __tablename__ = "jobskill"
    id  = Column(Integer, primary_key=True)
    name   = Column(String(200))

class JobSector(Base) :
    __tablename__ = "jobsector"
    id = Column(Integer, primary_key=True)
    name  = Column(String(200))

class Platform(Base) :
    __tablename__ = "platform"
    id = Column(Integer, primary_key=True)
    name  = Column(String(200))

class Click(Base) :
    __tablename__ = "click"
    id     = Column(Integer, primary_key=True)
    user_id = Column(String(32))
    recruit_id = Column(Integer)

class Bookmark(Base) :
    __tablename__ = "bookmark"
    id     = Column(Integer, primary_key=True)
    user_id = Column(String(32))
    recruit_id = Column(Integer)

class Recurit_apply(Base) :
    __tablename__ = "recurite_apply"
    id     = Column(Integer, primary_key=True)
    user_id = Column(String(32))
    recruit_id = Column(Integer)
    platform_id = Column(Integer,ForeignKey('platform.id'))
    platform = relationship("Platform", backref=backref("bookmark", order_by=id))

class Recurit_stack(Base) :
    __tablename__ = "recurite_stack"
    id     = Column(Integer, primary_key=True)
    recruit_id = Column(Integer)
    skill_id = Column(Integer,ForeignKey('jobskill.id'))
    skill = relationship("JobSkill", backref=backref("recurit_skill", order_by=id))

class Filtering(Base) :
    __tablename__ = "filtering"
    id     = Column(Integer, primary_key=True)
    user_id = Column(String(32))
    filtering = Column(String(100))

class Resume_sector(Base) :
    __tablename__ = "resume_sector"
    id     = Column(Integer, primary_key=True)
    user_id = Column(String(32))
    sector_id = Column(Integer,ForeignKey('jobsector.id'))
    sector = relationship("JobSector", backref=backref("resume_sector", order_by=id))

class Resume_skill(Base) :
    __tablename__ = "resume_skill"
    id     = Column(Integer, primary_key=True)
    user_id = Column(String(32))
    skill_id = Column(Integer,ForeignKey('jobskill.id'))
    skill = relationship("JobSkill", backref=backref("resume_skill", order_by=id))
