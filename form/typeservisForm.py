from wtforms import Form, StringField, validators

class TypeservisForm(Form):
    type_s_1=StringField('type_s_1')
    type_s_2=StringField('type_s_2')
    type_s_3=StringField('type_s_3')
    type_s_4=StringField('type_s_4')
    type_s_5=StringField('type_s_5')
    firstname = StringField('First name', [validators.Length(min=1, max=100)])
    number = StringField('Number', [validators.Length(min=1, max=100)])