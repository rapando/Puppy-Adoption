from wtforms import Form, StringField,IntegerField,SubmitField,validators


class AddForm(Form):
    name = StringField('Name',[
        validators.required(), validators.Length(min=1,max=50)])
    color = StringField('Color',[
        validators.required(), validators.Length(min=1,max=50)])
    owner = StringField('Owner',[
        validators.required(), validators.Length(min=1,max=50)])
    submit = SubmitField('Submit')

class DelForm(Form):

    name = StringField('Name to remove: ')
    submit = SubmitField('Remove')
