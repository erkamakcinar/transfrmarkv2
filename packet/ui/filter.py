from flask_wtf import FlaskForm
from wtforms import  IntegerField, SubmitField, StringField, FloatField, SelectMultipleField
from wtforms.validators import DataRequired, Length

class TeamFiler(FlaskForm):
    team_name = StringField('Takım İsmi', default=None)
    cup_num = IntegerField('Kupa Sayısı', default=None)
    total_val = FloatField('Toplam Piyasa Değeri')
    home_towns = StringField('Şehir')
    team_submit = SubmitField('Filtrele')
    team_reset = SubmitField('Reset')

class PlayerFiler(FlaskForm):
    player_name = StringField('Oyuncu İsmi (İçeren)')
    player_team = StringField('Oynadığı Takım')
    player_age_min = IntegerField('Min:')
    player_age_max = IntegerField('Max:')
    player_submit = SubmitField('Filtrele')
    player_reset = SubmitField('Reset')