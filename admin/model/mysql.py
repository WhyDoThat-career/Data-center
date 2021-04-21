from admin import db
import uuid
from sqlalchemy_utils import EmailType, UUIDType, URLType, IPAddressType

class User(db.Model) :
    id          = db.Column(UUIDType(binary=False), default=uuid.uuid4, primary_key=True)
    password    = db.Column(db.String(128))
    auth           = db.Column(db.String(100))
    email          = db.Column(EmailType, unique=True, nullable=False)
    nickname       = db.Column(db.String(100), nullable=False)
    resume    = db.relationship('Resume')

class JobSkill(Base) :
    __tablename__ = "jobskill"
    id  = db.Column(db.Integer, primary_key=True)
    name   = db.Column(db.String(200))

class JobSector(Base) :
    __tablename__ = "jobsector"
    id = db.Column(db.Integer, primary_key=True)
    name  = db.Column(db.String(200))

class Platform(Base) :
    __tablename__ = "platform"
    id = db.Column(db.Integer, primary_key=True)
    name  = db.Column(db.String(200))

class Click(Base) :
    __tablename__ = "click"
    id     = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.String(32))
    recruit_id = db.Column(db.Integer)
    datetime = db.Column(db.DateTime)

class Bookmark(Base) :
    __tablename__ = "bookmark"
    id     = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.String(32))
    recruit_id = db.Column(db.Integer)
    datetime = db.Column(db.DateTime)

class Recurit_apply(Base) :
    __tablename__ = "recurite_apply"
    id     = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.String(32))
    recruit_id = db.Column(db.Integer)
    platform_id = db.Column(db.Integer,db.ForeignKey('platform.id'))
    platform = db.relationship("Platform", backref=db.backref("bookmark", order_by=id))
    datetime = db.Column(db.DateTime)

class Recurit_stack(Base) :
    __tablename__ = "recurite_stack"
    id     = db.Column(db.Integer, primary_key=True)
    recruit_id = db.Column(db.Integer)
    skill_id = db.Column(db.Integer,db.ForeignKey('jobskill.id'))
    skill = db.relationship("JobSkill", backref=db.backref("recurit_skill", order_by=id))

class Filtering(Base) :
    __tablename__ = "filtering"
    id     = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.String(32))
    filtering = db.Column(db.String(100))
    datetime = db.Column(db.DateTime)

class Resume_sector(Base) :
    __tablename__ = "resume_sector"
    id     = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.String(32))
    sector_id = db.Column(db.Integer,db.ForeignKey('jobsector.id'))
    sector = db.relationship("JobSector", backref=db.backref("resume_sector", order_by=id))
    datetime = db.Column(db.DateTime)

class Resume_skill(Base) :
    __tablename__ = "resume_skill"
    id     = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.String(32))
    skill_id = db.Column(db.Integer,db.ForeignKey('jobskill.id'))
    skill = db.relationship("JobSkill", backref=db.backref("resume_skill", order_by=id))
    datetime = db.Column(db.DateTime)

class RegacyJobDetail(db.Model) :
    __tablename__ = "regacy_job_detail"
    id     = db.Column(db.Integer, primary_key=True)
    title     = db.Column(db.String(500))
    href      = db.Column(URLType)
    main_text = db.Column(db.Text)
    salary    = db.Column(db.String(50))
    skill_tag = db.Column(db.String(500))
    sector    = db.Column(db.String(200))
    newbie    = db.Column(db.Boolean)
    career    = db.Column(db.String(50))
    deadline  = db.Column(db.Date)
    company_name    = db.Column(db.String(100))
    company_address = db.Column(db.String(500))
    logo_image      = db.Column(db.String(500))
    big_company    = db.Column(db.Boolean)
    platform        = db.Column(db.String(100))
    crawl_date      = db.Column(db.DateTime)