from utils import folder, file, route
from config import *


if __name__ == "__main__":
  # 目標專案
  target_project = "app-plugin/testpage"
  base_path = f"../../{target_project}/src/pages" # 目前只是用於 app-plugin 的測試頁面

  # 建立的名稱
  name = "testFolder"

  try:
    folder_path = folder.create(base_path, name)

    file.create_vue_file(folder_path, name, vue_template_path)
    file.create_index_file(folder_path, name, index_template_path)

    route.add_route_to_menuRoutes(file_path, name)

    print('完成')
  except SystemExit as e:
    print("程序已終止。")