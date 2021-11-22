def cellphone_macapa_format(cellphone):
  """
  Format cellphone to format +55 (41) 93030-6905
  """

  if not cellphone:
    return None

  formatted_cellphone = f'+{cellphone[:2]} ({cellphone[2:4]}) {cellphone[4:9]}-{cellphone[9:]}'

  return formatted_cellphone

def cellphone_varejao_format(cellphone):
  import re
  """
  Format cellphone to format 5541930306905
  """

  if not cellphone:
    return None

  numeric_filter = filter(str.isdigit, cellphone)
  formatted_cellphone = "".join(numeric_filter)

  return formatted_cellphone

def parse_customer(email):
  """
  Parse customer from email
  """

  if not email:
    return None

  customer = email.split('@')[1].split('.')[0]

  if customer not in ['macapa', 'varejao']:
    return 'Invalid creditor'

  return customer