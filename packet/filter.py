from flask_wtf import FlaskForm
from wtforms import  IntegerField, SubmitField, StringField, FloatField, SelectMultipleField
from wtforms.validators import DataRequired, Length

class TeamFiler(FlaskForm):
    team_name = StringField('Takım İsmi', validators=[DataRequired(), Length(min=0, max=5)])
    cup_num = IntegerField('Kupa Sayısı')
    total_val = FloatField('Toplam Piyasa Değeri')
    home_towns = StringField('Şehir')
    team_submit = SubmitField('Filtrele')

class PlayerFiler(FlaskForm):
    player_name = StringField('Oyuncu İsmi')
    player_value = FloatField('Piyasa Değeri', validators=[DataRequired()])
    player_pos = SelectMultipleField('Mevki', choices= [('11', 'Tüm mevkiler'), ('1', 'Kaleci'), ('2', 'Stoper'), ('3', 'Sol Bek'), ('4', 'Sağ Bek'), ('5', 'Ön Libero'), ('6', 'Orta Saha'), ('7', 'On Numara'), ('8', 'Sağ Kanat'), ('9', 'Sol Kanat'), ('10', 'Santrafor')])
    player_submit = SubmitField('Filtrele')