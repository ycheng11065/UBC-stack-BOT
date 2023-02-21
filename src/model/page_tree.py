
"""
File representing the pages structure within which the student can navigate.
When imported, builds the whole tree once, and returns its root as a variable.
"""

import json
import os

ROOT_PAGE_PATH = "././data/pages/menu/"

ONE = "1️⃣"
TWO = "2️⃣"
THREE = "3️⃣"
FOUR = "4️⃣"
FIVE = "5️⃣"
SIX = "6️⃣"
SEVEN = "7️⃣"
EIGHT = "8️⃣"
NINE = "9️⃣"
TEN = "🔟"

ALL_BUTTONS = [ONE, TWO, THREE, FOUR, FIVE, SIX, SEVEN, EIGHT, NINE, TEN]

class PageTree:
  root = None

  @staticmethod
  def get_root():
    if not PageTree.root:
      PageTree.root = PageTree.Page(ROOT_PAGE_PATH)
    return PageTree.root

  class Page:

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
      button_count = 0

      for f in os.listdir(path):
        full_path = path + "/" + f
        if os.path.isdir(full_path):
          new_child = PageTree.Page(full_path)
          self.list_children.append(new_child) # list of all children whose json were found
          # dynamically create new entries for embed
          self.list_selection.append({
            "field_name": "",
            "field_value": ALL_BUTTONS[button_count] + "  " + new_child.func_name,
            "field_inline": False
          })
          button_count += 1
