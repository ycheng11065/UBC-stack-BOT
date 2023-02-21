
"""
Allows you to edit pages rather cleanly, hopefully.
"""

import os
import json
import sys

ROOT_PAGE_PATH = "././data/pages/menu/"
FIELD_NAME_FOR_NAME_OF_FILE = "name_shown_on_bot"


def get_y_n_input(msg):
    got_valid_input = False
    while (not got_valid_input):
        y_or_n = input(msg)
        if y_or_n.casefold() == "y".casefold():
            return True
        elif y_or_n.casefold() == "n".casefold():
            return False
        elif y_or_n.casefold() == "stop".casefold():
            print("TERMINATING.")
            sys.exit(0)
        else:
           print("Not a valid input! Please input y / n!")


class PageTreeEditor:
  root = None

  @staticmethod
  def get_root():
    if not PageTreeEditor.root:
      PageTreeEditor.root = PageTreeEditor.PageInEditor(ROOT_PAGE_PATH)
      print("Process completed!")
    return PageTreeEditor.root

  class PageInEditor:

    def add_new_field_name(self, content):
        # Adding new field name
        if FIELD_NAME_FOR_NAME_OF_FILE not in content.keys():
            to_add_new_fileld_name = get_y_n_input("This page lacks a field name to be exhibited on discord." + 
                                                    "\n" + 
                                                    self.func_name +
                                                    "\n" +
                                                    "Would you like to add a field name? y/n" +
                                                    "\n")
        else:
            to_add_new_fileld_name = get_y_n_input("The current page's field name exhibited on discord is: " + 
                                                    "\n" + 
                                                    content[FIELD_NAME_FOR_NAME_OF_FILE] +
                                                    "\n" +
                                                    "for the page: " +
                                                    "\n" +
                                                    self.func_name +
                                                    "\n" +
                                                    "Would you like to change the field name? y/n" +
                                                    "\n")
                
                
        # If adding new field
        if to_add_new_fileld_name:
            # Loop to get the right name
            got_name_user_wants = False
            while not got_name_user_wants:
                if self.previous_node_selections == None:
                    self.previous_node_selections = ""
                else:
                    temp = ""
                    for n in self.previous_node_selections:
                        temp += (n + "; ")
                    self.previous_node_selections = temp

                new_field_name = input("Please input your new name." + 
                                        "\n" + 
                                        "Previous fields include: " + 
                                        self.previous_node_selections + 
                                        "\n")
                if get_y_n_input("Is this the name you want?" + 
                                "\n" + 
                                new_field_name + 
                                "\n"):
                    content[FIELD_NAME_FOR_NAME_OF_FILE] = new_field_name
                    self.name_shown_on_bot = new_field_name
                    got_name_user_wants = True
                    print("New name added." + 
                            "\n" +
                            "________________________")
        # If not adding new field
        else:
            print("Not adding a new field name." + 
                "\n" +
                "________________________")
            
    def remove_fields(self):
        # For each selection, ask if they want to remove it or not. The removed should be 
        # hardcoded fields
        selections_removed = []

        for selection in self.list_selection:
            removal_loop_over = False
            while (not removal_loop_over):
                if get_y_n_input("Do you want to remove this field?" +
                                "\n" +
                                selection["field_value"] +
                                "\n"):
                    if get_y_n_input("ARE YOU SURE you want to remove this field?" + 
                                        "\n" +
                                        selection["field_value"] + 
                                        "\n"):
                        selections_removed.append(selection["field_value"])
                        self.list_selection.remove(selection)
                        removal_loop_over = True
                        print("Field removed." + 
                                "\n" +
                                "________________________")
                
                else:
                    removal_loop_over = True
                    print("Not removing the field!" + 
                            "\n" +
                            "________________________")
        
        return selections_removed


    def __init__(self, path, previous_node_selections=None):
        # look into folder given
        #  -> read the json
        #   -> create the menu page content out of it
        # -> read the other folders in the path
        #  for each folder in the path, create a new menu object 

        self.list_selection = []
        self.list_children = []
        self.title = ''
        self.func_name = ''
        self.name_shown_on_bot = ''
        self.previous_node_selections = previous_node_selections
        
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
            self.func_name = content['function_name']
            self.title = content['embed']['title']
            self.list_selection = content['embed']['fields']
        
            # Check whether to change this file or not
            if FIELD_NAME_FOR_NAME_OF_FILE in content.keys():
                contains_field_name = "true"
            else:
                contains_field_name = "false"

            change_this_page_at_all = get_y_n_input("Do you want to change this page in any way?""\n" + 
                                                    self.func_name +
                                                    "\n" +
                                                    "Containing a field name or not: " +
                                                    contains_field_name +
                                                    "\n")
            
            if change_this_page_at_all:
                self.add_new_field_name(content)
                selections_removed = self.remove_fields()
            else:
                selections_removed = []

        # write the content to the same file
        content_to_be_dumped = {}
        new_embed = {}
        new_embed['title'] = self.title
        new_embed['fields'] = self.list_selection
        content_to_be_dumped['function_name'] = self.func_name
        content_to_be_dumped[FIELD_NAME_FOR_NAME_OF_FILE] = self.name_shown_on_bot
        content_to_be_dumped['embed'] = new_embed
        
        with open(json_path, "w") as file:
            json_content_to_be_dumped = json.dumps(content_to_be_dumped)
            file.write(json_content_to_be_dumped)

                        
        # for every folder in this folder, run the same thing
        
        for f in os.listdir(path):
            full_path = path + "/" + f
            if os.path.isdir(full_path):
                new_child = PageTreeEditor.PageInEditor(full_path, selections_removed)


if __name__ == "__main__":
    PageTreeEditor.get_root()