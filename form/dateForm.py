from wtforms import Form, StringField, validators, DateTimeField

class DateForm(Form):
    date_cal = StringField('Date', [validators.Length(min=5,max=20)])
    master = StringField('Master', [validators.Length(min=5, max=20)])