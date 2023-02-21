import discord
from discord.ext import commands
import page_tree
from page_tree import PageTree


ARROW_LEFT = "⬅"
ARROW_RIGHT = "➡"

BACK_ICON = ARROW_LEFT
MENU_ICON = "🏠" #"⏪"
CLOSE_ICON = "❌"

BACK_BUTTON_NAME = "back_button"
MENU_BUTTON_NAME = "menu_button"
CLOSE_BUTTON_NAME = "close_button"

ALL_BUTTONS = page_tree.ALL_BUTTONS_IN_UNICODE

class NaviBot(commands.Bot):

  def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)


  def menu_button_func(self):
    next_node = PageTree.get_root()
    self.stack.append(self.curr_node)
    return next_node

  def back_button_func(self):
    if len(self.stack) != 0:
      next_node = self.stack.pop()
    else:
      next_node = self.curr_node
    return next_node

  def close_button_func(self):
    exit(0)

  def process_number_buttons(self, action):
    user_reaction_num = self.number_buttons.index(action)
    next_node = self.curr_node.list_children[user_reaction_num]
    self.stack.append(self.curr_node)
    return next_node

  # Sets up the bot such that it has additional buttons, current node and
  # other attributes initialized; should run each time we call menu
  def setUp(self, user_using_now=None):
    # declaring the variables
    self.option_buttons = {}
    self.option_button_functions = {}
    self.curr_msg = None
    self.user_using_now = None

    #Add additional buttons
    self.add_option_button(MENU_BUTTON_NAME, MENU_ICON, self.menu_button_func)
    self.add_option_button(BACK_BUTTON_NAME, BACK_ICON, self.back_button_func)
    self.add_option_button(CLOSE_BUTTON_NAME, CLOSE_ICON, self.close_button_func)

    #Setup the current node
    self.curr_node = PageTree.get_root()

    #Setup number buttons
    curr_num_buttons = len(self.curr_node.list_children)
    self.number_buttons = ALL_BUTTONS[0:curr_num_buttons]

    #Setup the stack
    self.stack = []

    #Setup the user to a single person
    if user_using_now:
      self.user_using_now = user_using_now

  # Creates an embed using the current node and current author
  def create_curr_node_embed(self):
    embed_to_return = discord.Embed(title=self.curr_node.title)
    for field in self.curr_node.list_selection:
      embed_to_return.add_field(name=field["field_name"],
                                value=field["field_value"],
                                inline=field["field_inline"])
    embed_to_return.set_footer(text=f'Hi {self.user_using_now}')

    return embed_to_return
  

  # Add an option button to the list
  def add_option_button(self, button_name, button_emoji, b_func):
    self.option_buttons[button_emoji] = button_name
    self.option_button_functions[button_emoji] = b_func


  # Process reactions by changing buttons and the current node accordingly, and 
  # returning the old number button list
  def process_action(self, action):
    if action not in (self.number_buttons + list(self.option_buttons.keys())):
        return

    # 1) get the user's action and update curr_node to according next node

    # process the additional buttons FIRST
    # if action is in the optional buttons
    if action in self.option_buttons.keys():
      # then execute the according function
      next_node = self.option_button_functions[action]()

    else:
      next_node = self.process_number_buttons(action)

    # 3) update the current node to the next node and set the number of buttons (= the number of its children)
    self.curr_node = next_node
    curr_num_buttons = len(self.curr_node.list_children)
    self.number_buttons = ALL_BUTTONS[0:curr_num_buttons]

    return 