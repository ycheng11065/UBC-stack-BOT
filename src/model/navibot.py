import discord
from discord.ext import commands
from page_tree import PageTree


ARROW_LEFT = "⬅"
ARROW_RIGHT = "➡"
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

BACK_ICON = ARROW_LEFT
MENU_ICON = "⏪"
CLOSE_ICON = "❌"

BACK_BUTTON_NAME = "back_button"
MENU_BUTTON_NAME = "menu_button"
CLOSE_BUTTON_NAME = "close_button"
NUMBER_BUTTONS_NAME = "number_buttons"

ALL_BUTTONS = [ONE, TWO, THREE, FOUR, FIVE, SIX, SEVEN, EIGHT, NINE, TEN]


class NaviBot(commands.Bot):

  def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)
  

  # Sets up the bot such that it has additional buttons, current node and
  # other attributes initialized; should run each time we call menu
  def setUp(self, user_using_now=None):
    # declaring the variables
    self.option_buttons = {}
    self.curr_msg = None
    self.user_using_now = None

    #Add additional buttons
    self.add_option_button(MENU_BUTTON_NAME, MENU_ICON)
    self.add_option_button(BACK_BUTTON_NAME, BACK_ICON)
    self.add_option_button(CLOSE_BUTTON_NAME, CLOSE_ICON)

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
  def add_option_button(self, button_name, button_emoji):
    self.option_buttons[button_name] = button_emoji


  # Process reactions by changing buttons and the current node accordingly  
  def process_action(self, action):
    if action not in (self.number_buttons + list(self.option_buttons.values())):
        return

    # 1) get the user's action and update curr_node to according next node

    # TODO Make use of the function-as-parameter to make this a much cleaner and conceptual code
    # process the additional buttons FIRST
    if (action == self.option_buttons[BACK_BUTTON_NAME]):
      if len(self.stack) != 0:
        next_node = self.stack.pop()
      else:
          next_node = self.curr_node

    elif (action == self.option_buttons[MENU_BUTTON_NAME]):
      next_node = PageTree.get_root()
      self.stack.append(self.curr_node)

    # TODO FIND A WAY TO MAKE THIS BE IN THE MAIN FILE (AS IT SEEMS MORE UI THAN MODEL)    
    elif (action == self.option_buttons[CLOSE_BUTTON_NAME]):
      self.curr_msg.delete()
      exit(0)

    else:
      for i in range(len(self.number_buttons)):
        if action == self.number_buttons[i]:
          user_reaction_num = i
          break
      next_node = self.curr_node.list_children[user_reaction_num]
      self.stack.append(self.curr_node)

    # 3) update the current node to the next node and set the number of buttons (= the number of its children)
    self.curr_node = next_node
    curr_num_buttons = len(self.curr_node.list_children)
    self.new_number_buttons = ALL_BUTTONS[0:curr_num_buttons]