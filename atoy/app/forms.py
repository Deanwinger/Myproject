from flask_wtf import Form
from wtforms import StringField, SubmitField
from wtforms.validators import Required

class PKForm(Form):
    pk1 = StringField(validators=[Required()])
    pk2 = StringField(validators=[Required()])
    submit = SubmitField('PK一下')