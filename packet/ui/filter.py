from flask_wtf import FlaskForm
from wtforms import  IntegerField, SubmitField, StringField, FloatField, SelectMultipleField
from wtforms.validators import DataRequired, Length

class TeamFiler(FlaskForm):
    team_name = StringField('Takım İsmi', default=None)
    kupa_min = IntegerField('Min:', default=None)
    kupa_max = IntegerField('Max:', default=None)
    total_val = FloatField('Toplam Piyasa Değeri')
    home_towns = StringField('Şehir')
    team_submit = SubmitField('Filtrele')
    team_reset = SubmitField('Reset')

class PlayerFiler(FlaskForm):
    player_name = StringField('Oyuncu İsmi')
    player_surname = StringField('Oyuncu Soyismi')
    player_team = StringField('Oynadığı Takım')
    player_country = StringField('Uyruk')
    player_age = IntegerField('Yaş')
    player_value = FloatField('Piyasa Değeri')
    player_pos = SelectMultipleField('Mevki', choices= [('11', 'Tüm mevkiler'), ('1', 'Kaleci'), ('2', 'Stoper'), ('3', 'Sol Bek'), ('4', 'Sağ Bek'), ('5', 'Ön Libero'), ('6', 'Orta Saha'), ('7', 'On Numara'), ('8', 'Sağ Kanat'), ('9', 'Sol Kanat'), ('10', 'Santrafor')])
    player_submit = SubmitField('Filtrele')
    player_reset = SubmitField('Reset')