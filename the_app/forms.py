from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, SubmitField, HiddenField
from wtforms.validators import DataRequired, Length, ValidationError

def valida_coste(form, field):
    if field.data > form.precio_unitario.data:
        raise ValidationError('Ya te he dicho que el coste unitario ha de ser menor que el precio.')

class ProductForm(FlaskForm):
    id = HiddenField('id')
    tipo_producto = StringField('Tipo de Producto', validators=[DataRequired(), Length(min=3, message="Debe tener al menos tres caracteres")])
    precio_unitario = FloatField('Precio U.', validators=[DataRequired(message="Introduce algo, nano")])
    coste_unitario = FloatField('Coste U.', validators=[DataRequired(), valida_coste])

    submit = SubmitField('Aceptar')

    '''
    def validate_coste_unitario(self, field):
        if field.data > self.precio_unitario.data:
            raise ValidationError('El coste unitario ha de ser menor o igual que el precio ')
    '''