from wtforms import Form, StringField, validators, DateTimeField

class MasterForm(Form):
    master_name = StringField('master_name', [validators.Length(min=1, max=100)])