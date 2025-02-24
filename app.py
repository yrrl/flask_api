from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='postgresql://postgres:qwerty123@localhost/flask'
db=SQLAlchemy(app)


#@app.route('/', methods=['GET'])
#def index():
    #return render_template('index.html')


#TO IMPORT DB
class staff(db.Model):
    __tablename__ = 'staff'
    uid = db.Column(db.Integer, primary_key=True)
    fname = db.Column(db.String(255))
    lname = db.Column(db.String(255))
    age = db.Column(db.Integer)


@app.route('/')
def index():
    staffs = staff.query.all()
    return render_template('index.html', staffs = staffs)



if __name__ == '__main__':
    app.run(debug=True)