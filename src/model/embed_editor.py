
"""
Class which allows to create embeds systematically through console.

A template json looks like this:


{ 
    "function_name": FUNCTION NAME (NO REAL USE YET),
    "name_shown_on_bot": NAME DISPLAYED IN DISCORD IN PARENTS,
    "embed": 
    {
        "title": TITLE OF EMBED,
        "fields_before": [ ALL FIELDS HERE PUT BEFORE DYNAMICALLY CREATED FIELDS
        {
            "field_name": FIELD NAME,
            "field_value": FIELD VALUE,
            "field_inline": IF FIELD IS INLINE
        }
        ],
        "fields_after": [ ALL FIELDS HERE PUT AFTER DYNAMICALLY CREATED FIELDS
        {
            "field_name": FIELD NAME,
            "field_value": FIELD VALUE,
            "field_inline": IF FIELD IS INLINE
        }
        ]
    }
}
"""

import json
import sys


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

def get_input_loop(msg):
    is_satisfied_with_input = False
    while (not is_satisfied_with_input):
        new_input = input(msg)
        is_satisfied_with_input = get_y_n_input("Are you satisfied with this input? y/n" + 
                                                "\n" + 
                                                new_input +
                                                "\n")
    
    print("New input set! \n")
    return new_input

class EmbedEditor:

    def __init__(self, path=None):

        self.function_name = ""
        self.name_shown_on_bot = ""
        self.embed_title = ""
        self.fields_before = []
        self.fields_after = []

        if path != None:
            self.path = path
    
    def readJSON(self):
        if self.path == None:
            print("readJSON called without path set to any value!")
            return

        with open(self.path, "r") as file:
            json_content = file.read()
            content = json.loads(json_content)

            self.function_name = content["function_name"]
            self.name_shown_on_bot = content["name_shown_on_bot"]
            self.embed_title = content["embed"]["title"]
            #New fields
            if "fields_before" in content.keys():
                self.fields_before = content["embed"]["fields_before"]
            else:
                self.fields_before = []
                
            if "fields_after" in content.keys():
                self.fields_after = content["embed"]["fields_after"]
            else:
                self.fields_after = []
            
            # Old fields
            if "fields" in content.keys(): self.fields_before = content["embed"]["fields"]

    def writeJSON(self, path=None):
        if path == None:
            path = self.path
        
        with open(path, "w") as file:
            content = {}
            
            embed = {}
            embed["title"] = self.embed_title
            embed["fields_before"] = self.fields_before
            embed["fields_after"] = self.fields_after

            content["function_name"] = self.function_name
            content["name_shown_on_bot"] = self.name_shown_on_bot
            content["embed"] = embed

            json_content_to_be_written = json.dumps(content)
            file.write(json_content_to_be_written)

            print("Writing to file " + path + " finished.")
        

    
    def return_embed(self):
        embed = {}
        embed["title"] = self.embed_title
        embed["fields_before"] = self.fields_before
        embed["fields_after"] = self.fields_after
        return embed
    
    def set_path(self, path):
        self.path = path

    def _update_string_field_or_not(self, field_name, actual_field):
        if get_y_n_input("Do you want a new " + field_name + "? Currently it is: " + 
                         "\n" +
                         actual_field + 
                         "\n" +
                         "y/n \n"):
            new_field_val = get_input_loop("What is the new " + field_name + "?\n")
            return new_field_val
        
        return None
    
    def _show_single_field(self, field):
        print("-field_name: ",     field["field_name"])
        print("-field_value: ",   field["field_value"])
        print("-field_inline: ", field["field_inline"])
    
    def _show_list_of_fields(self, fields):
        print("Currently have " + str(len(fields)) + " fields:")
        for i in range(len(fields)):
            field = fields[i]
            print("Field " + str(i) + ":")
            self._show_single_field(field)

    def _choose_what_to_do(self):
        got_valid_input = False
        while(not got_valid_input):
            choice = input("Would you like to: \n 1) ADD \n 2) CHANGE \n 3) REMOVE \n" +
                           " a new field, or 4) STOP, the loop? \n")
            if ((choice.casefold() ==    "ADD".casefold()) or 
                (choice.casefold() == "CHANGE".casefold()) or
                (choice.casefold() == "REMOVE".casefold()) or
                (choice.casefold() ==   "STOP".casefold())):
                return choice.casefold()
            else:
                print("Input was not valid! Please choose one of the options. \n")


    def _make_new_field(self):
        new_field = {}
        new_field["field_name"] = get_input_loop("What is the name of your new field?\n")
        new_field["field_value"] = get_input_loop("What is the value of your new field?\n")
        new_field["field_inline"] = get_y_n_input("Is your new field inline? y/n \n")
        return new_field

    def get_valid_position(self, msg, fields):
        got_valid_position = False
        while (not got_valid_position):
            print(msg)
            
            self._show_list_of_fields(fields)
            
            pos = input("The order is 0-indexed.\n")
            
            try:
                obtained_pos = int(pos)
                if (obtained_pos < 0) or (obtained_pos > len(fields)):
                    print("Position is out of bounds of the given field; input again!")
                else:
                    got_valid_position = True
            except:
                print("Input wasn't convertible to int. Please input again (in form '1').")
        return obtained_pos


    def _helper_add_field(self, fields, pos):
        new_field = self._make_new_field()
        fields.insert(pos, new_field)
        print("Field inserted!")
        return fields

    def _add_field(self, fields):
        valid_pos = self.get_valid_position("Which position in the list do you want to insert this field, in number (like 1)? \n" + 
                                            "The current list of fields is: ", fields)
        fields = self._helper_add_field(fields, valid_pos)
        return fields
    
    def _helper_remove_field(self, fields, pos):
        if len(fields) == 0:
            print("Fields is empty!")
            return fields
        fields.remove(fields[pos]) # assumption is that there are no identical fields
        print("Field removed!")
        return fields
    
    def _remove_field(self, fields):
        remove_pos = self.get_valid_position("Which position in the list do you want to remove this field from, in number (like 1)? \n" + 
                                            "The current list of fields is: ", fields)
        fields = self._helper_remove_field(fields, remove_pos)
        return fields
    
    def _change_field(self, fields):
        if len(fields) == 0:
            print("Fields is empty!")
            return fields
        change_pos = self.get_valid_position("Which position in the list do you want to change, in number (like 1)? \n" + 
                                            "The current list of fields is: ", fields)
        # copy the field that is at the position, displaying it
        print("The field to be changed is:")
        self._show_single_field(fields[change_pos])
        # remove the object at the current position
        self._helper_remove_field(fields, change_pos)
        # add a new field, prompt the user to make it, and insert it at the same index
        self._helper_add_field(fields, change_pos)
        print("Field changed!")
        return fields
    
    def _edit_fields(self, fields):
        self._show_list_of_fields(fields)
        done_with_editing = False
        while (not done_with_editing):
            action = self._choose_what_to_do()
            if action == "add":
                fields = self._add_field(fields)
            elif action == "change":
                fields = self._change_field(fields)
            elif action == "remove":
                fields = self._remove_field(fields)
            elif action == "stop":
                done_with_editing = True
            print("Current field is: ")
            self._show_list_of_fields(fields)

        return fields
    
    def change_node_content(self):
        print("Changing node content.")

        updated_func_name = self._update_string_field_or_not("function name", self.function_name)
        if not updated_func_name == None:
            self.function_name = updated_func_name
        
        updated_name_shown_on_bot = self._update_string_field_or_not("name shown on bot", self.name_shown_on_bot)
        if not updated_name_shown_on_bot == None:
            self.name_shown_on_bot = updated_name_shown_on_bot
        
        updated_embed_title = self._update_string_field_or_not("embed title", self.embed_title)
        if not updated_embed_title == None:
            self.embed_title = updated_embed_title

        self.fields_before = self._edit_fields(self.fields_before)
        self.fields_after = self._edit_fields(self.fields_after)

if __name__ == "__main__":
    editor = EmbedEditor("data/pages_made/test.json")
    editor.readJSON()
    editor.change_node_content()
    editor.writeJSON()