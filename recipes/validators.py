import pint
from pint.errors import UndefinedUnitError
from django.core.exceptions import ValidationError


valid_unit_measurements = ['pounds','lbs','oz', 'grams']

def validate_unit_of_measure(value):
  print("Entered validation")
  ureg = pint.UnitRegistry()
  try:
    single_unit = ureg[value]
    print(single_unit)
  except UndefinedUnitError:
    raise ValidationError(f'{value} is not a valid unit of measurememnt')
  except:
    raise ValidationError(f'{value} is invalid. Unknown Error')

