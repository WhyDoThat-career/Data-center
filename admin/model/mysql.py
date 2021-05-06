from admin import db
import uuid
from sqlalchemy_utils import EmailType, UUIDType, URLType, IPAddressType

class User(db.Model) :
    id          = db.Column(UUIDType(binary=False), default=uuid.uuid4, primary_key=True)
    password    = db.Column(db.String(128))
    auth           = db.Column(db.String(100))
    email          = db.Column(EmailType, unique=True, nullable=False)
    nickname       = db.Column(db.String(100), nullable=False)
    @property
    def is_authenticated(self):
        return True
    @property
    def is_admin(self) :
        if self.auth == u'admin' :
            return True
        else :
            return False
    @property
    def is_active(self):
        return True

    @property
    def is_anonymous(self):
        return False

    def get_id(self):
        return self.id

    # Required for administrative interface
    def __unicode__(self):
        return self.username

class JobSkill(db.Model) :
    __tablename__ = "jobskill"
    id  = db.Column(db.Integer, primary_key=True)
    name   = db.Column(db.String(200))

class JobSector(db.Model) :
    __tablename__ = "jobsector"
    id = db.Column(db.Integer, primary_key=True)
    name  = db.Column(db.String(200))

class Platform(db.Model) :
    __tablename__ = "platform"
    id = db.Column(db.Integer, primary_key=True)
    name  = db.Column(db.String(200))

class Click(db.Model) :
    __tablename__ = "click"
    id     = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.String(32))
    recruit_id = db.Column(db.Integer)
    datetime = db.Column(db.DateTime)

class Bookmark(db.Model) :
    __tablename__ = "bookmark"
    id     = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.String(32))
    recruit_id = db.Column(db.Integer)
    datetime = db.Column(db.DateTime)

class Recurit_apply(db.Model) :
    __tablename__ = "recurite_apply"
    id     = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.String(32))
    recruit_id = db.Column(db.Integer)
    datetime = db.Column(db.DateTime)

class Recurit_stack(db.Model) :
    __tablename__ = "recurite_stack"
    id     = db.Column(db.Integer, primary_key=True)
    recruit_id = db.Column(db.Integer)
    skill_id = db.Column(db.Integer,db.ForeignKey('jobskill.id'))
    skill = db.relationship("JobSkill", backref=db.backref("recurit_skill", order_by=id))

class Filtering(db.Model) :
    __tablename__ = "filtering"
    id     = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.String(32))
    filtering = db.Column(db.String(100))
    datetime = db.Column(db.DateTime)

class Resume_sector(db.Model) :
    __tablename__ = "resume_sector"
    id     = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.String(32))
    sector_id = db.Column(db.Integer,db.ForeignKey('jobsector.id'))
    sector = db.relationship("JobSector", backref=db.backref("resume_sector", order_by=id))
    datetime = db.Column(db.DateTime)

class Resume_skill(db.Model) :
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