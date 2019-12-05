import os
from forms import AddForm,DelForm
from flask import Flask, render_template,url_for,redirect,request,flash
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)

app.config['SECRET_KEY'] = 'youwillneverguess'



#####SQL DB SECTION#####


basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+os.path.join(basedir,'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
Migrate(app,db)



#####MODELS######

class Puppy(db.Model):

    __tablename__ = 'puppies'
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.Text)
    color = db.Column(db.Text)
    owner = db.Column(db.Text)

    def __init__(self,name,color,owner):
        self.name = name
        self.color = color
        self.owner = owner

    def __repr__(self):
        return f'Puppy name is {self.name.upper()}, color is {self.color.upper()} and the owner is {self.owner.upper()}'



#VIEW FUNCTIONS ---> HAVE FORMS#


@app.route('/')
def index():
    return render_template('home.html')


@app.route('/add', methods=['GET','POST'])
def add_pupp():

    form = AddForm(request.form)

    if request.method == 'POST' and form.validate():

        name = form.name.data
        color = form.color.data
        owner = form.owner.data

        new_puppy = Puppy(name,color,owner)
        db.session.add(new_puppy)
        db.session.commit()

        flash('Puppy successfully added to our database')

        return redirect(url_for('list_pup'))

        
    return render_template('add.html', form=form)


@app.route('/list')
def list_pup():

    puppies = Puppy.query.all()
    return render_template('list.html', puppies=puppies)


@app.route('/delete', methods=['GET','POST'])
def del_pup():

    form = DelForm(request.form)

    if request.method == 'POST' and form.validate():

        name = form.name.data

        pup = Puppy.query.filter_by(name='pup').first()
        db.session.delete(pup)
        db.session.commit()

        flash('Puppy successfully deleted from the database')

        return redirect(url_for('list_pup'))
    

    return render_template('delete.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)


