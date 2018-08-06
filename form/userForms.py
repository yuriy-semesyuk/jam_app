from wtforms import Form, StringField, IntegerField, validators


class UserForm(Form):
    date = StringField('Date', [validators.Length(min=1, max=100)])
    time = StringField('Time', [validators.Length(min=1, max=100)])
    type_servis = StringField('Type_servis', [validators.Length(min=1, max=100)])
    master = StringField('Master', [validators.Length(min=1, max=100)])
    firstname = StringField('First name', [validators.Length(min=1, max=100)])
    number = StringField('Number', [validators.Length(min=1, max=100)])
