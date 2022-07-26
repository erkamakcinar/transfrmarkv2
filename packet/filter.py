from flask_wtf import FlaskForm
from wtforms import  IntegerField, SubmitField, StringField, FloatField
from wtforms.validators import DataRequired, Length

class TeamFiler(FlaskForm):
    team_name = StringField('Takım İsmi', validators=[DataRequired(), Length(min=0, max=5)])
    cup_num = IntegerField('Kupa Sayısı')
    total_val = FloatField('Toplam Piyasa Değeri')
    submit = SubmitField('TakımBtn')

class PlayerFiler(FlaskForm):
    player_name = StringField('Oyuncu İsmi')
    player_value = FloatField('Piyasa Değeri', validators=[DataRequired()])
    submit = SubmitField('OyuncuBtn')