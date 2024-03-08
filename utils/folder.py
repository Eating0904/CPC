import os
import sys
from pathlib import Path
from utils import format


def create(base_path, name):
  folder_name = format.to_lower_camel_case(name)
  folder_path = Path(base_path) / folder_name

  if folder_path.exists():
    print(f"Error： '{folder_name}' 已存在")
    sys.exit(1)
  else:
    os.makedirs(folder_path, exist_ok=True)
    
  return folder_path