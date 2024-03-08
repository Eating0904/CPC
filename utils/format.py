def to_lower_camel_case(name):
  return name[0].lower() + name[1:]

def to_upper_camel_case(name):
  return name[0].upper() + name[1:]

def to_kebab_case(name):
  transformed_characters = []
  for c in name:
    if c.isupper():
      transformed_characters.append('-' + c.lower())
    else:
      transformed_characters.append(c)
  kebab_case_name = ''.join(transformed_characters)

  return kebab_case_name