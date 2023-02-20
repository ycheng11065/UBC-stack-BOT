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


#helper functions 2
def add_button(dict_buttons, button_name, button_emoji):
  dict_buttons[button_name] = button_emoji

class NaviBot(commands.Bot):

  def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)
    self.setUp()

  # Sets up the bot such that it has additional buttons, current node and
  # other attributes initialized; should run each time we call menu
  def setUp(self, user_using_now=None):
    # declaring the variables
    self.additional_buttons = {}
    self.number_buttons = []
    self.curr_msg = None
    self.user_using_now = None

    #Add additional buttons
    add_button(self.additional_buttons, MENU_BUTTON_NAME, MENU_ICON)
    add_button(self.additional_buttons, BACK_BUTTON_NAME, BACK_ICON)
    add_button(self.additional_buttons, CLOSE_BUTTON_NAME, CLOSE_ICON)

    #Setup the current node
    self.curr_node = PageTree.get_root()

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
