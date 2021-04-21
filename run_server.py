from admin import app, db
from admin.model.mysql import User
from werkzeug.security import generate_password_hash, check_password_hash

def registerAdmin():
    if db.session.query(User).filter_by(email='admin@admin').first() is None :
        user = User()

        user.auth = u'admin'
        user.email = 'admin@admin'
        user.nickname = 'admin'
        user.password = generate_password_hash('dc210309')

        db.session.add(user) 
        db.session.commit()
        print('Create Admin account')
        return ""
    else :
        print('Already Exist Admin account')
        return ""

db.create_all()
registerAdmin()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='8888',debug=True)