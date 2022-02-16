from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:22441011@localhost/school'
app.config['SQLALCHEMY_BINDS'] = {'postgre': "postgresql://postgres:22441011@localhost/postgres"}

sq = SQLAlchemy(app)


class students(sq.Model):
    id = sq.Column('student_id', sq.Integer, primary_key=True)
    name = sq.Column(sq.String(100))
    marks = sq.Column(sq.String(50))


class office(sq.Model):
    __bind_key__ = 'postgre'
    id = sq.Column('employee_id', sq.Integer, primary_key=True)
    name = sq.Column(sq.String(100))
    points = sq.Column(sq.String(50))


@app.route('/mysql', methods=['GET'])
def mysql():
    data = students.query.all()
    response = {}
    for d in data:
        response[d.id] = {
            "name": d.name,
            "marks": d.marks
        }
    return response


@app.route('/postgresql', methods=['GET'])
def postgre():
    data = office.query.all()
    response = {}
    for d in data:
        response[d.id] = {
            "name": d.name,
            "points": d.points
        }
    return response


if __name__ == '__main__':
    app.run()
