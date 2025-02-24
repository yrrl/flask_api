from flask import Flask, render_template,url_for,redirect, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='postgresql://postgres:qwerty123@localhost/flask'
db=SQLAlchemy(app)


#@app.route('/', methods=['GET'])
#def index():
    #return render_template('index.html')


#TO IMPORT DB
class Staff(db.Model):
    __tablename__ = 'staff'
    uid = db.Column(db.Integer, primary_key=True)
    fname = db.Column(db.String(255))
    lname = db.Column(db.String(255))
    age = db.Column(db.Integer)

#get all staff
@app.route('/api/staff',methods=['GET'])
def get_all_staff():
    staffs = Staff.query.all()
    return jsonify([{"uid":s.uid,"fname":s.fname,"lname":s.lname,"age":s.age}for s in staffs])

#view all information
@app.route('/')
def index():
    staffs = Staff.query.all()
    return render_template('index.html', staffs = staffs)

#insert a new staff
@app.route('/api/staff', methods=['POST'])
def create_staff():
    data = request.json  # Ensure JSON data is received
    if not data:
        return jsonify({"error": "Invalid input"}), 400
    
    new_staff = Staff(fname=data['fname'], lname=data['lname'], age=data['age'])
    db.session.add(new_staff)
    db.session.commit()
    
    return jsonify({"message": "Staff added successfully"}), 201



#delete a staff
@app.route("/api/staff/<int:uid>", methods=["DELETE"])
def delete_staff(uid):
    staff = Staff.query.get(uid)
    if not staff:
        return jsonify({"error": "Staff not found"}), 404

    db.session.delete(staff)
    db.session.commit()

    return jsonify({"message": "Staff deleted successfully"})


if __name__ == '__main__':
    app.run(debug=True)