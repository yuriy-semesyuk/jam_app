from wtforms import Form, StringField, validators, DateTimeField, IntegerField

class PriceForm(Form):
    master_name = StringField('master_name', [validators.Length(min=1, max=100)])
    servis_name = StringField('servis_name', [validators.Length(min=1, max=100)])
    servis_cost = StringField('servis_cost', [validators.Length(min=1, max=100)])
    servis_duration = StringField('servis_duration', [validators.Length(min=1, max=100)])