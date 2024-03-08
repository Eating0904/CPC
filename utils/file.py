from pathlib import Path
from utils import format


# 建立 .vue 檔案
def create_vue_file(folder_path, name, template_path):
  component_name = format.to_upper_camel_case(name)
  file_name = f"{component_name}.vue"
  file_path = Path(folder_path) / file_name
  
  with open(template_path, 'r') as file:
    template_content = file.read()
  
  vue_content = template_content.replace("{{ componentName }}", component_name)
  
  with open(file_path, 'w') as file:
    file.write(vue_content)
  
  return file_path

# 建立 index.js 檔案
def create_index_file(folder_path, name, template_path):
  component_name = format.to_upper_camel_case(name)
  file_path = Path(folder_path) / "index.js"
  
  with open(template_path, 'r') as file:
    template_content = file.read()
  
  js_content = template_content.replace("{{ componentName }}", component_name)
  
  with open(file_path, 'w') as file:
    file.write(js_content)
  
  return file_path
