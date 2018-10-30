from wtforms import StringField, IntegerField, validators, Form

class UserForm(Form):
    username = StringField('Username', [validators.length(max=20)])
    # username = StringField('Username')
    password = StringField('Password', [validators.length(max=20)])
    # number = IntegerField('Number')