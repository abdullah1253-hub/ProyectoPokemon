from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length

class TrainerForm(FlaskForm):
    trainer = StringField(
        'Trainer Name',
        validators=[
            DataRequired(message="Trainer name is required."),
            Length(min=3, max=15, message="Trainer's name should be between 3 and 15 characters.")
        ]
    )
    submit = SubmitField('Continue')