from string import Template
from utils import format


def add_route_to_menuRoutes(file_path, name):
  menuRoutes_path = '/' + format.to_kebab_case(name)
  menuRoutes_name = format.to_upper_camel_case(name)

  route_template = Template('''  {
    path: '$path',
    name: '$name',
  },\n''')

  new_route_content = route_template.substitute(path=menuRoutes_path, name=menuRoutes_name)

  with open(file_path, 'r') as file:
    content = file.readlines()

  insert_index = None
  for i, line in enumerate(content):
    if 'path:' in line:
      current_path = line.split("'")[1]
      if menuRoutes_path < current_path:
        insert_index = i - 1
        break
  if insert_index is None:
    insert_index = len(content) - 1

  content.insert(insert_index, new_route_content)

  with open(file_path, 'w') as file:
    file.writelines(content)