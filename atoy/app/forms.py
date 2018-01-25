from flask_wtf import Form
from wtforms import StringField, SubmitField
from wtforms.validators import Required

class PKForm(Form):
    pk1 = StringField('一号选手', validators=[Required()])
    pk2 = StringField('二号选手', validators=[Required()])
    submit = SubmitField('PK一下')