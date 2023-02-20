import json
import os

ORIGINAL_MENU_PATH = "././data/pages/menu/"

class Menu():
  list_selection = []
  list_children = []
  title = ''
  func_name = ''

  def __init__(self, path):
    # look into folder given
    #  -> read the json
    #   -> create the menu page content out of it
    # -> read the other folders in the path
    #  for each folder in the path, create a new menu object 

    self.list_selection = []
    self.list_children = []
    self.title = ''
    self.func_name = ''
    
    # if it contains a json with same name as itself
    page_found = False
    
    for f in os.listdir(path):
      if f.endswith(".json"):
        json_path = path + "/" + f
        page_found = True
        break

    if not page_found:
      print("No such page found.")
      return
        
    # reads that
    with open(json_path, "r") as file:
      json_content = file.read()
      content = json.loads(json_content)
      # {course_nav: folders, select2: null, select3: null}
      self.func_name = content['function_name']
      self.title = content['embed']['title']
      self.list_selection = content['embed']['fields']


    # I build the menu as I want it with the content read

    # for every folder in this folder, run the same thing
    for f in os.listdir(path):
      full_path = path + "/" + f
      if os.path.isdir(full_path):
        new_child = Menu(full_path)
        self.list_children.append(new_child) # list of all children whose json were found

    

def return_root_of_tree():
  root = Menu(ORIGINAL_MENU_PATH)
  return root